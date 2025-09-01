from  django.http import HttpResponse
from django.shortcuts import render, redirect
from employee.models import Employee, Todo


def home(request):
    employees = Employee.objects.all()
    print(employees)
    context = {'employees': employees}
    return render(request, 'home.html', context)

    # return render(request, 'home.html')


def get_todo(request):
    todo_list = Todo.objects.filter(is_completed=False).order_by('-updated_at')
    completed_todo = Todo.objects.filter(is_completed=True)
    # print(todo_list)
    context = {'todo_list': todo_list, 'completed_todo': completed_todo}
    return render(request, 'todo_home.html', context)

def add_todo(request):
    if request.method == 'POST':
        print("Request Received==>", request.POST)
        task = request.POST.get('task')
        print("task===>",task)
        # todo = Todo(
        #     task=task,
        # )
        todo = Todo.objects.create(task=task)
        todo.save()
    return redirect('get_todo')

def mark_as_done(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_completed = True
    todo.save()
    return redirect('get_todo')

def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        todo = Todo.objects.get(pk=pk)
        todo.task  = request.POST.get('task')
        todo.save()
        return redirect('get_todo')  
    context = {'todo': todo}
    return render(request, 'update_todo.html', context)