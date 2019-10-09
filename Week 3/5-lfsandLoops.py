# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
# ## ITNPBD2: Representing and Manipulating Data
# ## University of Stirling
# ## Dr. Kevin Swingler
#%% [markdown]
# # Python conditional statements and loops
# - How to run code only if a condition is true
# - How to do the same thing over and over
#%% [markdown]
# # If Statements
# - Syntax is<br>
# `if condition:
#     do something if condition is true
# else:
#     optional thing to do otherwise`<br>
# # Checking if two things are equal: use `==` double equals

#%%
if 1+1 == 2:
    print("Yes it is")
else:
    print("No it is not")

#%% [markdown]
# # Boolean values `True` and `False`

#%%
if True:
    print("True!")

if False:
    print("False")


#%%
res = 1 == 2
print(res)

#%% [markdown]
# ## Other comparison operators:
# 
# `>`,`<`,`!=`,`>=`,`<=`

#%%
if 4 < 5:
    print("Yes, 4 is less than 5")

#%% [markdown]
# ## Short hand on one line

#%%
a, b = 8, 7
print("a is bigger") if a > b else print("b is bigger")

#%% [markdown]
# ## More complex logic
# - `and`
# - `or`
# - `not`

#%%
a, b, c=1, 2, 3

if a > b or a < c:
    print("Yes")
    
# Be clear about the order of evaluation using brackets

#%% [markdown]
# ## Operator precedence
# Take something like:
# - `if a > b or a > c and b <d` ...
# - Which parts are evaluated first, and how does the result change depending on the order?
# 
# ### Python operator precedence is:
# 1. `not`
# 2. `and`
# 3. `or`
# 

#%%
print(True and False)
print(False or True)
print(not False or True)
print(not (False or True))
print(True or False and False)
print((True or False) and False)

#%% [markdown]
# ## When to use `==` and when to use `is`
# - `==` is for comparing values
# - `is` is for comparing identity - if two objects have the same id

#%%
b = [1, 2, 3000]
c = [1, 2, 3000]

print("id of b:", id(b), "id of c:", id(c))

if c is b:
    print("c is b")
else:
    print("c is not b")
        
if c == b:
    print("c == b")
else:
    print("c does not == b")


a = None
if a is None:
    print("a is None")

#%% [markdown]
# ## With sets, tuples and dicts

#%%
a = set((1, 2, 3000))
b = set((3000, 1, 2))

print(a == b)
# Sets are not ordered


#%%
a = (1, 2, 3000)
b = (3000, 1, 2)

print(a == b)
# Tuples are orderd


#%%
b = [1, 2, 3000]
c = [3000, 1, 2]

print(a == b)
# Lists are ordered


#%%
a = {'x':1, 'y':2}
b = {'y':2, 'x':1}

print(a == b)
# Dicts are not ordered

#%% [markdown]
# ## `if ... elif` chains

#%%
mark=75

if mark < 50:
    print("Fail")
elif mark < 60:
    print("Pass")
elif mark < 70:
    print("Merit")
else:
    print("Distinction")
    

#%% [markdown]
# ## Often it is better to use a dict instead of a lot of `if` ... `elif`

#%%
marks={50:'Fail', 60:'Pass', 70:'Merit', 101:'Distinction'}
mark=61
for m,g in marks.items():
    if mark < m:
        print(g)
        break

#%% [markdown]
# ## Better to check if values exist before you process them though:

#%%
if 'Pass' in marks.values():
    print("Pass is a grade")
    
if 'super' not in marks.values():
    print("super is not a grade")

#%% [markdown]
#  ## We can get quite clever with this
#  - Here we define a dictionary of functions
#  - We then call the appropriate function based on its key
#  - Obviously this example is trivial, but the concept is very useful and better than lots of `if` statements

#%%
def func_a():
    print('a')
    
def func_b():
    print('b')
    
def func_c():
    print('c')
    
actions = {'a':func_a, 'b':func_b, 'c':func_c}
act = 'a'
actions[act]()

#%% [markdown]
# # While loops

#%%
count=1
while count < 10:
    print(count)
    count = count+1

#%% [markdown]
# # User Input

#%%
# a=''
# while a != 'quit':
#     a=input("Type a number or 'quit' to end")
#     if(a != 'quit'):
#         a=float(a)
#         print(f"{a} squared is {a*a}")
# print("Done")


#%%
import numpy
import math

c = ''
while c != 'end':
    c = input("Get square root of: ")
    if (c != 'end'):
        temp = math.sqrt(float(c))
        print(f"sqrt({c}) = {temp}")
print("Sayonara")


