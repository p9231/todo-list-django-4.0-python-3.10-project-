from django.http import HttpResponse
from django.shortcuts import redirect, render
from todoapp.forms import TODOForm
from todoapp.models import TODO



def home(request):
    form=TODOForm()
    todos = TODO.objects.filter(isdelete=True)

    return render (request, 'home.html', context={'form' : form, 'todos':todos})

def user(request):
    return render (request, 'user.html')


def add_todo(request, id=0):
    if request.method=='GET':
        if id==0:
            form=TODOForm()
        else:
            todo=TODO.objects.get(pk=id)
            form=TODOForm(instance=todo)
        return render (request, 'home.html', context={'form' : form})
    else:
        if id==0: 
            form = TODOForm(request.POST)
        else:
            todo=TODO.objects.get(pk=id)
            form=TODOForm(request.POST, instance=todo)
        if form.is_valid:
            form.save()
            
    
            
            return redirect ("home")
        else:
            return render (request, 'home.html', context={'form' : form})


def delete_task(request, id):
    todo=TODO.objects.get(pk=id)
    todo.isdelete=False
    todo.save()
    return redirect('home')
        
    

