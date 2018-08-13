from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Todo

# Create your views here.

def index(request):
    todo_list = Todo.objects.all()
    context = {'todos':todo_list}
    return render(request, 'todolist/index.html', context)

def remove(request, pk):
    target_todo = get_object_or_404(Todo, pk=pk)
    target_todo.delete()
    return HttpResponseRedirect(reverse('todos:index'))

def done(request, pk):
    target_todo = get_object_or_404(Todo, pk=pk)
    target_todo.completed = (not target_todo.completed)
    target_todo.save()
    return HttpResponseRedirect(reverse('todos:index'))

def add(request):
    if request.method == "POST":
        text = request.POST['todo_text']
        new_todo = Todo(todo_text = text)
        new_todo.save()
    return HttpResponseRedirect(reverse('todos:index'))
