from django import forms
from .models import *
from django.contrib.auth.models import User  

meterial = [('Credit card','Credit card'),('Debit card','Debit card'),('Pass book','Pass book'),('Cheque book','Cheque book')]

class Client_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    Confirm_password = forms.CharField(widget=forms.PasswordInput())
    
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise forms.ValidationError("User Already Exist")  
        return username 
    def clean_password(self):
        value = self.cleaned_data['password']
        min_length = 8
        special = ['!','@','#','$','%','^','&','*','(',')','_','~','`','.','{','}','[',']',';',':','"','<',',','>','?','/','+','-','=']
        if len(value)<min_length:
            raise forms.ValidationError('Password must be at least 8 charecters.')
        if sum(i.isdigit() for i in value) < 1:
            raise forms.ValidationError('Password must contain at least 1 digit.')
        if not any(i.isupper() for i in value):
            raise forms.ValidationError('Password must contain at least 1 uppercase letter.')
        if not any(i.islower() for i in value):
            raise forms.ValidationError('Password must contain at least 1 lower letter.')
        if not any((i in special) for i in value):
            raise forms.ValidationError('Password must contain at least 1 special charecter.')
        return value
    def check_password(self):
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['Confirm_password']
        if (pass1!=pass2):
            raise forms.ValidationError('Passwords are not matching.')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class Update_form(forms.Form):
    
    branc =[('Aluva','Aluva'),('Edapally','Edapally'),('Vazhakala','Vazhakala'),('Kakkanad','Kakkanad'),('Mattancheri','Mattancheri')]
    choice = [('male','Male'),('female','Female'),('trans','Transgender')]
    account = [('Savings account','Savings account'),('Current account','Current account'),('Salary account','Salary account'),('Fixed deposit account','Fixed deposit account'),('Recurring deposit account','Recurring deposit account'),('NRI account','NRI account')]
    locatn = [('Trivandrum','Trivandrum'),('Kottayam','Kottayam'),('Ernakulam','Ernakukulam'),('Wayanad','Wayanad'),('Kozhikode','Kozhikode')]
    Name = forms.CharField()
    Date_of_birth = forms.DateField()
    Age = forms.IntegerField()
    Gender = forms.CharField(widget=forms.Select(choices=choice))
    Mobile_number = forms.IntegerField()
    Email_id = forms.EmailField()
    Address = forms.CharField()
    District = forms.CharField(widget=forms.Select(choices=locatn))
    Branch = forms.CharField(widget=forms.Select(choices=branc))
    Account_type = forms.CharField(widget=forms.Select(choices=account))
    Meterials_provide = forms.MultipleChoiceField(choices=meterial, widget=forms.CheckboxSelectMultiple)
    
