from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Fibonacci

def calculate(request,number):
    
    fibonacci = Fibonacci()
    fibonacci.number = number
    fibonacci.fibonacci(number)

    return HttpResponse("O fibonacci do numero %s es: %s" % (number,fibonacci.result))