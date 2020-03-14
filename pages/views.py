from django.shortcuts import render
from todos.models import Todo
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def dashboard(request):

    if request.method == 'POST':
        # print(request.POST['todo-done'])
        todo_id = request.POST['todo-done']
        obj = Todo.objects.get(pk=todo_id)
        obj.is_done = True
        obj.save()
        # print(Todo.objects.get(pk=todo_id).is_done)

    x = datetime.now()
    day = x.strftime("%d")
    month = x.strftime("%b")
    year = x.strftime("%Y")

    Todos = Todo.objects.all()
    context = {
        'todos': Todos,
        'day': day,
        'month': month,
        'year': year
    }
    print(context)
    return render(request, 'pages/dashboard.html', context)
