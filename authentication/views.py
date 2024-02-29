from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    return HttpResponse("Home")


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass1']
        password2 = request.POST['pass2']

        user = f'{fname[:3]}_{lname[:3]}_{fname[-3:]}_{lname[-3:]}'

        user_create = User.objects.create_user(username=user, email=email, password=password)

        user_create.first_name = fname
        user_create.last_name = lname
        user_create.save()

        messages.success(request, 'Registro realizado com sucesso')
        return redirect('signin')

    else:
        return render(request, 'authentication/register.html')


def signin(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass1']

        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request=request, user=user)
        else:
            messages.error(request, 'Usuário ou senha incorreta')
            return render(request, 'authentication/login.html')
        
    return render(request, 'authentication/login.html')

def logout(request):
      
    pass
