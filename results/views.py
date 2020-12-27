from django.shortcuts import render,redirect
from django.http import HttpResponse
from results.forms import AddstudentsForm,StudentsreportForm,AddsubjectForm,AddusersForm,ViewreportsForm,AddmarkintoForm,ResultsviewForm
from results.models import Login,Subjectreport,Addstudents,Studentsreport,Addsubject,Addusers,Viewreports,Addmarkinto,Resultsview
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
		Entername = request.POST["Entername"]
		Emailid = request.POST["Emailid"]
		Contactno = request.POST["Contactno"]
		EnterAddress = request.POST["EnterAddress"]
		SelectYear = request.POST["SelectYear"]
		SelectGender = request.POST["SelectGender"]
		Rollno = request.POST["Rollno"]
		SelectDepartment = request.POST["SelectDepartment"]
		SelectSemester = request.POST["SelectSemester"]
		instance = Addstudents(Entername=Entername, Emailid=Emailid,Contactno=Contactno, EnterAddress=EnterAddress, SelectYear=SelectYear, SelectGender=SelectGender, Rollno=Rollno, SelectDepartment=SelectDepartment, SelectSemester=SelectSemester)
		instance.save()
		return HttpResponse('Success')
		
	else:
		form=AddstudentsForm()
	return render(request,'results/addstudent.html',{'form':form})
def update(request,Rollno):
	data=Addstudents.objects.get(Rollno=Rollno)
	if request.method=="POST":
		Entername = request.POST["Entername"]
		Emailid = request.POST["Emailid"]
		Contactno = request.POST["Contactno"]
		EnterAddress = request.POST["EnterAddress"]
		SelectYear = request.POST["SelectYear"]
		SelectGender = request.POST["SelectGender"]
		Rollno = request.POST["Rollno"]
		SelectDepartment = request.POST["SelectDepartment"]
		SelectSemester = request.POST["SelectSemester"]
		data.Entername=Entername
		data.Emailid=Emailid
		data.Contactno=Contactno
		data.EnterAddress=EnterAddress
		data.SelectYear=SelectYear
		data.SelectGender=SelectGender
		data.Rollno=Rollno
		data.SelectDepartment=SelectDepartment
		data.SelectSemester=SelectSemester
		data.save()
		return redirect('/studentreport')

	return render(request,'results/update.html',{'mydata':data})

def delete(request,Entername):
	data=Addstudents.objects.get(Entername=Entername)
	data.delete()
	return redirect('/studentreport')

def studentreport(request):
	if request.method=="POST":
		rollno=request.POST["rollno"]
		obj=Addstudents.objects.filter(Rollno=rollno)
		print(obj)
		return render(request,'results/studentreport.html',{'info':obj})
		data=Addstudents.objects.all()
		return render(request,'results/studentreport.html',{'info':data})
		form=StudentsreportForm(request.POST)
		if form.is_valid():
			form.save()
		context={'form':form}
		return render(request,'results/studentreport.html',context)


def addsubjects(request):
	form=AddsubjectForm(request.POST)
	if form.is_valid():
		form.save()
	context={'form':form}
	return render(request,'results/addsubjects.html',context)
def subjectsreport(request):
	if request.method=="POST":
		SelectYear = request.POST["SelectYear"]
		SelectDepartment=request.POST['SelectDepartment']
		SelectSemester=request.POST['SelectSemester']
		data=Subjectreport.objects.create(SelectYear=SelectYear,SelectDepartment=SelectDepartment,SelectSemester=SelectSemester)
	return render(request,'results/subjectsreport.html')
def adduser(request):
	form=AddusersForm(request.POST)
	if form.is_valid():
		form.save()
	context={'form':form}
	return render(request,'results/adduser.html',context)
def userreport(request):
	if request.method == "POST":
		Entername = request.POST["Entername"]
		Contactno = request.POST["Contactno"]
		instance = Viewreports(Entername=Entername,Contactno=Contactno)
		instance.save()
		return HttpResponse('Success')
	else:
		form=ViewreportsForm()
	return render(request,'results/userreport.html')
def addmarks(request):
	form=AddmarkintoForm(request.POST)
	if form.is_valid():
		form.save()
	context={'form':form}
	return render(request,'results/addmarks.html',context)
def resultsanalysis(request):
	form=ResultsviewForm(request.POST)
	if form.is_valid():
		form.save()
	context={'form':form}	
	return render(request,'results/resultsanalysis.html')
	
