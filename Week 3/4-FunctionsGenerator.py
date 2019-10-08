# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
# ## ITNPBD2: Representing and Manipulating Data
# ## University of Stirling
# ## Dr. Kevin Swingler
#%% [markdown]
# # Functions, Generators, Functional Programming
# ## Avoid repeating code by putting code you use a lot in a function
# 
# - Defining and calling functions
# - Parameter passing
# - Return values
# 
#%% [markdown]
# ## Define a function

#%%
def mark_to_grade(mark):
    if mark < 50:
        grade = "Fail"
    elif mark < 60:
        grade = "Pass"
    elif mark < 70:
        grade = "Merit"
    else:
        grade = "Distinction"
    return grade

# define a function
def m_g(m):
    if m < 50:
        g = "Fail"
    elif m < 60:
        g = "Pass"
    elif m < 70:
        g = "Merit"
    else:
        g = "Distinction"
    return g
#%% [markdown]
# ## Call a function and store its result

#%%
grade = mark_to_grade(50)
print(grade)

print(m_g(70))
#%% [markdown]
# ## Positional Arguments
# - Names of arguments are matched to their position

#%%
def pos_arg(a, b):
    print(f"a is {a}, b is {b}")
pos_arg(1, 2)

def fpos_arg(c, d):
    print(f"c is {c} and d is {d}")

fpos_arg(213, 12421)

#%% [markdown]
# ## `#` Keyword Arguments
# - Name of arguments are matched by name

#%%
pos_arg(b=3, a=1)

fpos_arg(c=300, d=4)
fpos_arg(d=300, c=4)

#%% [markdown]
# ## Variable Length Argument Lists
# - When there can be a variable length list of arguments to a function
# - They are automatically wrapped in a tuple in the function
# - Put a `*` infront of the argument when you define the function

#%%
def add_list(*nums):
    return sum(nums) - 100

print(add_list(1, 2, 3))

# overwrite add_list definition
def add_list(*nums): # use `*` when there's going to be a list of arguments passed
    return sum(nums) - 200

print(add_list(1, 2, 3))

#%% [markdown]
# ## Variable Length Keyword Arguments
# - Specify that the function accepts a variable length of keyword arguments
# - Use `**` infront of argument list name

#%%
def kwargs_example(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} = {v}")

kwargs_example(a=1, b=2, c=3)

def key_words_arguments(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} = {v}")

key_words_arguments(x = 0, y = 1, z = 2)

#%% [markdown]
# ## Unpack an array into arguments
# - When you have an array that represents the arguments to a function
# - Put a `*` infront of the argument when calling the function and use an array

#%%
def add_three(a, b, c):
    return a + b + c

print(add_three(1, 2, 3))
numlist=[1, 2, 3]
print(add_three(*numlist))

kwlist={'a':1, 'b':2, 'c':3}
print(add_three(**kwlist))

#%% [markdown]
# ### Which to use depends on how the function is defined:
# - `zip(*iterables)` is a function for aggregating elements from a list of iterables
# - It is defined with `*` as a variable length argument list
# - So we can call it with a variable number of arguments:

#%%
print (list(zip('123', 'abc')))
print (list(zip('123', 'abc', 'xyz')))

#%% [markdown]
# ### Or use a `*` when we call it to send a single list of values to be unpacked into arguments

