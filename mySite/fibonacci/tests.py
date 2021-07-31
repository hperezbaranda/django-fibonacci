from django.test import TestCase
from .models import Fibonacci

class FibonacciTestCase(TestCase):

    def setUp(self) -> None:
        self.fibonacci = Fibonacci(number=0)

    def test_calcFibo5(self):
        self.assertEqual(self.fibonacci.fibonacci(5), 8)

    def test_calcErrorFibo10(self):
        self.assertNotEqual(self.fibonacci.fibonacci(10), 8)