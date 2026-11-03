#q1
def greet_decorator(func):
    def wrapper():
        print("Greetings to everyone")
        func()

    return wrapper
@greet_decorator
def message():
    print("This is my first attempt at using decorator")
message()
#q2
def before_after(func):
    def wrapper():
        print("Function is starting....")
        func()
        print("Function has finished!")

    return wrapper
@before_after
def calculate():
    print("Calculating...")
calculate()
#q3
def count_calls(func):
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        func()
        print("Call count: ", count)

    return wrapper
@count_calls
def say_hi():
    print("Hi!")
say_hi()
say_hi()
say_hi()
#q4
def check_positive(func):
    def wrapper(n):
        if n > 0:
            func(n)
        else:
            print("Number must be positive")

    return wrapper
@check_positive
def display(n):
    print(n)
display(5)
display(-23)
display(7)
#q5
import time
import math

def measure_time(func):
    def wrapper(n):
        begin = time.time()
        func(n)
        end = time.time()
        print("Total time taken was ", end - begin, "s")
    return wrapper

@measure_time
def factorial(n):
    print("Factorial of", n, "is", math.factorial(n))

factorial(50)
#Q6
import math

def population_growth(initial, rate, time):
    def exponential_growth():
        return initial + math.exp(rate * time)

    population = exponential_growth()
    print(round(population))

population_growth(100, 1, 10)
#Q7
import time

def measure_time(func):
    def wrapper():
        begin = time.time()
        func()
        end = time.time()
        print("Total time taken was ", end - begin, "s")
    return wrapper

@measure_time
def population_growth():
    population = 100
    for i in range(1000000):
        population = population * 1.01

population_growth()
#Q8
def analyse_dna(sequence):
    def gc_content():
        gc = sequence.count('G') + sequence.count('C')
        return (gc / len(sequence)) * 100

    gc = gc_content()
    print("GC Content: ", gc, "%")

    if gc > 50:
        print("GC rich sequence")
    else:
        print("AT rich sequence")

analyse_dna("ATGCTGACT")
#q9
def log_function_call(func):
    def wrapper(dna):
        print("Running DNA analysis ....")
        result = func(dna)
        print("GC%: ", result)
        print("Analysis complete!")
        return result
    return wrapper

@log_function_call
def gc_percentage(dna):
    gc = dna.count("G") + dna.count("C")
    return (gc / len(dna)) * 100

gc_percentage("ATGCGCTGCAGTC")

