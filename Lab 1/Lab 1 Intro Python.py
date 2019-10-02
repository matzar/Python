# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
# # ITNPBD2 Practical Lab 1. Introduction to Python
# 
# - Running code and printing results
# - Variables
# - Lists, sets and dictionaries
#%% [markdown]
# ## First Python Code
# In the box below, write the Python code to print "Hello World" to the screen, and run it (Ctrl + Enter or with the Run button)

#%%
# Type your answer below in this box
print("Hello world")
print("Hello world")

#%% [markdown]
# ## Variables
# Next, declare some variables and give them values. Experiment with different data types and the operators +,-,* and /. What happens if you add two strings, or multiply a string by a number?
# 
# Use `str()` and `int()` or `float()` to change the data types - how do the results change? Use `type()` to see the data types of your results.

#%%
# Type your answer below in this box
a = float(1)
print(a)

#%% [markdown]
# ## Immutable Variables and `id()`
# Define a numeric variable and use `id()` to print its ID. Now add 1 to the value of that variable and look at its ID again. What has happened to the ID? It has changed because the variable is immutable - its value cannot change. A new variable has been created in its place.
# 
# Now try setting a variable to have some numeric value and print its ID. On the next line, assign the SAME value again and print its ID again. Try this first of all by assigning the value 10 to the variable twice, then try again with 10.5 - what difference do you see? Look online to try and find the reason why this happens.

#%%
# Type your answer below in this box
a = int(2)
print(id(a))

#%% [markdown]
# # f-strings
# f-string syntax is `f"some text {variable} more text"`. Assign values to variables `a` and `b` and print "a plus b equals a+b" but replace the variables with the appropriate expression!

#%%
# Type your answer below in this box
name = "Mateusz"
surname = "Zaremba"
age = int(28)

val = f"Hi! My name is {name} {surname}. I'm {age} y/o."
print(val)

# print date and time
import datetime
today = datetime.datetime.today()
print(f"day: {today:%d}")   # 26
print(f"Day: {today:%D}")   # 09/26/19
print(f"month: {today:%b}") # Sep
print(f"Month: {today:%B}") # September
print(f"year: {today:%y}")  # 19
print(f"year: {today:%Y}", end = '')  # 2019

print("")

print(f"{today:%b %d, %y}") # Sep 26, 19
print(f"{today:%B %d, %Y}") # September 26, 2019
print(f"{today:%D}")        # 09/26/19

# format()
print("")
print("{} is my name.".format("Mateusz"))
str = "this lab teaches {}"
str.format("Python")

print("This {} is written in {pth} in {str}"
      .format("lab", pth = "Python", str = "Stirling"))

#%% [markdown]
# # Lists
# Create a list with the integers from 5 to 10 in it. Do this two different ways, once by hand and one using `range()`. Print them both. Do they look the same? If not - have you remembered to use `list()` to change the second one from being a range object to a list?

#%%
# Type your answer below in this box
list = [5, 6, 7, 8, 9, 10]

for i in list:
    print(i, end = '')

print("")

range_list = range(5,11)
for i in range_list:
    print(i, end = '')

#%% [markdown]
# Now you have your two lists, produce each of the following new lists
# - Concatenate the two lists to produce one: `[5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10]`
# - Add both together to produce `[10, 12, 14, 16, 18, 20]`
# - The first three elements of the first list: `[5,6,7]`
# - The first list backwards: `[10, 9, 8, 7, 6, 5]`
# - Only the even numbers from the first list: `[]`
# - A two dimensional list where the element at i,j is `list1[i] * list2[j]`:
# `[[25, 30, 35, 40, 45, 50],
#   [30, 36, 42, 48, 54, 60],
#   [35, 42, 49, 56, 63, 70],
#   [40, 48, 56, 64, 72, 80],
#   [45, 54, 63, 72, 81, 90],
#   [50, 60, 70, 80, 90, 100]]`
#  - The square root of each number in list 1 - use `math.sqrt()`: `[2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.0, 3.1622776601683795]`

#%%
test_list1 = [5, 6, 7, 8, 9, 10]
range_list = list(range(5,11))

