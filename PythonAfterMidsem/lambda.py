#performing the task using simple function

def factorial(num):
    result = 0
    for i in range (1, num):
        result*=i
    return result
print(factorial(5))