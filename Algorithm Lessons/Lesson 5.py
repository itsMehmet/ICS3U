# Predict
"""
9
When both are strings it outputs 72
You can not mix data types (string and int)
"""

# Modify
def add(a, b):
  return a + b

try:
  a = float(input("Please input a number: "))
  b = float(input("Please input another number: "))
  print(add(a, b) * 2)
except:
  print("Please input a valid number")

# Modify 2
import math

def myPow(m, n):
  return m**n

try:
  m = float(input("Please input a number: "))
  n = float(input("Please input another number: "))
  print(myPow(m, n))
  print(math.pow(m, n))
except:
  print("Please input a valid number")
