from django import forms
from results.models import Addstudents,Studentsreport,Addsubject,Addusers,Viewreports,Addmarkinto,Resultsview
class AddstudentsForm(forms.ModelForm):
	class Meta:
		model = Addstudents
		fields=('Entername','Emailid','Contactno','EnterAddress','SelectYear','SelectGender','Rollno','SelectDepartment','SelectSemester')
class StudentsreportForm(forms.ModelForm):
	class Meta:
		model=Studentsreport
		fields=('Entername','Rollno','SelectDepartment','SelectSemester')
class AddsubjectForm(forms.ModelForm):
	class Meta:
		model=Addsubject
		fields=('SelectYear','SelectDepartment','SelectSemester','Entersubjectcode','Entersubjectname')
class AddusersForm(forms.ModelForm):
	class Meta:
		model=Addusers
		fields=('Entername','Emailid','Contactno','EnterAddress','EnterDesignation','Enterpassword','confirmpassword')
class ViewreportsForm(forms.ModelForm):
	class Meta:
		model=Viewreports
		fields=('Entername','Contactno')
class AddmarkintoForm(forms.ModelForm):
	class Meta:
		model=Addmarkinto
		fields=('SelectYear','SelectDepartment','SelectSemester','Enterentrollmentno')
class ResultsviewForm(forms.ModelForm):
	class Meta:
		model=Resultsview
		fields=('SelectYear','SelectDepartment','SelectSemester','Enterentrollmentno','Selectsubject','Marksbetween')
