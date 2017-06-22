from pip._vendor.distlib.compat import raw_input

from ex12 import weight, height, age

print ("How old are you?",
age = raw_input())
print ("How tall are you?",
height = raw_input())
print ("How much do you weigh?",
weight = raw_input())

print("So, you're %r old, %r tall and %r heavy." % ( age, height, weight))