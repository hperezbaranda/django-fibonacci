from django.db import models
from django.db.models.fields import CharField

class Fibonacci(models.Model):
    number = models.CharField(max_length=50)
    result = models.CharField(max_length=50)

    def fibonacci(self, number):
        if(number == 0 or number == 1):
            return 1
        else:
            return self.fibonacci(number-1)+self.fibonacci(number-2)

    def __str__(self) -> str:
        return self.number
