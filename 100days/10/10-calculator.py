from art import logo
import os

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
     while(b == 0):
            b = float(input("Second nummber can't be 0. Please type number expect 0: "))
     return a / b




print(logo)
flag = 0
while True:
    if(flag == 0):
        a = float(input("What's the first number?: "))
        print("""+
-
*
/""")
    op = input("Pick an operation: ")
    b = float(input("What's the next number?: "))
    res = None
    if(op == "+"):
        res = add(a,b)
    elif(op == "-"):
        res = subtract(a,b)
    elif(op == "*"):
        res = multiply(a,b)
    elif(op == "/"):
        res = divide(a,b)
    print(f"{a} {op} {b} = {res}")
    x = input("Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation:")
    if(x == 'n'):
        os.system('clear')
        flag = 0
    elif(x == 'y'):
        flag = 1
        a = res
    else:
        print("You entered wrong input. Program will exit.")
        break
        
