from django.shortcuts import redirect, render
from todoapp.forms import TODOForm
from todoapp.models import TODO


def home(request):
    form=TODOForm()
    todos = TODO.objects.all()
    
    return render (request, 'home.html', context={'form' : form, 'todos':todos})

def user(request):
    return render (request, 'user.html')


def user_update(request):
    return render (request, 'userupdate.html')


def add_todo(request):
    form = TODOForm(request.POST)
    if form.is_valid:
        form.save()
        
        return redirect ("home")
    else:
        return render (request, 'home.html', context={'form' : form})