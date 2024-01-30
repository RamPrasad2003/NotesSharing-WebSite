from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login,logout
from datetime import date

def about(request):
    return render(request,'about.html')

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def userlogin(request):
    error=""
    if request.method=='POST':
        u=request.POST['emailid']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        try:
            if user:
                login(request,user)
                error='no'
            else:
                error='yes'
        except:
            error='yes'
    d={'error':error}
    return render(request,'login.html',d)

def adminlogin(request):
    error=""
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error='no'
            else:
                error='yes'
        except:
            error='yes'
    d={'error':error}
    return render(request,'adminlogin.html',d)

def signup1(request):
    error=""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        con=request.POST['contact']
        email=request.POST['emailid']
        pwd=request.POST['pwd']
        branch=request.POST['branch']
        role=request.POST['role']
        try:
            user=User.objects.create_user(username=email,password=pwd,first_name=f,last_name=l)
            SignUp.objects.create(user=user,contact=con,branch=branch,role=role)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'signup.html',d)

def adminhome(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    error=False
    a=len(Notes.objects.filter(status='pending'))
    b=len(Notes.objects.filter(status='Accept'))
    c=len(Notes.objects.filter(status='Reject'))
    d=len(Notes.objects.all())
    e={'a':a,'b':b,'c':c,'d':d}
    return render(request,'adminhome.html',e)

def profile(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error=False
    user=User.objects.get(id=request.user.id)
    data=SignUp.objects.get(user=user)
    d={'data':data,'user':user}
    return render(request,'profile.html',d)

def Logout(request):
    logout(request)
    return redirect('index')

def changepass(request):
    error=""
    if not request.user.is_authenticated:
        return redirect('userlogin')
    if request.POST:
        old=request.POST['old']
        new=request.POST['new']
        confirm=request.POST['confirm']
        if confirm==new:
            u=User.objects.get(username__exact=request.user.username)
            u.set_password(new)
            u.save()
            error='no'
        else:
            error='yes'
    d={'error':error}
    return render(request,'changepass.html',d)

def editprofile(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error=False
    user=User.objects.get(id=request.user.id)
    data=SignUp.objects.get(user=user)
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        c=request.POST['con']
        b=request.POST['branch']
        user.first_name=f
        user.last_name=l
        data.contact=c
        data.branch=b
        user.save()
        data.save()
        error=True
    d={'data':data,'user':user,'error':error}
    return render(request,'editprofile.html',d)

def upload_notes(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error=""
    if request.method=='POST':
        b=request.POST['branch']
        s=request.POST['subject']
        n=request.FILES['notesfile']
        f=request.POST['filetype']
        d=request.POST['description']
        print(n)
        ct=User.objects.filter(username=request.user.username).first()
        try:
            Notes.objects.create(user=ct,uploadingdate=date.today(),branch=b,subject=s,notesfile=n,filetype=f,description=d,status='pending')
            error="no"
        except:
            error='yes'
    d={'error':error}
    return render(request,'upload_notes.html',d)

def view_notes(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error=False
    notes=Notes.objects.filter(status='Accept')
    d={'notes':notes}
    return render(request,'view_notes.html',d)

def delete_mynotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    notes=Notes.objects.get(id=pid)
    notes.delete()
    return redirect('view_notes')

def view_user(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error=False
    users=SignUp.objects.all()
    d={'users':users}
    return render(request,'view_user.html',d)

def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    notes=User.objects.get(id=pid)
    notes.delete()
    return redirect('view_user')

def pending_notes(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    error=False
    notes=Notes.objects.filter(status='pending')
    d={'notes':notes}
    return render(request,'pending_notes.html',d)

def assign_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    notes=Notes.objects.get(id=pid)
    error=""
    try:
        if request.method=='POST':
            b=request.POST['status']
            notes.status=b
            error='no'
            notes.save()
    except:
        error='yes'
    d={'error':error,'notes':notes}
    return render(request,'assign_status.html',d)

def accepted_notes(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    error=False
    notes=Notes.objects.filter(status='Accept')
    d={'notes':notes}
    return render(request,'accepted_notes.html',d)

def rejected_notes(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    error=False
    notes=Notes.objects.filter(status='Reject')
    d={'notes':notes}
    return render(request,'rejected_notes.html',d)

def all_notes(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    error=False
    notes=Notes.objects.all()
    d={'notes':notes}
    return render(request,'all_notes.html',d)

def delete_notes(request,pid):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    notes=Notes.objects.get(id=pid)
    notes.delete()
    return redirect('all_notes')

def allnotes(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error=False
    notes=Notes.objects.filter(status='Accept')
    d={'notes':notes}
    return render(request,'allnotes.html',d)


