# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
# # ITNPBD2: Representing and Manipulating Data
# ## University of Stirling
# ## Dr. Kevin Swingler
#%% [markdown]
# # Python Dictionaries
# - Data structures indexed by named keys
# - Basic structure is an unsorted list of key-value pairs
# - Stored as a hashmap for speed of access by key
# - Enclosed in `{}` braces

#%%
modules = {'ITNPBD1':'Mathematics for Big Data',
        'ITNPBD2':'Representing and Manipulating Data',
        'ITNPBD3':'Relational and Non-Relational Databases'}

print(modules)

values = {"string" : '\"This is an example of a string\"',
        'float' : '1.0', # we can use either '' or "" for both keys and values
         "integer" : "1"}

display(values)

#%% [markdown]
# ## Access a single entry by its key

#%%
print(modules['ITNPBD2'])

print(modules['ITNPBD3'])

print(values['string'])
print(values['float'])
print(values['integer'])

#%% [markdown]
# ## List all the keys and values

#%%
for mcode, description in modules.items():
    print(f"The module {mcode} is called {description}")
    
for v, w in values.items():
    print(f"Example of a '{v}' could be {w}")

#%% [markdown]
# ## Add a new entry with `[ ]`

#%%
modules['ITNPBD4'] = 'Scientific and Commercial Applications of Big Data'

values['character'] = '\'c\''

for key, value in values.items():
    print(f"values = key is {key} : value is {value}")

#%% [markdown]
# ## Loop through just the keys

#%%
for mcode in modules:
    print(mcode)
    print(modules[mcode])  # Can also use mcode to access value
        
print("\nPrint just dictionary's keys")
for key in values:
    print(key)

print("\nPrint just dictionary's values")
for v in values:
    print(values[v])
    
print("\nPrint dictionary's keys and values")    
for key in values:
    print(key, ":", values[key])

    

#%% [markdown]
# ## Nesting objects
# - Values can be any Python object
# - For example lists or dictionaries

#%%
modules['ITNPBD6'] = ['Data Mining', 'Machine Learning', 'Data Visualisation']
print(modules['ITNPBD6'])
print(modules['ITNPBD6'][0])

values['string'] = ['we\'re', 'adding', 'a', 'list', 'to', 'values', 'dictionary', 'at', 'key', 'equal', 'string']

display(values)

print("\n", values['string'][0],end = ' ')
print(values['string'][1], end = ' ')
print(values["string"][2], end = " ") # it doesn't matter if it's double or single quotes
print(values['string'][3], '\n')

print(values['string'], '\n')

for s in values['string']:
    print(s, end = ' ')


#%%
bd6_dict = {'name':'Data Analytics','topics':['Data Mining','Machine Learning','Data Visualisation'],'Lecturer':'Kevin Swingler'}
print(bd6_dict)

that_is_how_you_can_initialize_a_dictionary = {
    'bruh' : 'what\'s up',
    'well spoken bruh' : ['To', 'put', 'it', 'lightly', 'not', 'much'], # dictionary keys can have spaces!
    'dictionary_bruh' : 'I\'m a very inteligent bruh',
    'int_bruh' : 110
}

print(that_is_how_you_can_initialize_a_dictionary)

for well_spoken_bruh in that_is_how_you_can_initialize_a_dictionary['well spoken bruh']:
    print(well_spoken_bruh, end = ' ')
    
print('\n',that_is_how_you_can_initialize_a_dictionary['int_bruh'])


#%%
modules['ITNPBD6'] = bd6_dict
print(modules['ITNPBD6'])
print(modules['ITNPBD6']['Lecturer'])
print(modules['ITNPBD6']['topics'][1])

print(values['integer']) # the value under 'ingteger' key before overwriting it with a new value
values['integer'] = that_is_how_you_can_initialize_a_dictionary # overwrite the value under 'integer' key with a dictionary
print('\n',values['integer']['bruh'])
print(values['integer']['well spoken bruh'])     # print with print()
for b in values['integer']['well spoken bruh']:  # print with for loop
    print(b, end = ' ')
print('\n',values['integer']['dictionary_bruh']) # print the last key 'dictionary_bruh' from 'that_is_how_you_can_initialize_a_dictionary' dictionary

#%% [markdown]
# # JSON
# Dictionaries look a lot like JSON there are some differences:
# - JSON is just a string based data representation, but a dictionary is a data structure
# - The key in a dictionary is hashed to aid fast in memory access
# - The key in JSON must be a string. In a dictionary, it can be any hashable type
# - Single quotes in a dictionary, double quotes in JSON
# ## Main Python methods
# - `json.loads()` Produces dictionary from json string
# - `json.dumps()` Produces json string from object

