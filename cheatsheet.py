#variables
x = 1
x = x + 2
print(X)

#Strings
x = "abc"
y = "de"
z = X + y
z

z = z [1:3]
z

#Functions
def f(X):
    y = x+2
    return y
f(5)

#If Statements
x = 2
if x+1 == 3:
    print (x)

#Loops
for i in range(1,100):
    if i%2 == 0:
        print(i)

#Importing
import math
math.sqrt(144)

import time
time.ctime()

#Arrays
a = [1,2,3,4]
a
a.append(8)
a

#Looping Through Arrays In 2 Different Ways
#Old Way
for i in range(len(a)):
    print(a[i])

#New Way
for x in a:
    print(x)

#Multiple Functions
def f(x):
    return 2*X

def g(y):
    return 1+y

g(f(4))
f(g(4))

#Delete From Array
a = [1,2,3,4,5]
a.pop()
a

#and/or
x = 5
y = 3
if x > 2 and y < 9:
    print(2)
if x > 2 or y < 10:
    print(2)

#Get Element From String Or Array
s = "how are you"
print(s[5])
a = [2,4,6,8]
a[3]

# Get First And Last Element From String Or Array
a = [2,4,6,8]
print(a[-1])
a[0]

# Change Directory And Get Current Directory
import os
os.getcwd()[:]

os.chdir("/")

# Data Types: String(s), Float(f), Bool(b)
s = "abc"
f = 1.0
b = True
n = None

# Data Casting
f = float("1")
s = str(1)

# String Operations
s = "abc"
S1 = s.upper()
S2 = s.capitalize()
s[0] = "d" #Not Possible

# Tuples
x = (1,2,3)
y = [1,2,3]
y[0] = 4
x[0] = 4

# Sets
s = set([1,2,3])
s.add(4)
s
s.add(3)
s

# F-Strings
name = "Enigma"
# Instead Of This
"my name is" + name + "nice to meet you."

# Use This
f"my name is {name} nice to meet you"

# In Opperator
a = [1,2,3,4]
for x in a:
    print(x)

# List Comprehension
a = [1,2,3]
[3*x for x in a]

# Exponents And Division
5**2
5/2
5//2

# Iterator Through Dictionary
d = {1:5,2:15}
for k in d:
    print(k)

for k in d.keys():
    print(x)

for k in d.values():
    print(x)

# Data Science