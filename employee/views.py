from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from .models import Employee
from django.shortcuts import redirect

# Create your views here.

def about(request, pk):
    try:
        # employee_details = Employee.objects.get(pk=pk)
        employee_details = get_object_or_404(Employee, pk=pk)
        print(employee_details)
        context = {'employee': employee_details}
        # return HttpResponse(f"Employee Name: {employee_details}")
        return render(request, 'about.html', context)
    except Exception as e:
        raise Http404("Employee not found")

def add_employee(request):
    if request.method == 'POST':
        print("request Received==>",request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        position = request.POST.get('position')
        department = request.POST.get('department')
        photo = request.FILES.get('photo')
        employee = Employee(
            name=name,
            email=email,
            phone=phone,
            position=position,
            department=department,
            photo=photo
        )
        employee.save()
        return redirect('/')  # Redirect to home after saving
    return HttpResponse('Invalid request', status=400)

def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.phone = request.POST.get('phone')
        employee.position = request.POST.get('position')
        employee.department = request.POST.get('department')
        if request.FILES.get('photo'):
            employee.photo = request.FILES.get('photo')
        employee.save()
        return redirect('/')
    context = {'employee': employee}
    return render(request, 'edit_employee.html', context)

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('/')
    return HttpResponse('Invalid request', status=400)