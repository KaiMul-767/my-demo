
def calculater(x,o,y):
    if o == "+":
        return (f" {x} + {y} = {x+y}")
    elif 0 == "-":
        return (f" {x} - {y} = {x-y}")
    elif o == "*":
        return (f" {x} * {y} = {x*y}")
    elif o == "/":
        return (f" {x} / {y} = {x/y}")
x = int(input("enter the first number :"))
o = input("enter the oparator")
y = int(input("enter the sedond number :"))
z = calculater(x,o,y)
print(z)