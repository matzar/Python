# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%%
from IPython import get_ipython

#%% [markdown]
# # ITNPBD2 Representing and Manipulating Data
# 
# ## Python Coding Style
# ## Python Scope and Mutability
# ## Measuring Run Time and Optimising Speed
# Three quite different and unrelated topics!
#%% [markdown]
# ## 1) PEP 8 Coding Style
# 
# There is a published guide to the style you should use when writing Python code. It dictates things like where spaces should or shouldn't be inserted, how to use indentation, where to use upper or lower case letters for names, and how to write comments.
# 
# The official guide is here 
# 
# https://www.python.org/dev/peps/pep-0008/
#%% [markdown]
# # The two main concepts are that code should be:
# 
# ## - Readable
# ## - Consistent
# 
# Though occasionally, you should allow inconsistency if it interferes with something more important.
#%% [markdown]
# # Indentation
# 
# ## Code should be indented to:
# - Define a block of code
# - break up a line of code that is too long (more than 79 characters)
# - Line up something in open and closing brackets that is long

#%%
# A block of code
if (1==2):
    print("How did I get here?")
    print("That can't be right")
print("Now, I can be here")

a_long_variable_name = 1

print("I've called my variable 'a_long_variable_name' even though it has the value",
     a_long_variable_name)

# Note the comma separated parts of this
print("This is a very long piece of text, well, at least long enough that it would",
     "be better to split it over two lines")

#%% [markdown]
# ## Blocks of code should be indented by 4 spaces - not a tab
# 
# ## Longer indents can be used to line up brackets on new lines
# 
# ## If the lining up of brackets is 4 spaces in, make it a few more so it doesn't look like a block
#%% [markdown]
# ## Put binary operators (+, - etc) at start of broken lines:
# Note the use of brackets - remove them and you'll get an indent error

#%%
numbers = [1, 2, 3]
sum = (numbers[0]
    + numbers[1]
    - numbers[2])
print(sum)
    

#%% [markdown]
# # Spaces
# ## Here are some examples of the correct use of spaces:

#%% [markdown]
# Variable assignment - a space either side of the =
# `x = 1`
# Array list - spaces after the commas
# `x = [1, 2, 3]`
# Index - no spaces
# `y = x[1]`
# Function call - no space on either side of the brackets
# `print("Hello")``
# Simple expression - No space near +
# `x = a+b`
# Expression with operator priority - space to show which is evaluated first
# (doesn't affect calculation, just readability)
# `x = a*b + c*d`

#%% [markdown]
# # Comments
# 
# ## Comments should be informative!
# ## Write comments in proper English
# ## Don't state the obvious - explain why the code is there as well as what it does

#%%
# This is bad ...
# x = x + 1    # Add one to x

# This is better ...
# x = x + 1

# This is good if needed
# x = x + 1    # Add one to x to account for the counter starting at 1 instead of zero

#%% [markdown]
# # Longer comments use docstring
# 
# ## Used only for modules, functions, classes, and methods
# 
# ## Multi line comments start and end with `'''`
# Proper sentences and proper punctuation.
# 
# If you add docstrings to function and class definitions, users can access them with the `help` function

#%%
def str_int_concat(st, num):
    '''Concatenate an integer and a string to produce a new string
    
    Args:
        num (int): The integer to append to the string
        st (str): The string to append to
    
    Returns:
        str_int_concat (string): A string that is the result of appending the number argument to the end of the string argument
    '''
    
    return st+str(num)

conc = str_int_concat("Cat",2)
print(conc)
help(str_int_concat)

#%% [markdown]
# # Naming conventions
# 
# ## Classes use first letter UpperCase no spaces
# ## Variables and functions use lower_case and underscores
# ## Constants are in ALL_CAPITALS and underscores
# 
#%% [markdown]
# # Functions
# 
# ## Either all return routes should return a value, or none
# 
# ## Try to group return statements at start and end, not in the middle of a function

#%%
# Good - all routes return a value
def sqr_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None
    
# Good - quick return at start, all others at end

def complicated(x):
    if x < 0:
        return None
    else:
        if x == 1:
            r = 2
        elif x == 2:
            r = 5
        elif x == 3:
            r = 8
        else:
            r = -1
    return r          # Single return here
complicated(7)

#%% [markdown]
# # Something Completely Different:
# # Variables, Objects and Mutability and Scope
# - Variables in Python are immutable - once defined their value cannot change
# - Objects are mutable, you can change parts of them after they are defined
# - Explore the identity of variables and objects with `id()`

