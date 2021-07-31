from django.db import models
from django.db.models.fields import CharField

class Fibonacci(models.Model):
    number = models.IntegerField(0)
    result = models.IntegerField(1)

    def fibonacci(self, number):
        if(number == 0 or number == 1):
            self.result = 1
        else:
            self.result = self.fibonacci(number-1)+self.fibonacci(number-2)
        self.save()
        
        return self.result

    def __str__(self) -> str:
        return "(%s, %s)" % (self.number,self.result)