#%%
xy=[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
x,y = zip(*xy)
print(x)
print(y)

#%% [markdown]
# ## Default Arguments Values
# - Define a function with some arguments given default values
# - Can be tricky with positional arguments
# - Works very well with keyword arguments

#%%
#add_three(1, 2)  # Doesn't work - see add_three definition above
def add_two_or_three(a, b ,c=0):
    return a+b+c
print(add_two_or_three(1, 2))
print(add_two_or_three(1, 2, 3))

#%% [markdown]
# ## Return Values
# - `return` statement both ends the running of the function and tells it what to send back to the calling environment
# - You can return anything -arrays, dicts, tuples, etc.

#%%
import random

def ret_rand_tuple():
    a=random.randrange(0, 5)
    b=random.randrange(0, 5)
    return a, b

print(ret_rand_tuple())

#%% [markdown]
# ## Generator Functions and `Yield`
# - A generator is iterable, but does not store the values in memory
# - Can be useful for large structures
# - You can iterate over it once only
# - Defined like an iterable list, but with `()` instead of `[]`

#%%
# Iterable into a list
l = [x*x for x in range(0, 5)]
print(l)    # l  is a list


#%%
# Iterable into a generator
g = (x*x for x in range(0, 5))
print(g)    # l  is an object!


#%%
for x in g:
    print(x)

#%% [markdown]
# ## Write a generator function

#%%
def square_gen(s, f):
    for a in range(s, f):
        yield a*a

sq=square_gen(0,5)   # This is a generator object - the result of calling the function
print(sq)
for i in sq:         # This actually calls the function!
    print(i)
    
sq=square_gen(0,5)   # Define it again - iterables are one use only, remember!
print(list(sq))

#%% [markdown]
# ## Recursion
#  - A function that calls itself
#  - Often used to traverse a structure
#  
#  ### For example, the factorial of a number, n! can be defined recursively as:
#  - 1! = 1
#  - n! = n(n-1)!
#  ### The usual pattern is:
#  - A base case, which returns a value (1 in this case) and 
#  - A call to the same function again, but with a different value

#%%
def recur_factorial(n):
    # Base case: 1! = 1
    if n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * recur_factorial(n-1)
    
print(recur_factorial(5))


#%%
def recur_get_keys(d,keyset):
    '''Recursively get all the keys from a dictionary and all sub docs, including arrays of sub docs'''
    if isinstance(d,dict):    # If this value is a dictionary
        for k in d.keys():
            keyset.add(k)
            recur_get_keys(d[k],keyset)   # Here is the recursion
            if isinstance(d[k],list):
                for e in d[k]:
                    recur_get_keys(e,keyset) # and here
    return keyset

d1 = {'a':1, 'b':2, 'c':3}
k = recur_get_keys(d1,set())
print(k)

d2 = {'a':1, 'b':{'c':1}, 'd':[1,2,3], 'e':[{'f':1}, {'g':1,'h':1}]}
k = recur_get_keys(d2,set())
print(sorted(k))


#%%


#%% [markdown]
# # Functional Programming
# 
#%% [markdown]
# ## Passing a function as a parameter - High Order Functions

#%%
def apply_to_x(func, x):
    return func(x)

def sq(x):
    return x*x

def halve(x):
    return x/2

print(apply_to_x(sq, 5))
print(apply_to_x(halve, 5))


#%%
funcs=[sq,halve]
for f in funcs:
    print(apply_to_x(f, 6))

#%% [markdown]
# ## Lambda functions
# - Sometimes called anonymous functions, because they need no name!
# - Defined and called in place where a function call would be used

#%%
print(apply_to_x(lambda x: x+5, 5))

#%% [markdown]
# ## Map
# - `map(function, iterable)`
# - Apply a function to every item in an iterable
# - Produce an interable as a result

#%%
itr_res = map(sq,[1, 2, 3, 4, 5])
print(itr_res)


#%%
for r in itr_res:
    print(r)


#%%
itr_res = map(sq,range(1, 6))
res_list=list(itr_res)
print(res_list)

#%% [markdown]
# ## Reduce
# - Condense all contents of an iterable into a single thing
# - Produce an object
# - `reduce(function,iterable)`
# - The function does not get sent the list, however!!!! It is called repeatedly with two parameters
# - The next value in the list
# - A current accumulator
# - The first time it is called, it gets the first two items in the list, though

#%%
from functools import reduce

def red_sum(acc, val):
    print(f"val:{val}, acc:{acc}")
    return val+acc

print(reduce(red_sum,range(1, 6)))

#%% [markdown]
# ## Filter
# - Produces an iterable of objects that pass a test
# - The test is given as a function, the candidates as an iterable
# - `filter(function,iterable)`
# 

#%%
import math

def is_square(x):
    return math.sqrt(x) == int(math.sqrt(x))

print(is_square(9))
print(is_square(10))

candidates=range(1,101)
squares=filter(is_square, candidates)
print(list(squares))


#%%
# Or with a lambda function

candidates=range(1,101)
squares=filter(lambda x:x>75 and x<81, candidates)
print(list(squares))

#%% [markdown]
# # List Comprehension
# - Apply an expression to every item in a sequence and produce a list of results

#%%
word="Hello"
shiftup = [chr(ord(x)+1) for x in word]
print(shiftup)


#%%
sentence="This sentence has five words"
words_lens=[len(x) for x in sentence.split()]
print(words_lens)


#%%
pairs = [(1, 2), (3, 4), (5, 6)]
sums=[a+b for (a,b) in pairs]
print(sums)

#%% [markdown]
# ## We can even add a filter to the process with `if`

#%%
cars = [{'Age':20, 'Car':'Ford'}, {'Age':30, 'Car':'BMW'},{'Age':50, 'Car':'Mercedes'}]
older = [car['Car'] for car in cars if car['Age']>20]
print(older)


#%%



