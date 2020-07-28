from django.db import models

# Create your models here.

class Userdata(models.Model):
    Username=models.CharField(max_length=20)
    Email=models.EmailField(unique=True,primary_key=True)
    Password1=models.CharField(max_length=20)
    Password2=models.CharField(max_length=20)
    City=models.CharField(max_length=50)
    def __str__(self):
        return self.Email

class publish(models.Model):
    Userid=models.ForeignKey(Userdata,on_delete=models.CASCADE)
    tittle=models.CharField(max_length=20)
    contend=models.TextField(max_length=20000)
    def __str__(self):
        return self.tittle

class image(models.Model):

    img1=models.ImageField(null=True,blank=True)
    img2=models.ImageField(null=True,blank=True)
    img3=models.ImageField(null=True,blank=True)

class TopUser(models.Model):
    mail1=models.EmailField(unique=True)
    def __str__(self):
        return self.mail1
