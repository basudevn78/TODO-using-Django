from django.shortcuts import render,redirect
from todo.models import Todos

# Create your views here.

def home(request):
    if request.method == 'POST':
        title = request.POST["title"]
        Todos.objects.create(title = title)
        return redirect('home_page')
    
    todo_data = Todos.objects.all()
    return render(request, 'todo/home.html', {'context': todo_data})

def display_todo_by_id(request,id):
    data = Todos.objects.get(id = id)
    print(data)
    return render(request,'todo/display_todo.html',{'context':data})

def toggle_status(request,id):
    data = Todos.objects.get(id = id)
    data.is_completed = not data.is_completed
    data.save()

    return redirect('home_page')

def delete_todo_by_id(request,id):
    Todos.objects.get(id=id).delete()
    return redirect('home_page')

def update_todo_by_id(request,id):
    data = Todos.objects.get(id = id)
    if request.method=='POST':
        title = request.POST["title"]
        data.title = title
        data.save()
        return redirect('home_page')
    return render(request,'todo/update.html',{"context":data})