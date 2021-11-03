from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Image(models.Model):
 photo = models.ImageField(upload_to="myimage")
 date = models.DateTimeField(auto_now_add=True)

class Jobregistration(models.Model):
     name=models.CharField(max_length=20)
     eamil=models.EmailField(max_length=254)
     highestqualification=models.CharField(max_length=30)
     yearofpassing=models.IntegerField()
     phone=models.IntegerField()
     address=models.CharField(max_length=60)
     experienceInYear=models.IntegerField()
    #  photo=models.ImageField(uplode_to="myimage")
     date=models.DateTimeField(auto_now_add=True)



     def  __str__(self):
         return self.user.name
