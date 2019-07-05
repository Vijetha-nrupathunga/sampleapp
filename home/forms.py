from django import forms
from .models import student
class studentsearchform(forms.Form):
    q=forms.CharField(label='search bar',widget=forms.TextInput(attrs={'class':'form-control','max-length':'30','placeholder':'search'}))

class studentEditModelForm(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'#student_name,department for all fields
        #fields=('department',) for only department
        widgets={
            'student_name':forms.TextInput(attrs={'class':'form-control',
            'placeholder':'student name'}),
            'department':forms.Select(attrs={'class':'custom-select'})}

class studentcreateform(forms.Form):
    student_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        'class':'form-control','maxlength':'50','placeholder':'student name'}))
    dept=(('ise','information science'),('mh','mech'),('cv','civil'))
    department=forms.CharField(label='',widget=forms.Select(attrs={'class':'form-control'},choices=dept))