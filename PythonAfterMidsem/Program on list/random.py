import time

def generate_random_integer(lower_limit, upper_limit):
    seed = int(time.time())
    
    range_size = upper_limit - lower_limit + 1
    
    pseudo_random = ((seed * 1103515245 + 12345) // 65536) % 32768
    
    random_integer = lower_limit + (pseudo_random % range_size)
    
    return random_integer

lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

random_integer = generate_random_integer(lower_limit, upper_limit)
print("Random Integer:", random_integer)
