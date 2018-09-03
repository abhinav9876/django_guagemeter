from django.db import models

# Create your models here.
class user(models.Model):
    fname    = models.CharField(max_length=30)
    lname    = models.CharField(max_length=30)
    email    = models.CharField(max_length=50)
    pnumber  = models.IntegerField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email
    def isLoggedIn( email, password):
        check = user.objects.filter(email=email,password=password)
        print(check,"hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")

        user1 = check.first().__dict__
        return user1, check.count()


#datatable models
class Datatable(models.Model):
    someAttr1 = models.CharField(max_length=30)
    someAttr2 = models.CharField(max_length=30)
    someAttr3 = models.CharField(max_length=30)
    someAttr4 = models.CharField(max_length=30)
    someAttr5 = models.CharField(max_length=30)
    someAttr6 = models.CharField(max_length=30)
    someAttr7 = models.CharField(max_length=30)
    someAttr8 = models.CharField(max_length=30)
    someAttr9 = models.CharField(max_length=30)
    someAttr10 = models.CharField(max_length=30)
    someAttr11 = models.CharField(max_length=30)
