from django import forms
from results.models import Addstudents
class AddstudentsForm(forms.ModelForm):
	class Meta:
		model = Addstudents
		fields=('Entername','Emailid','Contactno','EnterAddress','SelectYear','SelectGender','Rollno','SelectDepartment','SelectSemester')