from django.db import models
from django.contrib.auth.models import User

class SignUp(models.Model):
    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    contact=models.CharField(null=True, max_length=10)
    branch=models.CharField(null=True, max_length=30)
    role=models.CharField(null=True, max_length=15)
    def __str__(self):
        return self.user.username

class Notes(models.Model):
    user=models.ForeignKey(User,  on_delete=models.CASCADE)
    uploadingdate=models.CharField( max_length=30)
    branch=models.CharField( max_length=30)
    subject=models.CharField( max_length=30)
    notesfile=models.FileField(null=True)
    filetype=models.CharField(null=True,max_length=15)
    description=models.CharField(max_length=200)
    status=models.CharField(null=True,max_length=15)
    def __str__(self):
        return self.user.username+" "+self.status
    