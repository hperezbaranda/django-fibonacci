from django.http.response import HttpResponse
from django.shortcuts import render

def calculate(request,number):
    return HttpResponse({fibonacci(number)})

def fibonacci(number):
    if(number == 0 or number == 1):
        return 1
    else:
        return fibonacci(number-1)+fibonacci(number-2)