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
	Rollno=models.CharField(max_length=20,null=True)
	SelectDepartment=models.CharField(max_length=20)
	SelectSemester=models.IntegerField(null=True)
class Studentsreport(models.Model):
	Entername=models.CharField(max_length=50)
	Rollno=models.CharField(max_length=20,null=True)
	SelectDepartment=models.CharField(max_length=20)
	SelectSemester=models.IntegerField(null=True)
class Addsubject(models.Model):
	SelectYear=models.IntegerField(null=True)
	SelectSemester=models.IntegerField(null=True)
	SelectDepartment=models.CharField(max_length=20)
	Entersubjectcode=models.CharField(max_length=20,null=True)
	Entersubjectname=models.CharField(max_length=50)
class Addusers(models.Model):
	Entername=models.CharField(max_length=50)
	Emailid=models.EmailField(max_length=50)
	Contactno=models.IntegerField(null=True)
	EnterAddress=models.CharField(max_length=20)	
	SelectGender=models.CharField(max_length=20)
	EnterDesignation=models.CharField(max_length=20)
	Enterpassword=models.CharField(max_length=20,null=True)
	confirmpassword=models.CharField(max_length=20,null=True)
class Viewreports(models.Model):
	Entername=models.CharField(max_length=50)	
	Contactno=models.CharField(max_length=12,null=True)
class Addmarkinto(models.Model):
	SelectYear=models.IntegerField(null=True)
	SelectDepartment=models.CharField(max_length=20)
	SelectSemester=models.IntegerField(null=True)
	Enterentrollmentno=models.CharField(max_length=20)


class Subjectreport(models.Model):
	SelectYear=models.IntegerField(null=True)
	SelectDepartment=models.CharField(max_length=15)
	SelectSemester=models.IntegerField(null=True)
class Resultsview(models.Model):
	SelectYear=models.IntegerField(null=True)
	SelectDepartment=models.CharField(max_length=20)
	SelectSemester=models.IntegerField(null=True)
	Enterentrollmentno=models.CharField(max_length=20)
	Selectsubject=models.CharField(max_length=20)
	Marksbetween=models.IntegerField(null=True)
 






           # Create your models here.

# Create your models here.
