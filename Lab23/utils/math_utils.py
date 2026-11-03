def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
        return a / b
def remainder(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot find remainder with zero")
        return a % b