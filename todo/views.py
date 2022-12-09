from django.shortcuts import render 

from .models import Todo
from django.contrib import messages

def index(request):
    todos = Todo.objects.filter(title_contains=request.GET.get('search,'))
    context = {
        'todos':todos
    }
    return render(request, 'todo/index.html', todos)



def views(request, id):
    return render(request, 'todo/index.html',{})

def edit(request, id):
    return render(request, 'todo/index.html',{})
    
def create(request):
    return render(request, 'todo/index.html',{})


def delete(request, id):
    return render(request, 'todo/index.html',{})