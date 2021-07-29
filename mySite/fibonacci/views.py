from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Fibonacci

def calculate(request,number):
    
    fibonacci = Fibonacci()
    fibonacci.number = number
    result = fibonacci.fibonacci(number)
    fibonacci.result = result
    fibonacci.save()

    return HttpResponse(result)