print(range_list)

# Type your answer below in this box
# list.extend(range_list)
print(list)

# adding two list elements

# Method #1
method1_list = []
for i in range(0, len(test_list1)):
    method1_list.append(test_list1[i] + range_list[i])
print("Method #1 addition: ", end = '')
print(method1_list)   

# Method #2 (list comprehension)
"""method2_list = [list[i] + range_list[i] 
                for i in range(len(test_list1))]
print("Method #2 comprehension: ", end = '')
print(method2_list)"""

# Method #3 map() + add()
from operator import add
method3_list = list(map(add, test_list1, range_list))
print("Method #3 map() + add(): ", end = '')
print(method3_list)

# Method #4 zip() + sum()
method4_list = [sum(i) for i in zip(test_list1, range_list)]
print("Mathod #4 zip() + sum(): ", end = '')
print(method4_list)

# Print first 3 elements of the list
print(test_list1[slice(0, 3)])

# Print list backwards
test_list1.reverse()
print(test_list1)
test_list1.reverse()
print(test_list1)

def Reverse(lst):
    lst.reverse()
    return lst

print("Reverse list ", Reverse(test_list1))
print(Reverse(test_list1))

# Method #1
for i in test_list1:
    if (i % 2 == 0):
        print(i, " ", end = '')
        
print("")
        
# Method #2 (using list comprehension)
even_nos = [num for num in test_list1 if num % 2 == 0]
print("Even numbers from the list using list comprehension", even_nos)

# Method #3 (using lambda expressions)
even_nos = list(filter(lambda x: (x % 2 == 0), test_list1))
print("Even numbers from the list using lambda", even_nos)

#%% [markdown]
# From the two dimensional array you just created, extract or calculate the following:
# - The second row: `[30, 36, 42, 48, 54, 60]`
# - The fifth column: `[45, 54, 63, 72, 81, 90]`
# - The sum of the first row: 270
# - The sum of the leading diagonal (top left to bottom right): 355

#%%
# Type your answer below in this box

#%% [markdown]
# # Sets
# Define two sets: `{'Cat', 'Dog', 'Pig', 'Cow'}` and `{'Cat', 'Cow', 'Rat', 'Fish'}`
# Using them, calculate the following:
# - The union of the two sets: `{'Cat', 'Cow', 'Dog', 'Fish', 'Pig', 'Rat'}`
# - The intersection of the two sets: `{'Cat', 'Cow'}`
# 
# Now remove `Cat` from the first set and add `Goat` instead.

#%%
# Type your answer below in this box


#%%
# Type your answer below in this box

#%% [markdown]
# Now, select all the four letter animal names from both sets into a single new set: `{'Fish', 'Goat'}`

#%%
# Type your answer below in this box

#%% [markdown]
# # Tuples, Sets and Lists
# Create a tuple, a set, and a list containing `1,2,3,4`
# See what happens if you add the element `2` to each of them. You won't be able to update the tuple. You'll need to create a new one with `(1,2,2,3,4)`.
# Look at the `id()` of each object before and after it is updated. What do you know about their immutability?
# 

#%%
# Type your answer below in this box

#%% [markdown]
# # Dictionaries
# Create a dictionary object that represents the data about a single customer storing a first name, surname, age, and a list of three named products they have bought, along with the price they paid for each product. Make up keys and values as you like.

#%%
# Type your answer below in this box

#%% [markdown]
# ## Write code to produce a sentence that says:
# `The customer named (insert name) bought the following (count of things bought) things: (list the names of the things)` Obviously, you should replace the parts in brackets with expressions that extract data from the dictionary
# 

#%%
# Type your answer below in this box

#%% [markdown]
# ## Calculate the total money spent by this customer

#%%
# Type your answer below in this box

#%% [markdown]
# # Extract just the prices paid into an array

#%%
# Type your answer below in this box

#%% [markdown]
# # Add a new field for the customer's phone number.

#%%
# Type your answer below in this box

#%% [markdown]
# # Still have time?
# Explore more about using different data structures to store and manipulate data. Use your own initiative to invent more examples.

#%%