#%%
import json

json_string = '{"Name":"Kevin", "Age":50}'
dict_obj = {"Name":"Kevin", "Age":50}

dict_from_string = json.loads(json_string)
string_from_dict = json.dumps(dict_obj)

print(json_string, type(json_string))
print(dict_obj, type(dict_obj))
print(dict_from_string, type(dict_from_string))
print(string_from_dict, type(string_from_dict))

import json

print('\n')

json_string = '{"name":"Mateusz", "age":28}'
dictionary_object = {"name" : "Mateusz", "age" : 28}
i = 25

dictionary_from_json_string = json.loads(json_string)
string_from_dictionary_python_object = json.dumps(dictionary_object)
i = json.dumps(i)

print('\n', i, type(i),'\n') # string created from python object using JSON

print(dictionary_object)
print(dictionary_from_json_string)
print(string_from_dictionary_python_object)
print(dictionary_from_json_string, type(dictionary_from_json_string))
print(string_from_dictionary_python_object, type(string_from_dictionary_python_object))


#%%
# This is a new test here

#%% [markdown]
# # Test title
# ## Subtitle text
# ### Sub-subtitle text
# Normal text
# - 1
# - 2
# - 3

#%%
mod_str=json.dumps(modules, indent=4)
print(mod_str)

print(values['string'][0])
print(values['integer'])
print(set(values))

print('\n\n')

mod_values = json.dumps(values, indent = 2)
print(mod_values)

#%% [markdown]
# ### To do the same with files, not strings, drop the `s`, so `dump` or `load`

#%%
# with open('/Users/mateuszzaremba/dev/Python/MovieData.json') as f:
#     movies = json.load(f)

# print(movies)

with open('/Users/mateuszzaremba/dev/Python/MovieData.json') as m:
    movie = json.load(m) # put json list array 'movie' variable

print(movie) # print movie array

#%% [markdown]
# ## Here we have loaded an array of json objects about movies
# - Let's find all the top level keys

#%%
keyset = set()
for mov in movies:
    for k in mov:
        keyset.add(k)
        
# print(keyset)
print(set())
keyset = set()
#%%
display(movies[0])

#%% [markdown]
# ## Pick out a single field

#%%
print(movies[0]['genres'])

#%% [markdown]
# ## Now pull out all the genres with a similar pattern of code:

#%%
genres = set()
# for mov in movies:
#    genres.add(mov['genres'])  # Won't work - you cannot have a set of lists
        
print(genres)

#%% [markdown]
# ## You cannot have a set of mutable lists - must convert to an imutable type, e.g. tuple
# - Discuss this for a minute or two!!

#%%
genres = set()
# for mov in movies:
#    genres.add(tuple(mov['genres']))  # Won't work - you cannot have a set of lists
        
print(genres)

#%% [markdown]
# ## Maybe that is not what we really want,
# - Try again for a list of genres

#%%
genres = set()
for mov in movies:
    for genre in mov['genres']:
        genres.add(genre)
        
print(genres)

#%% [markdown]
# ## That is more like it.
# - Something more challenging now - find the average rating by genre
# - This time we will build a list of dicts of the form `{genrename: {'num':number of examples, 'rating': av rating}}` 

#%%
genres = {}
for mov in movies:
    #print(mov['imdb'])
    for genre in mov['genres']:
        if mov['imdb']['rating'] is not None:    # Delete this first to see the problem it is fixing!
            if genre not in genres:
                genres[genre] = {'num':1, 'rating':int(mov['imdb']['rating'])}
            else:
                genres[genre]['num'] += 1
                genres[genre]['rating'] += int(mov['imdb']['rating'])
        
print(genres)
for genre in genres:
    genres[genre]['rating'] = genres[genre]['rating']/genres[genre]['num']
print(genres)

#%% [markdown]
# # Sets, lists and dicts Summary
# - You can have a list of dicts
# - You can have a list of sets
# - Both are mutable
# - You cannot have a set of mutable objects like lists or dicts
# - You can have a immutable objects like tuples

#%%
list_of_dicts = [{'a':1},{'b':2}]
list_of_dicts


#%%
list_of_sets = [set((1,2,3)),set((3,3,4))]
list_of_sets


#%%
#set_of_dicts = set(({'a':1},{'b':2}))


#%%
#set_of_lists = set(([1, 2, 4],[1,2,3]))


#%%
set_of_tuples = set(((1, 2, 4),(1,2,3)))
set_of_tuples


#%%
