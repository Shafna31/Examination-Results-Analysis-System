from django.shortcuts import render,redirect
from django.http import HttpResponse
from results.forms import AddstudentsForm
from results.models import Login,Subjectreport,Addstudents

def home(request):
	return render(request,'results/home.html')
def login(request):
	
	if request.method=="POST":
	       userid=request.POST['userid']
	       pwd=request.POST['pwd']
	       data=Login.objects.create(userid=userid,pwd=pwd)
	      
	return render(request,"results/login.html") 

# Create your views here
def addstudent(request):
	if request.method == "POST":
		form=AddstudentsForm(request.Addstudents.Entername,request.Addstudents.Emailid,request.Addstudents.Contactno,request.Addstudents.EnterAddress,request.Addstudents.SelectYear,request.Addstudents.SelectGender,request.Addstudents.Rollno,request.Addstudents.SelectDepartment,request.Addstudents.SelectSemester)
		if form.is_valid():
				form.save()
				return HttpResponse('Success')		
	else:
		form=AddstudentsForm()
	return render(request,'results/addstudent.html',{'form':form})

		
def studentreport(request):
	return render(request,'results/studentreport.html')
def addsubjects(request):
	return render(request,'results/addsubjects.html')
def subjectsreport(request):
	if request.method=="POST":
		EnterName=request.POST['EnterName']
		Rollno=request.POST['Rollno']
		SelectDepartment=request.POST['SelectDepartment']
		SelectSemester=request.POST['SelectSemester']
		data=Subjectreport.objects.create(EnterName=EnterName,Rollno=Rollno,SelectDepartment=SelectDepartment,SelectSemester=SelectSemester)
	return render(request,'results/subjectsreport.html')
def adduser(request):
	return render(request,'results/adduser.html')
def userreport(request):
	return render(request,'results/userreport.html')
def addmarks(request):
	return render(request,'results/addmarks.html')
def resultsanalysis(request):
	return render(request,'results/resultsanalysis.html')
	
