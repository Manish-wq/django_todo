from  django.http import HttpResponse
from django.shortcuts import render
from employee.models import Employee

def home(request):
    employees = Employee.objects.all()
    print(employees)
    context = {'employees': employees}
    return render(request, 'home.html', context)

    # return render(request, 'home.html')


def create_todo(request):
    return render(request, 'todo_home.html')