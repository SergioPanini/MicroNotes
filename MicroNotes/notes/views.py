from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import register_form

def main_page(request):
    return HttpResponse('main page')

def register_user(request):

    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username=name, password=password)
            user.save()
            return HttpResponse('done')
        
        except:
            return HttpResponse('you registers already')

        
    return render(request, 'register.html', {'form':register_form})

def signin(request):
    if not request.user.is_authenticated:
        
        if request.method == 'POST':
            
            name = request.POST['name']
            password = request.POST['password']

            user = authenticate(username=name, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('your signin')
                
            return HttpResponse('not user find, go to /register?')
        
        return render(request, 'register.html', {'form':register_form})
    return HttpResponse('you auntificater already')

def signout(request):
    logout(request)
    
    return HttpResponse('done')

def test(request):
    if request.user.is_authenticated:
        return HttpResponse(' aut aut')
    else:
        return HttpResponse('not not')