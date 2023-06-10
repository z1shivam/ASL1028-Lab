def value(c):
    map = {'i':1, 'v':5, 'x':10, 'l':50, 'c':100, 'd':500, 'm':1000}
    return map[c.lower()]

def roman2number(w):
    sum=0
    for i in range(len(w)-1, -1, -1):
        if i + 1 < len(w) and value(w[i]) < value(w[i+1]):
            sum -= value(w[i])
        else:
            sum += value(w[i])
    return sum

print(roman2number(input("Enter your roman number: ")))
