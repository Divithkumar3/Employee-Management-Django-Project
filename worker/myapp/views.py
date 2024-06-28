from django.shortcuts import render,redirect
from.models import *
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from .models import Employee
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

def Signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        college=request.POST['college']
        age=request.POST['age']
        if password1==password2:
            try:
                user=User.objects.create_user(username=username,password=password1,college=college,age=age)
            except Exception as e:
                raise ValidationError('User Name Already Exists')
        else:
            raise ValidationError('Password1 and Password2 are not Match')
        return redirect('main')
    return render(request,'signup.html')  


def Login(request):
    if request.method=='POST':
       username=request.POST['username']
       password=request.POST['password']
       user=authenticate(username=username,password=password)
       if user:
           login(request,user)
           return redirect('main')
    return render(request,'login.html')

def Logout(request):
    logout(request)
    return render(request,'login.html')

@login_required(login_url='/Login')
def main(request):
    return render(request,'main.html')

def show(request):
     data=Employee.objects.all()
     return render(request,'show.html',{'data':data})
def delete(request,id):
    obj=Employee.objects.get(id=id)
    obj.delete()
    return redirect('show') 
 
def main(request):
    return render(request,'main.html')

def query(request):
    return render(request,'query.html')
 
def cse(request):
     data=Employee.objects.filter(department='cse')
     return render(request,'cse.html',{'data':data})
 
def CIVIL(request):
     data=Employee.objects.filter(department='CIVIL')
     return render(request,'CIVIL.html',{'data':data})
 
def history(request):
    data=Employee.objects.all()
    return render(request,'history.html',{data:'data'})

def login(request):
    return render(request,'login.html') 
    

def signup(request):
    return render(request,'signup.html')

def save(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        Phone_number = request.POST.get('Phone_number')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        department = request.POST.get('department')
        position = request.POST.get('position')
        image = request.FILES.get('image')
        date_hired = request.POST.get('datehired')
        salary = request.POST.get('salary')
        is_active = request.POST.get('isactive')

        employee = Employee(
            first_name=first_name,
            last_name=last_name,
            email=email,
            Phone_number=Phone_number,
            address=address,
            date_of_birth=date_of_birth,
            department=department,
            position=position,
            image=image,
            date_hired=date_hired,
            salary=salary,
            is_active=is_active
        )
        employee.save()
        return redirect('history') 
    else:
        return render(request, 'save.html')
    
def view(request):
    first_name = request.GET.get('first_name')  # Assuming you pass employee_code via query parameter
    
    try:
        employee = Employee.objects.filter(first_name=first_name).first()
    except Employee.DoesNotExist:
        return HttpResponseNotFound('<h1>Employee not found</h1>')
    
    return render(request, 'view.html', {'employee': employee})






    
        

       
