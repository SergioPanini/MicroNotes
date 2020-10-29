from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import RegisterForm, CreateNote

from .models import Note

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

        
    return render(request, 'register.html', {'form':RegisterForm})

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
        
        return render(request, 'register.html', {'form':RegisterForm})
    return HttpResponse('you auntificater already')

def signout(request):
    logout(request)
    
    return HttpResponse('done')

def test(request):
    if request.user.is_authenticated:
        return HttpResponse(' aut aut')
    else:
        return HttpResponse('not not')

def create_note(request):
    if request.user.is_authenticated == False:
        return render(request, 'authorization_false.html')
    
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        if len(request.POST['text']) > 150:
            preview_text=text[:147] + '...'
        new_note = Note.objects.create(owner=request.user, title=title, text=text, preview_text=preview_text)
        new_note.save()
        return redirect('/notes/createnote')
    return render(request, 'create_note.html', {'form':CreateNote})

def show_notes(request):
    if request.user.is_authenticated == False:
        return render(request, 'authorization_false.html')
    
    notes = Note.objects.filter(owner=request.user).values()
    return render(request, "main.html", {"notes": notes})