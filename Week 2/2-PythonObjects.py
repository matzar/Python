# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
# ## ITNPBD2: Representing and Manipulating Data
# ## University of Stirling
# ## Dr. Kevin Swingler
#%% [markdown]
# # Python Data Objects
#%% [markdown]
# ## Variables
# - Variables are named objects that contain a value that can vary!
# - Set a named variable to a value using the = sign

#%%
age = 30
print("Age is", age)

#%% [markdown]
# ## Concatenating strings is done with the + sign

#%%
fname="Kevin"
sname="Swingler"
fullname=fname + " " + sname
print(fullname)

fname="M"
sname="Z"
fullname= fname + " " + sname
print(fullname)

#%% [markdown]
# ## Let's try that with age

#%%
name_age = fullname + " is " + str(28)
print(name_age)

#%% [markdown]
# # Age is the wrong data type
# ## Data Types define what can be done to a variable, and how:

#%%
age = 28
print(age)

age = age + 1
print(age)

#%% [markdown]
# # So we need to tell Python to treat `age` as a string

#%%
name_age=fullname + " is " + str(age)
print(name_age)

#%% [markdown]
# # Basic Python Data Types
# 
#  - Integer `int`
#  - Float `float`
#  - String `str`
#  - Boolean `Bool` (0=False, all else = True)

#%%
print(3.1)
print(int(3.1))
print(3)
print(float(3))
print(bool(0))
print(1e+2)
print("")
print(2.1)
print(int(2.1))
print(2)
print(float(3))
print(bool(1))
print(1e+5)

#%% [markdown]
# 
# # Find out the type using `type`

#%%
a = 3.1
print(a,type(a))

b = 2e5
print(b, type(b))

#%% [markdown]
# # Back to strings
# Enclose them in either single or double quotes: " or ' use one inside the other

#%%
print("I can do this to enclose this 'word' in single quotes")
print('Or this "word" in double quotes')
#print("But this "gives" and error")

#%% [markdown]
# ## The slash character: `\` is used to insert special characters, like extra quotes:
# - `\t` Tab
# - `\n` Newline
# - `\"` Double quote
# - `\'` Single quote

#%%
print("There is a \t tab space there")
print("Here is a \nnewline")
print("And here we insert a \"double quote\"")
print('And a \'single\' one')

print("I can use tab like \tthis")
print("Here is a \nnewline")
print("That's how you can insert \"double quotes\"")
print("That's how you can use \'single quotes'")

#%% [markdown]
# ## The % placeholder is used to insert variable values into a string
# - `%d` Integer
# - `%f` Float
# - `%s` String

#%%
print("This string contains an integer, %d a float, %f and a string, %s" %(1,2,"dog"))
print("This string contains an integer, %d, a float %f, and a string, %s" %(1, 2, "dog"))

#%% [markdown]
# ## f-strings are better

#%%
animal = "dog"
age = 3
print(f"My pet is an {animal} and it is {age} years old")
# You can put anything in the {} braces - try it!
print(f"My pet is a {animal} and is it {age} y/o")

#%% [markdown]
# # Lists and Tuples
# - What if you want to store more than one value in a single structure?
# - Lists are for variable length lists
# - Tuples are for fixed sets of values
# - Both can be of mixed types
# - Both can contain literal values or variables
# - Tuples are immutable

#%%
l1 = [1, 2, 3]
l2 = [1, 1.2, "a"]
v=3
l3=[1, 2, v]
t=(3,4)

tuple1 = [1, 2, 3]
tuple2 = [100, 5.4, "c"]
var = 3
tuple3 = [1, 2, var]
tuple4 = (5, 6)

print(l1, l2, l3, t)
print(tuple1, " , ", tuple2, var, tuple3, tuple4)


#%%
v=5
w = 6
print(v, l3)
print(v, w, 22, tuple2)


#%%
v = 55
list3 = [1, 2, v]
list3.append("more")
print(list3)

list3.insert(2, "Budge up")
print(list3)

tuple3.append("added string")
tuple3.insert(2, 555)
print(tuple3)


#%%
l3 = l3 + [5,6,7]
l3

tuple3 += [7, 8, 9]
print(tuple3)


#%%
t.append("more") # Can't do this
tuple3.append(5)

#%% [markdown]
# ## Tuples are useful for carrying multiple return values from a function

#%%
def div_and_remainder(a,b):
    div=int(a / b)
    rem=a % b
    return div,rem

print(div_and_remainder(10, 3), '\n')

def quotient_and_remainder(x, y):
    quotient = int(x / y)
    remainder = x % y
    return quotient, remainder

