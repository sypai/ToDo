from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo


def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        todo = request.POST['todo']
        user_id = request.POST['user_id']

        _todo = Todo(todo=todo, title=title, user_id=user_id)
        _todo.save()

        Todos = Todo.objects.all()
        context = {
            'todos': Todos
        }

        return render(request, 'pages/dashboard.html', context)