#%%
# Define x
x = 1000
# See where it is stored
print(id(x))
# Give it a new value
x = 5000
# See that it is a new variable
print(id(x))

#%% [markdown]
# # Variable Scope
# 
# ## Which parts of the code refer to which version of a named variable
# 
# - Variables defined at the top level of code are readable everywhere
# - What happens if you write to them depend on their mutability and whether or not they are treated as global

#%%
a=1
b=2

def a_func():
    global a
    print("In the function, variable a is made global, its value is",a)
    print("In the function, I can see b, even though it is not global:",b)
    a = 2
    print("Still in the function, a has been re-assigned:", a)

print("Before we call the function: a and b are:",a,b)
a_func()
print("After we call the function: a and b are:",a,b)

#%% [markdown]
# ## What if we assign a value to `b` in the function?
# - `b` is local to the function and its value does not change outside the function
# - This is because it is immutable - the new version of `b` in the function is not the same variable as the one outside

#%%
a=1
b=2

def a_func():
    global a
    print("In the function, variable a is made global, its value is", a)
    b=5
    print("In the function, I have assigned a new value to b:", b)
    a = 2
    print("Still in the function, a has been re-assigned:", a)

print("Before we call the function: a and b are:", a, b)
a_func()
print("After we call the function: a and b are:", a, b)

#%% [markdown]
# # Note - we cannot mix scopes in a function
# - Here we try to print `b` but assign it later and get an error
# - See what happens if we comment out the `b = 1` statement

#%%
# b = 1

# def a_func():
#     global a
#     print("Can't print b yet because we define it below", b)
#     b = 1

# a_func()

#%% [markdown]
# # Use `id()` to get a better idea

#%%
a = 1000
b = 1001
print(id(a), id(b))

def f():
    global a
    b=5
    print(id(a), id(b))

f()
print(id(a), id(b))

#%% [markdown]
# # What about mutable objects?
# - A function can see those and change their values, so be careful!
# - Here is some code that works, but is bad practice because it has hard to guess side effects

#%%
def add_to_a():
    a.append(5)
    
a = [1, 2, 3]
add_to_a()
print(a)

#%% [markdown]
# # The same applies to arguments sent to functions
# - A reference to the argument from the calling level is sent in to the function
# - If it is a mutable object, it can be operated on and changed
# - If it is immutable, then an assignment creates a new, local variable
# - They cannot be made global

#%%
def f(c):
    print(c,id(c))

d = 2000
#d = [1, 2, 3]
print(id(d))
f(d)

#%% [markdown]
# # A final note on IDs
# ## Numbers from -5 to 255 each always have the same ID regardless of how they are used
# 
# ## This is a little optimisation

#%%
a = 5
b = 5
print(id(a), id(b), id(5))

a = 500
b = 500
print(id(a), id(b), id(500))

#%% [markdown]
# # Timing Your Code
# - Different ways of doing things in Python can take different amounts of time
# - You should strive to write code that runs FAST
# - You can time your code to compare alternative ways of doing things
# - In Jupyter notebook, use `%timeit` to time the next line and `%%timeit` to time the whole cell
# - Both of these run the code repeatedly and report the average and deviation of the time taken

#%%
get_ipython().run_cell_magic('timeit', '', '\nfor i in range(1000000):\n    x = i*i')

#%% [markdown]
# # Built in NumPy methods are much faster than iterating
# - If you find yourself writing a loop of any kind, ask yourself if you could do the same thing without it
# - In Numpy, you can apply a function to an entire array MUCH faster than programming a loop
# - This is because NumPy runs optimised C, which is fast

#%%
import numpy as np
import timeit

code_to_test = """
a = range(100000)
b = []
for i in a:
    b.append(i*2)
"""
elapsed_time = timeit.timeit(code_to_test, number=100)/100
# print(elapsed_time)

%timeit mill = np.random.random(10000)
# print(mill)

x = 5
# %timeit y=x**2

# %timeit s = sum(mill)
#%% [markdown]
# ## A small improvement when reading:

#%%
get_ipython().run_cell_magic('timeit', '', 's = 0\nfor x in mill:\n    s = s+x')


#%%
get_ipython().run_cell_magic('timeit', '', 's = sum(mill)')

#%% [markdown]
# ## But a huge improvement here when writing

#%%
get_ipython().run_cell_magic('timeit', '', 'for i in range(1000000):\n    mill[i] = mill[i]+2')


#%%
get_ipython().run_cell_magic('timeit', '', 'mill2 = mill+2')