var = quotient_and_remainder(10, 6)
print(f"Quotient: {var[0]}\nRemainder: {var[1]}\n")
print(f"Quotient: {quotient_and_remainder(10, 6)[0]}\nRemainder: {quotient_and_remainder(10, 6)[1]}")

#%% [markdown]
# ## Both lists and tuples can be accessed by their index, starting at zero

#%%
print(t[1])
print(l3[0])

print(l3[-1])

l3[2]="New entry"
print(l3)

# Can't do this:
#t[0] = 1

list1 = [5, 6, 7]
tuple2 = [2, "2", 3]

list1[1] = 100
print(list1)

# Can't do this:
tuple[1] = 100

#%% [markdown]
# ## Lists and tuples can be iterated like this

#%%
for item in l3:
    print(f"Next item is {item}")
    
for i in tuple1:
    print(f"i = {i} ")

#%% [markdown]
# # Slicing lists
# Access a sub range of a list with the `:` operator inside `[]` square brackets
# - `[s:f:p]` Start to one more than the finish, step p at a time
# - Miss the first number means start at the beginning
# - Miss the second number means finish at the end
# - Miss the third means step size is 1
# - Negative step size means start from the other end

#%%
one_to_ten = list(range(0, 10))
#print(one_to_ten)

#print(one_to_ten[2:5])
#print(one_to_ten[3:])
#print(one_to_ten[:3])
#print(one_to_ten[:4:-1])

print(one_to_ten[2:5])   # 
print(one_to_ten[3:])    # 
print(one_to_ten[:3:])   # 
print(one_to_ten[0:len(one_to_ten):3])
print(one_to_ten[:4:-1]) # go in the reveresed order by 1 until index 4
print(one_to_ten[:-1:4]) # go by 4 and finish at the last index

#%% [markdown]
# ## Sorting a list
# - Sort it in place with `sort()`
# - Create a sorted copy with `sorted()`

#%%
import random
r=[]
for i in range(10):
    r.append(random.randrange(1, 10))

# Method #1
print("r = ", r)
print("sorted(r) = ", sorted(r))

# Method #2
print("r = ", r)
r.sort()
print("r.sort() then print", r)

#%% [markdown]
# ## Removing items from a list
# - Remove the last item and get its value with `pop`
# - Remove by index with `del`
# - Remove by value with `remove`

#%%
print(r)
print(r.pop()) # remove last item
print(r)

#del r[len(r) - 1] # remove an item at the index number 3
print(r)

if(4 in r):
    r.remove(4) # remove by value, in this case remove value equal to 4
    print(r)
else:
    print("No 4 in list") # if there's no 4, print a message saying there's no 4 in the list

print(f"Length is now {len(r)}")

# generate a list of 10 random numbers 
rnd_list = []
for i in range(10):
    rnd_list.append(random.randrange(1, 10))
print(rnd_list)

if (5 in rnd_list):
    rnd_list.remove(5)
    print(rnd_list)
else:
    print("There's no 5 in rnd_list")
    
del rnd_list[len(rnd_list) - 1]

#%% [markdown]
# ## Two dimensional lists

#%%
m=[]
for i in range(5):
    m.append([])
    for j in range(5):
        m[i].append(i * (j+1))
display(m)

d2 = []
for i in range(10):
    d2.append([])
    for j in range(10):
        d2[i].append(i * (j + 1))
display(d2)

#%% [markdown]
# # Select elements, rows and columns

#%%
row2_col3 = m[2][3]
print("row2_col3 = m[2][3] =", row2_col3)

r1 = m[1]
print("r1 = m[1] =", r1)

c1 = [row[1] for row in m]
print("c1 =", c1)

r2_d2 = d2[2]
print("r2_d2 = d2[2] =", r2_d2)

c3 = [row[1] for row in d2]
print("c3 =", c3)

row3_col4 = d2[3][4]
print("row3_col4 = d2[3][4] =", row3_col4)

#%% [markdown]
# # Sets
# - Unordered
# - No repeating values
# - Defined with `{ }` braces
# 

#%%
s1 = {1, 2, 3} # set
s2 = {2, 3, 4} # set
display(s1)
display(s2) # display makes a new line after each execu

print("s1.union(s2) =", s1.union(s2))
print("s1.intersection(s2) =", s1.intersection(s2))


#%%
s1.add(4)
print(s1)

s1.add(1000)
print(s1)

s2.add(99)
print(s2)

s = set()  # empty set declaration
s.add(500)
print(500)


#%%
print(s1)

s1.remove(4)
print(s1)

s1.remove(1000)
print(s1)

print(s2)
s2.remove(99)
print(s2)

#%% [markdown]
# Note - we declare an empty set with `set()` not `{}`, which is an empty dictionary
#%% [markdown]
# ## Later we will meed more sophisticated matrix representations such as numpy and pandas

