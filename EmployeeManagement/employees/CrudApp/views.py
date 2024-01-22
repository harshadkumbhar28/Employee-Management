from django.shortcuts import render, redirect
from .models import Employees


# Create your views here.

def INDEX(request):
    emp = Employees.objects.all()
    context = {
        "emp": emp
    }
    return render(request, 'index.html', context)


def ADD(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        emp = Employees(
            Name=name,
            Email=email,
            Address=address,
            Phone_Number=phone
        )
        emp.save()
        return redirect('home')

    return render(request, 'index.html')


def Edit(request):
    emp = Employees.objects.all()
    context = {
        "emp": emp
    }
    return render(request, 'index.html', context)


def Update(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        emp = Employees(
            id=id,
            Name=name,
            Email=email,
            Address=address,
            Phone_Number=phone
        )

        emp.save()
        return redirect("home")

    return render(request, 'index.html')


def Delete(request, id):
    emp = Employees.objects.filter(id=id)
    emp.delete()
    context = {
        "emp":emp
    }
    return redirect("home")
