from django.shortcuts import render, redirect
from main.forms import Registerform, Loginform
from django .contrib.auth import login, authenticate, logout
from main.models import User

def menu(request):
    return render(request,'menu/menu.html')

def admin_view(request):
    cont=User.objects.all()
    context={
        'context':cont,
    }
    return render(request,'users/admin.html',context)

def employer_view(request):
    return render(request,'users/employer.html')

def executor_view(request):
    return render(request,'users/executor.html')

def register_view(request):
    msg= None
    if request.method =='POST':
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Вы зарегистрировались'
            return redirect('login')
        else:
            msg = 'Недопустимые данные'
    else:
        form = Registerform()
    return render(request, 'registration/register.html',{'form':form, 'msg':msg})

def login_view(request):
    form = Loginform(request.POST or None)
    msg= None
    if request.method =='POST':
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None and user.Metric_name=='is_admin':
                login(request,user)
                return redirect('admin')
            elif user is not None and user.Metric_name=='is_employer':
                login(request,user)
                return redirect('employer')
            elif user is not None and user.Metric_name=='is_executor':
                login(request,user)
                return redirect('executor')
            else:
                msg = 'Аккаунт не существует'
        else:
            msg = 'Некоректные данные'
    return render(request, 'registration/login.html',{'form':form, 'msg':msg})

def UserLoggedIn(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    return username

def logout_view(request):
    username = UserLoggedIn(request)
    if username != None:
        logout(request)
        return redirect('login')