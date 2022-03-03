from django.http import HttpResponse
from django.shortcuts import redirect, render
from todoapp.forms import TODOForm
from todoapp.models import TODO



def home(request):
    form=TODOForm()
    todos = TODO.objects.filter(isdelete=True)

    return render (request, 'home.html', context={'form' : form, 'todos':todos})


def add_todo(request):
    form = TODOForm(request.POST)
    if form.is_valid:
        form.save()
        return redirect ("home")
    else:
        return render (request, 'home.html', context={'form' : form})
    
    
def update_task(request, id):
    todo=TODO.objects.get(id=id)
    form=TODOForm(instance=todo)
    if request.method=='POST':
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
        
    

