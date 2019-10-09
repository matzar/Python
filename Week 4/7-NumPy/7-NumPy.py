# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
# # ITNPBD2 Representing and Manipulating Data
# 
# # NumPy
# ## Array processing in Python
# 
# * Mostly used for numeric data
# * Installed by default in Anaconda Base Distribution
# * Use `pip install numpy` if you don't have it
# * Can handle 1D, 2D or higher dimensional arrays. Here we stick to 1D and 2D

#%%
import numpy as np

x = np.array([1, 2, 3])
print(x)

#%% [markdown]
# # Indexing
# * Integer index. In 2D the order is row, column
# * Slicing using `:` to specify a whole row or column

#%%
y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Array", y)
print("Row 1", y[1])
print("Row 1, Column 2 intersect", y[1, 2])
print("Column 1", y[:,1])

#%% [markdown]
# # More Slicing
# * `s:e` to slice from `s` to `e-1`

#%%
print("Rows 0 to 1", y[0:2])
s = 0
e = 2
print("The same, but with variables defining start and end",y[s:e])
print("Columns 1 and 2", y[:,1:3])
print("The top left square of 2 by 2", y[0:2,0:2])

#%% [markdown]
# # Conditional Selection
# * Select those elements of an array that satisfy a condition
# * Or select with a mask - a NumPy array of `True` or `False`

#%%
gr_five = y[y>5]
print(gr_five)


#%%
print(y>5)


#%%
my_sel=np.array([[True, False, False], [False, True, False], [False, False, True]])
print(my_sel)
print(y[my_sel])

#%% [markdown]
# # Arrays of indexes
# * Give an array of rows, then an array of columns
# * Extract the values from the intersection locations

#%%
# Extracts locations [0,0], [1,1], [2,2]
print(y[[0, 1, 2], [0, 1, 2]])

#%% [markdown]
# # NumPy Array Shapes
# ## Specified by a tuple
# * In 2D the tuple is (rows, cols)
# * in 1D it is (elements, ) note this `,` showing this is still a tuple
# * Higher dimensions have more entries: (x,y,z) etc.
# 
# ## Define an array by shape

#%%
ones = np.ones((2, 3))
print(ones)

#int_ones = np.ones((2, 3), dtype=np.int)
#print(int_ones)


#%%
rand_ar = np.random.random((5,))
print(rand_ar)

#%% [markdown]
# # Get the shape with `shape`
# # Reshape an exsting array with `reshape`

#%%
z = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print(np.shape(z))
# print(z.shape)
z = np.reshape(z, (4, 2))
print(z)

#%% [markdown]
# ## Now we can see a higher dimensional example
# * `arange` creates an array of numbers spanning a given range
# * Then we reshape that into a 3D 3 by 3 by 3 array

#%%
a = np.arange(27).reshape((3, 3, 3))
print(a)

#%% [markdown]
# # Elementwise Maths
# * Simple operators like `+,-,*,/` are overloaded in NumPy to operate on whole arrays, one element at a time

#%%
y = y+10
print(y)

#%% [markdown]
# # Select and Operate
# * Combine selection and elementwise operations to operate only on selected elements

#%%
y[y>13]+=100
print(y)

#%% [markdown]
# # Reading and Writing With Files
# * Read a whole file into a NumPy array
# * Write data to a new file

#%%
sleep = np.loadtxt("data\sleep.csv", skiprows = 1 ,delimiter = ",")
sleep


#%%
np.savetxt("data\sleep2.csv",sleep,delimiter=",",
           header="Exercise Minutes,Coffees,Av HR,Eat after 9pm,Steps,Age,Hours awake,Day,Sleep Rating")


#%%
np.savetxt("data\sleep2.csv", sleep,delimiter = ",",
           header = "Exercise Minutes,Coffees,Av HR,Eat after 9pm,Steps,Age,Hours awake,Day,Sleep Rating",
          fmt = "%d")

#%% [markdown]
# # Aggregation and Other Functions
# * Aggregating arrays or parts of arrays with functions like `sum` and `avgerage`
# * Note that `df[:,i]` selects the `i`th column

#%%
print(sleep[:,0])


#%%
print("Average exercise minutes:",np.average(sleep[:,0]))
print("Total Coffees:",np.sum(sleep[:,1]))

#%% [markdown]
# ## Last variable is `sleep rating`
# * Lets find the average sleep rating for 3 coffees and for 0 coffees

#%%
print("Max sleep rating:", np.max(sleep[:,8]))
print("Min sleep rating:", np.min(sleep[:,8]))

print("Max Coffees:", np.max(sleep[:,1]))
print("Min Coffees:", np.min(sleep[:,1]))

#%% [markdown]
# ## Extract Only rows where coffees==0
# ## Find Average
# ## Then same for coffees==3

#%%
no_coffee = sleep[sleep[:,1]==0]
print(no_coffee)
print(np.average(no_coffee[:,8]))
      
lots_coffee = sleep[sleep[:,1]==3]
print(lots_coffee)
print(np.average(lots_coffee[:,8]))

#%% [markdown]
# # Broadcasting
# * When performing an arithmetic operation with 2 arrays of different size
# * Smaller of the 2 is broadcast across the bigger to line them up
# 
# ## Simple version - multiply by a scalar
#%% [markdown]
# # Extract Indices of interest with `where`
# ## Then extract a given column using the indices to get the rows

#%%
lots_coffee_indices = np.where(sleep[:,1]==0)
print(lots_coffee_indices)
print(sleep[lots_coffee_indices, 8])


#%%



