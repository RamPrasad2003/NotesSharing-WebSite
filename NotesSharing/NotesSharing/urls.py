"""
URL configuration for NotesSharing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path('userlogin',userlogin,name='userlogin'),
    path('adminlogin',adminlogin,name='adminlogin'),
    path('signup',signup1,name='signup'),
    path('adminhome',adminhome,name='adminhome'),
    path('Logout',Logout,name='Logout'),
    path('profile',profile,name='profile'),
    path('changepass',changepass,name='changepass'),
    path('editprofile',editprofile,name='editprofile'),
    path('upload_notes',upload_notes,name='upload_notes'),
    path('view_notes',view_notes,name='view_notes'),
    path('delete_mynotes/<int:pid>',delete_mynotes,name='delete_mynotes'),
    path('delete_notes/<int:pid>',delete_notes,name='delete_notes'),
    path('delete_user/<int:pid>',delete_user,name='delete_user'),
    path('pending_notes',pending_notes,name='pending_notes'),
    path('accepted_notes',accepted_notes,name='accepted_notes'),
    path('rejected_notes',rejected_notes,name='rejected_notes'),
    path('all_notes',all_notes,name='all_notes'),
    path('allnotes',allnotes,name='allnotes'),
    path('assign_status/<int:pid>',assign_status,name='assign_status'),
    path('view_user',view_user,name='view_user'),
    path('',index,name='index')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
