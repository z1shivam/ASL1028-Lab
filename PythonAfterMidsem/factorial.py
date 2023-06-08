# def factorial(num):
#     for i in range(num, 1):
#         result = num*(num-1)
#     return result

# num = int(input("Enter a number: "))
# print(factorial(num))

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

print(factorial(5))