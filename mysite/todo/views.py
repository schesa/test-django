from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Todo
# Create your views here.
def hello(request):
    "hello view"
    return HttpResponse(content="Hello!")

def todo_list(request):
    todos = Todo.objects.all()
    context = { 'todos': todos }
    return render(request, 'todo/todo-list.html', context)