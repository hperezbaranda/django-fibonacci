from mySite.fibonacci.views import fibonacci
from django.db import models
from django.db.models.fields import CharField

class Fibonacci(models.Model):
    number = CharField(max_length=50)
    result = CharField(max_length=50)

    def __str__(self) -> str:
        return (self.number,self.result)

