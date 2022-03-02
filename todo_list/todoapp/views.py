from django.http import HttpResponse
from django.shortcuts import redirect, render
from todoapp.forms import TODOForm
from todoapp.models import TODO
import csv


def home(request):
    form=TODOForm()
    todos = TODO.objects.all()

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
    todo.delete()
    return redirect('home')


def csv_export_file(request):
    response=HttpResponse(content_type='text/csv')
    response={'Content-Disposition': 'attachment; filename="todo_list.csv"'}
    writer = csv.writer(response)
    writer.writerow(['title', 'description', 'date_time', 'created_on', 'updated_on'])
    todo = TODO.objects.all().values_list('title', 'description', 'date_time', 'created_on', 'updated_on')
    for todo_list in todo:
        writer.writerow(todo_list)
        
    return response
        
    

