from django.shortcuts import render
#from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request, "input.html")

@csrf_exempt 
def addition(request):
    if request.method == "POST":
        num1 = request.POST['num1']
        num2 = request.POST['num2']

        if num1.isdigit() and num2.isdigit():
            a = int(num1)
            b = int(num2)
            res = a + b

            return render(request, "result.html", {"result": res})
        else:
            res = "Only digits are allowed"
            return render(request, "result.html", {"result": res})


@csrf_exempt 
def substraction(request):
    if request.method == "POST":
        num1 = request.POST['num1']
        num2 = request.POST['num2']

        if num1.isdigit() and num2.isdigit():
            a = int(num1)
            b = int(num2)
            res = a - b

            return render(request, "result.html", {"result": res})
        else:
            res = "Only digits are allowed"
            return render(request, "result.html", {"result": res})

@csrf_exempt
def multiplication(request):

    if request.method == "POST":
        num1 = request.POST['num1']
        num2 = request.POST['num2']

        if num1.isdigit() and num2.isdigit():
            a = int(num1)
            b = int(num2)
            res = a * b

            return render(request, "result.html", {"result": res})
        else:
            res = "Only digits are allowed"
            return render(request, "result.html", {"result": res})


@csrf_exempt
def division(request):

    if request.method == "POST":
        num1 = request.POST['num1']
        num2 = request.POST['num2']

        if num1.isdigit() and num2.isdigit():
            a = int(num1)
            b = int(num2)
            res = a / b

            return render(request, "result.html", {"result": res})
        else:
            res = "Only digits are allowed"
            return render(request, "result.html", {"result": res})