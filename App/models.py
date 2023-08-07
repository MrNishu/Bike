from django.db import models

# Create your models here.
class MyDb(models.Model):
    Full_Name = models.CharField(max_length=20)
    EMail = models.EmailField()
    Querry = models.CharField(max_length=500)
    Gender = models.CharField(max_length=10) 



    def __str__(self):
        return f'Name : {self.Full_Name}, Querries : {self.Querry}'





class Admin(models.Model):
    AdminID = models.CharField(max_length=20)
    AdminKey = models.IntegerField()
    AdminPassword = models.CharField(max_length=20)
    

