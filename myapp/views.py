from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.conf import settings
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages




# Create your views here.
def index(request):
    return render(request,'index.html')
def indcon(request):
    return render(request,'indcon.html')

def register(request):
    if request.method=='POST':
        form=Client_form(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            Confirm_password=form.cleaned_data['Confirm_password']
            object = Client()

            object.username=username
            object.password=password
            object.Confirm_password=Confirm_password
            if password != Confirm_password:
                print(form.errors)
            else:
                object.save()
                User.objects.create_user(username=username,password=password)

            return redirect('signin')
        else:
            print(form.errors)
            return render(request,'register.html',{'form':form})
    else:
        form = Client_form()
        return render(request,'register.html',{'form':form})

def form(request):
    if request.method=='POST':
        form=Update_form(request.POST)
        if form.is_valid():
            Name= form.cleaned_data['Name']
            Date_of_birth=form.cleaned_data['Date_of_birth']
            Age = form.cleaned_data['Age']
            Gender=form.cleaned_data['Gender']
            Mobile_number=form.cleaned_data['Mobile_number']
            Email_id=form.cleaned_data['Email_id']
            Address=form.cleaned_data['Address']
            District=form.cleaned_data['District']
            Branch=form.cleaned_data['Branch']
            Account_type=form.cleaned_data['Account_type']
            Meterials_provide=form.cleaned_data['Meterials_provide']

            LastInsertId = (Client.objects.last()).id
            t = Client.objects.get(id=LastInsertId)
        
            t.Name =Name
            t.Date_of_birth = Date_of_birth
            t.Age = Age
            t.Gender = Gender
            t.Mobile_number = Mobile_number
            t.Email_id = Email_id
            t.Address = Address
            t.District = District
            t.Branch = Branch
            t.Account_type = Account_type
            t.Meterials_provide = Meterials_provide
            t.save(update_fields=['Name','Date_of_birth','Age','Gender','Mobile_number','Email_id','Address','District','Branch','Account_type','Meterials_provide'])
            messages.success(request, "Application accepted")
            return redirect('home')
        else:
            print(form.errors)
            return render(request,'form.html',{'form':form})
    else:
        form = Update_form()
        return render(request,'form.html',{'form':form})

def signin(request):
    if request.method =='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            myusername = form.cleaned_data['username']
            mypassword = form.cleaned_data['password']
            if User.objects.filter(username=myusername).exists():
                myuser = User.objects.get(username=myusername)
                if myuser.check_password(mypassword):
                    login(request,myuser)
                    return redirect('indcon')
                else:
                    messages.error(request,'Invalid password')
                    return render(request,'signin.html',{'form':form})
            else:
                messages.error(request,'Invalid username')
                return render(request,'signin.html',{'form':form})
    else:
        form = LoginForm()
        return render(request,'signin.html',{'form':form})
    
def signout(request):
    logout(request)
    if 'count' in request.session:
        del request.session['count']
    messages.success(request, "You've successfully signed out.")
    return redirect('signin')