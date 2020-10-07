from django.forms import  ModelForm,Textarea
from django.db import models
class Login(models.Model):
     userid= models.CharField(max_length=50,null=True)
     pwd=models.CharField(max_length=8,null=True)
class Addstudents(models.Model):
	Entername=models.CharField(max_length=50)
	Emailid=models.EmailField(max_length=50)
	Contactno=models.IntegerField(null=True)
	EnterAddress=models.CharField(max_length=20)
	SelectYear=models.IntegerField(null=True)
	SelectGender=models.CharField(max_length=20)
	Rollno=models.IntegerField(null=True)
	SelectDepartment=models.CharField(max_length=20)
	SelectSemester=models.IntegerField(null=True)
class Subjectreport(models.Model):
	EnterName=models.CharField(max_length=15)
	Rollno=models.CharField(max_length=50,null=True)
	SelectDepartment=models.CharField(max_length=15)
	SelectSemester=models.IntegerField(null=True)





           # Create your models here.

# Create your models here.
