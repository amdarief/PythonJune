# Simple calculator in python
import math
def add(x, y):

   return x + y

def subtract(x, y):

   return x - y

def multiply(x, y):

   return x * y

def divide(x, y):

   return x / y
def squart(x):
    return (math.sqrt(x))

print("Select any operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.square root")

choice = input("Enter choice(1/2/3/4/5):")

if choice == '5':
    num1 = int(input("Enter first number: "))
else:

 num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))

elif choice == '5':
       print(squart(num1))


else:
   print("Invalid input")
