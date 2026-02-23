a = int(input())
b = int(input())
result = 0
def add(x,y):
    return (x+y)
def subtract(x,y):
    return (x-y)
def multi(x,y):
    return (x*y)
def divi(x,y):
    return (x/y)
print(f"{a}+{b} = {add(a,b)}")
print(f"{a}-{b} = {subtract(a,b)}")
print(f"{a}*{b} = {multi(a,b)}")
print(f"{a}/{b} = {divi(a,b)}")