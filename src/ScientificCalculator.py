import math

class ScientificCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

    def power(self, base, exponent):
        return base ** exponent

    def square_root(self, x):
        if x < 0:
            return "Error: Square root of negative number is not allowed."
        return math.sqrt(x)

    def logarithm(self, x, base=10):
        if x <= 0:
            return "Error: Logarithm of non-positive number is not allowed."
        if base <= 0 or base == 1:
            return "Error: Logarithm base must be positive and not equal to one."
        return math.log(x, base)

    def sine(self, x):
        return math.sin(x)

    def cosine(self, x):
        return math.cos(x)

    def tangent(self, x):
        try:
            return math.tan(x)
        except ValueError:
            return "Error: Tangent of this angle is undefined."

    def degrees_to_radians(self, degrees):
        return math.radians(degrees)

    def radians_to_degrees(self, radians):
        return math.degrees(radians)