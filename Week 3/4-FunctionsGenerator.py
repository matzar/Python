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
# def add_list(*nums):
#     return sum(nums) - 100

# print(add_list(1, 2, 3))

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

print(add_three(1, 2, 4))
numlist=[1, 2, 4]
print(add_three(*numlist))

kwlist={'a':1, 'b':2, 'c':4}
print(add_three(**kwlist))

def add_three_values(x, y, z):
    return x + y + z

print("")

print(add_three_values(0, 1, 2))
print(add_three_values(*[0, 1, 2]))
print(add_three_values(**{'x' : 0, 'y' : 1, "z" : 2}))

#%% [markdown]
# ### Which to use depends on how the function is defined:
# - `zip(*iterables)` is a function for aggregating elements from a list of iterables
# - It is defined with `*` as a variable length argument list
# - So we can call it with a variable number of arguments:

#%%
i = list(zip('123', 'abc'))
print (i)
j = list(zip('xyz', '123', 'def'))
print (j)

#%% [markdown]
# ### Or use a `*` when we call it to send a single list of values to be unpacked into arguments

#%%
xy=[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
x,y = zip(*xy)
print(x)
print(y)

ab = [  ('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), 
        ('f', 6), ('g', 7), ('h', 8), ('i', 9), ('j', 10), 
     ]

a, b = zip(*ab) # unpack a list of tupels into values
print("a:", a)
print("b:", b)
print("sum(b):", sum(b))

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

x = lambda x, y, z = 0 : x + y + z
print(x(0, 1))

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

r = lambda a, b : a + b
print(r(random.randrange(0, 10), random.randrange(0, 10)))

def print_random_between(begin, end):
    print(random.randrange(begin, end))

lambda_print_random_between = lambda begin, end : print_random_between(begin, end)

print_random_between(0, 10000)
lambda_print_random_between(0, 10000)

lambda_return_tuple = lambda a, b : (random.randrange(a, b), random.randrange(a, b)) # declare lambda which returns a tuple
temp = lambda_return_tuple(0, 10000) # save lambdas return value in temp value
print(temp) # print tuple from lambda

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

l_is_a_list = [ z * z for z in range(0, 2)]
print(l_is_a_list)

#%%
# Iterable into a generator
g = (x*x for x in range(0, 5))
print(g)    # g  is an object!

print("iterable into a generator: ", end='')
for i in g:
    print(i, " ", end='')

print('\n')

a = 0
b = 3
g_is_an_object = (i * i for i in range(a, b))
print(g_is_an_object)

print(f"iterable into a generator in range ({a}, {b}): ", end='')
for i in g_is_an_object:   # you can iterate over a generator only once
    print(i, " ", end='')  # usefull for large structures

for i in g_is_an_object:   # this line will not be executed because
    print(i, " ", end='')  # we can iterate over a generator only once

#%% [markdown]
# ## Write a generator function
generator_function = (x * 10 for x in range(1, 11))

for i in generator_function:
    print(i)

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

import math as mt
import matplotlib.pyplot as plt

def square_root_of_sine_gen_in_range(a, b):
    for i in range(a, b):
        yield mt.sin(i) * mt.sin(i)

sqrt = square_root_of_sine_gen_in_range(0, 5)
print(sqrt)
for i in sqrt:
    print(i)

sqrt = square_root_of_sine_gen_in_range(0, 5)
print(list(sqrt))

sqrt = square_root_of_sine_gen_in_range(0, 5)
plt.figure(10)
plt.plot(mt.sqrt(0.5))

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

import math as mt
# wrapper funciton
# pass function to function
def wrapper_pass_2_arguments(func, i, j):
    return func(i, j)    # pass i to func using wrapper function

def sqrt_two_numbers(x, y):
    return (mt.sqrt(x), mt.sqrt(y))
square_root_of_two_numbers = wrapper_pass_2_arguments(sqrt_two_numbers, 2, 3)
print("square_root_of_two_numbers: ",square_root_of_two_numbers)

def mult_sine_of(r1, r2):
    return mt.sin(r1) * mt.sin(r2)
multiple_of_sine = wrapper_pass_2_arguments(mult_sine_of, 0.5, 0.7)
print("\nmultiple of sine: ",multiple_of_sine)

# pass two functions as a list of functions
funcs=[sq,halve]
# make a list of functions
list_of_functions = [sqrt_two_numbers, mult_sine_of] # list of functions

for f in funcs:
    print(apply_to_x(f, 6))

for function in list_of_functions:
    print("function:", function.__name__, "- output:", wrapper_pass_2_arguments(function, 2, 3) )

#%% [markdown]
# ## Lambda functions
# - Sometimes called anonymous functions, because they need no name!
# - Defined and called in place where a function call would be used

#%%
print(apply_to_x(lambda x: x+5, 5))

print(wrapper_pass_2_arguments(lambda x, y : mt.sqrt(x) + y, 2, 2 ))

# wrapper function that takes only a function as an argument
def wrapper_func(f):
    return f()
print(wrapper_func(lambda x = 0 : x )) # wrapper takes a lambda function; lambda needs to have default arguments defined
#%% [markdown]
# ## Map
# - `map(function, iterable)`
# - Apply a function to every item in an iterable
# - Produce an interable as a result


#%%
itr_res = map(sq,[1, 2, 3, 4, 5])
# print(itr_res)
# print("iter_res:", end='')
# for r in itr_res:
#     print(r, end='')

class class_iter_results:
    def sqrt_number(x):
        return mt.sqrt(x)

    list_of_nums = [2, 3, 25, 2.9, 3.7]
    # def __init__(self):
    iter_result = map(sqrt_number, list_of_nums)

    def get_map():
        return iter_result

c = class_iter_results()
# TODO why do I have to declare iter_result each time?
print("\niter_result using (printing using `j = 0` value):")
j = 0
for i in c.iter_result:
    print(f"sqrt({c.list_of_nums[j]}) =", i)
    j += 1

iter_result = map(sqrt_number, list_of_nums)
print("\niter_result (printing using zip):")
for k, y in zip(list_of_nums, iter_result):
    print(f"sqrt({k}) = {y}")

iter_result = map(sqrt_number, list_of_nums)
print("\niter_result (printing using enumerator):")
for i, j in enumerate(iter_result):
    print(f"sqrt({list_of_nums[i]}) = {j}")

#%%
# Build a map of functions and a list of numbers in range(1, 6)
itr_res = map(sq,range(1, 6))
# Put the result into list
res_list=list(itr_res)
print(res_list)

# Apply a function to all the numbers in a list using a map
i_r = map(sqrt_number, range(1, 6)) # Build a map of functions and a list of number in range(1, 6)
r_l = list(i_r) # Put the result of inputing the numbers in range(1, 6) into sqrt_number function
print(r_l) # Print the list of numbers
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
# TODO what is reduce?
from functools import reduce

def red_sum(acc, val):
    # print(f"acc:{acc}, val:{val}")
    return acc + val

l_range = (range(1,6))
print(reduce(red_sum, l_range))

reduce_example = reduce(lambda x, y : x * y, [1, 2, 3, 4, 5])
print(reduce_example)
print(lambda x, y, z : x * y + z, [1, 2, 3])
print(reduce(lambda x, y : x * y, [1, 2, 3], [2, 3, 2]))

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

def is_perfect_square(x):
    return math.sqrt(x) == int(math.sqrt(x))

begin = 0
end = 10001
candidates_for_perfect_squares = range(begin, end)
list_of_perfect_squares = list(filter(is_perfect_square, candidates_for_perfect_squares))

# print(list_of_perfect_squares)
print(f"list of perfect squares within range({candidates_for_perfect_squares.index(begin)},{candidates_for_perfect_squares.index(end - 1)})")
for i in list_of_perfect_squares:
    temp = int(math.sqrt(i))
    print(f"sqrt({i}) = {temp}")

#%%
# Or with a lambda function

candidates=range(1,101)
squares=filter(lambda x:x>75 and x<81, candidates)
print(list(squares))

# this is the same as ->
candidates = range(1, 10001)
print(list(filter(lambda x : x > 1075 and x < 1077, candidates)))
print(list(filter(lambda x : x > 1075 and x <= 1077, candidates)))
print(list(filter(lambda x : x >= 1075 and x < 1077, candidates)))
print(list(filter(lambda x : x >= 1075 and x<= 1077, candidates)))
# -> this
print(list(filter(lambda x : x > 1075 and x < 1077, range(1, 10001))))
print(list(filter(lambda x : x > 1075 and x <= 1077, range(1, 10001))))
print(list(filter(lambda x : x >= 1075 and x < 1077, range(1, 10001))))
print(list(filter(lambda x : x >= 1075 and x<= 1077, range(1, 10001))))

#%%
## List Comprehension
# - Apply an expression to every item in a sequence and produce a list of results
word="Hello"
shiftup = [chr(ord(x)+1) for x in word]
print(shiftup)

word = "Hello"
shift_down = [chr(ord(c) - 1) for c in word]
print(shift_down)

print(list(chr(ord(c) - 1) for c in word))
print([chr(ord(c) + 2) for c in word])
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

younger = [car['Car'] for car in cars if car['Age'] <= 30]
print(younger)

