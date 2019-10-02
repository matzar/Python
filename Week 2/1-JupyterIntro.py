# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
# # ITNPBD2: Representing and Manipulating Data
# ## University of Stirling
# ## Dr. Kevin Swingler
#%% [markdown]
# # Introduction to Jupyter Notebooks
#%% [markdown]
# - This is a __Jupyter Notebook__. It is a mixture of text (like this) and code (see below).
# - We will be using them in lectures and labs
# - Each of these boxes is called a __cell__ and you run its contents by selecting it and then either  pressing <ctrl> and <enter> or by clicking the Run button in the menu above

#%%
print("This is a section of code.")
print("It can have many lines, or just one.")

#%% [markdown]
# You can have many cells in a single notebook

#%%
a = 2

#%% [markdown]
# And they maintain the program state, so I can do this:

#%%
print(a)

#%% [markdown]
# I can even edit previous statements and run code from any cell I want!
#%% [markdown]
# # Other Useful things to know:
# 
# - Move, clear and edit the cells using the menu above
# - Name the cell by clicking on its name at the top (JupyterIntro in this case)
# - Use the file tree in another window to create new notebooks or open existing ones
# - Useful to know where these files are actually stored - `C:\Users\username\.jupyter`
# - It is not nice to try and convert these notebooks to python programs, so choose wisely when you start!
#%% [markdown]
# # Basic Python Syntax

#%%
# Comments have a # sign in front of them

# Good comments tell you WHY as well as what the code does. Compare:

age = 10

age = age + 1    # Add one to age
age = age + 1    # Add 1 to age because it is your birthday


#%%
# Blocks of code are defined using indentation, note the colon :
for i in range(10):
    print(i)
    print("Plus 1 ", i + 1)
print("Done")

#%% [markdown]
# # Packages and Modules
# - Python does the basic things you would expect from a programming language
# - If you want specific, complex things, there might be a package that does it
# - Some can be simple like random number generation
# - Some can be sophisticated like computer vision or speech recognition
# ## Install a package
# - From the command line: `pip install lib_name` or `conda install lib_name`
# - From Anaconda Navigator
# ## Use a package
# - `import` it in your Python code

#%%
import random
print(random.random())
# Use tab key for suggestions
#random.

import random
print(random.random())

#%% [markdown]
# ## Give the package a shorter name

#%%
import random as rnd
print (rnd.randrange(1,10))

# give a package a shorter name
import random as rnd
print(rnd.randrange(1, 100))

#%% [markdown]
# ## Import a class from a module

#%%
# Import a class from a module
from sklearn import linear_model as lm

#%% [markdown]
# # Get help

#%%
help(lm)


#%%
help(rnd.gauss)

#%% [markdown]
# # Where are my files?

#%%
import os
print(os.getcwd())

#%% [markdown]
# # Set the working directory in Jupyter
# 
# ## This is done BEFORE you run Jupyter, not from within the notebook
# 
# - Decide where you want your files to go. `H:/Jupyter` is a good idea
# - Create that folder (remember, `H` is your home network drive)
# - In notepad (or something) create a file with this on line 1
# `c.NotebookApp.notebook_dir = u'H:/Jupyter'`
# - Call it `jupyter_notebook_config.py` when you save it into `C:\Users\<username>\.jupyter` changing `username` to your own
# 
# ## If you do not do this, all your code will go into your roaming profile and slow things down when you log in.

#%%



