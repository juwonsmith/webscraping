from functools import reduce
y = []
def mean():
    s= int(input("enter the range of the numbers: "))
    for i in range (s):
        z = int(input("enter the corresponding numbers: "))
        y.append(z)
    x = reduce(lambda a,b:a+b, y)
    b = x /s
    print(b)

def fact(n):
    if n== 0:
        return 1
    return n * fact(n-1)
