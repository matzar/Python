# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # University of Stirling
# 
# # ITNPBD2, Representing and Manipulating Data
# 
# # Assignment 2019
# 
# # An analysis of the book, Around the World in 80 Days by Jules Verne
# 
# This notebook forms the assignment instructions and submission document of the assignment for ITNPBD2 in 2019. Read the instructions carefully and enter code into the cells as indicated.
# 
# You will need to download the text of the book from Canvas - it is in the same place as this file, and called aroundTW80Days.txt.
# 
# Rename this file to be xxxxxx_BD2 where xxxxxx is your student number, then type your code into the boxes provided. Each question is given in a markdown call, and there is an empty box beneath each one where you enter your answer. These boxes should contain 2 things:
# 
# - **The code that performs the required task**
# - **Comments that explain your code**
# 
# Marks are given for both code (70%) and style and comments (30%). If you cannot get the code to work properly, you will still get some marks for correct comments. The marks available for each question are given in square brackets in each title.
# %% [markdown]
# # Submission and Other Notes
# 
# - Submit your notebook to canvas when it is complete
# - Make sure the version you submit contains the results of running every cell. The output should be visible without the need to run the code again
# 
# ## Plagiarism
# 
# Plagiarism is presenting somebody else’s work as your own. Plagiarism is a form of academic misconduct and is taken very seriously by the University. Students found to have plagiarised work can have marks deducted and, in serious cases, even be expelled from the University. Do not submit any work that is not entirely your own. 
# 
# The University’s full guidance on academic misconduct can be found here:
# 
# http://stir.ac.uk/1x0
# 
# %% [markdown]
# ## 1) Open the file `aroundTW80Days.txt` and read its contents into a string [3]
# 
# 
# 1. Print the number of characters (letters, etc) in the whole book
# 2. Split the book into a Python list containing all the words of the book in order. At this stage, use string splitting, not a more fancy library like `nltk`. Call this variable `book_list`
# 3. Print the number of words in the book
# 4. Print the first 10 words of the book. It should look like this:
# 
# `['The', 'Project', 'Gutenberg', 'EBook', 'of', 'Around', 'the', 'World', 'in', '80', 'Days,']`

# %%
import random
import string
# import re
# import numpy as np
# from matplotlib import pyplot as plt
# %matplotlib inline

# Answer 1
# read the book into a string, use 'r' to prevent reading of special characters in the file name
# and replace new line ('\n') characters with a white space
data = open(r"aroundTW80Days.txt", "r").read().replace('\n',' ')

# Clean the data
# Split the book into words
book_words = data.split()

# create new list, from book_list, with no punctuation, called book_no_punc
book_no_punc = list()
for word in book_words:
    book_no_punc.append(word.strip(string.punctuation))

# 1. Number of characters in the book
print("Number of characters in the book:", len(data))
# 2. Split the book into a sorted list
book_list = sorted(list(book_words))
rnd = random.randint(100, 109)
print("Random sample from the sorted book:", book_list[rnd:rnd+5])
# 3. Number of words in the book
print("Number of words in the book:", len(book_words))
# 4. The first 10 words of the book
print("The first 10 words from the book:", book_words[0:10])

# %% [markdown]
# ## 2) Now create a set containing all the unique words in the book [3]
# - Print the number of unique words it finds

# %%
# Answer 2
# Set stores values only once, so we're going to convert the list containing
# all the words in the book into a set, hence getting all the unique words
# but first we need to get rid of all the punctuation signs so we don't 
# count, e.g., "Francisco?" and "Francisco" as two unique words

book_no_punc = list()
# create new list, from book_list, with no punctuation, called book_no_punc
for word in book_words:
    book_no_punc.append(word.strip(string.punctuation))

# convert book_unique list into a set to obtain the unique values
book_unique = set(book_no_punc)
print(book_unique)

# %% [markdown]
# ## 3) Build a Dictionary of the words used in the book [3]
# - Build a Python dictionary (`dict`) in which the keys are the unique words in the book and the values are dictionary objects with fields `length` for word length and `freq` for frequency, e.g.:
# 
# `{'the': {'length': 3, 'freq': 4303}}`
# 

# %%
# Answer 3 
book_dict = dict()

# !!! WARNING !!! - long execution! Only use if you need the whole dictionary in the memory, otherwise
# use the generator version instead

# create a dictionary of words with words as the key and a tuple with its length and frequency
# for word in book_no_punc:
#     book_dict.update({word: (len(word), book_no_punc.count(word))})
# print(book_dict)

# %%
# generator version of the same dictionary
gen_book_dic = (book_dict.update({word: (len(word), book_no_punc.count(word))}) for word in book_no_punc)
# print(gen_book_dic)

# %% [markdown]
# ## 4) Use the dictionary that you created above to find the most commonly used word in the book [3]
# - Print the word and the number of times it appeared in the book

# %%
# Answer 4
# We're using the book_no_punc list because we don't want to count
# "Francisco?" and "Francisco" twice and get two unique keys and values
print(max(book_no_punc, key=lambda x: book_no_punc[1]))

# %% [markdown]
# ## 5) Write a generator function to produce each word and its length each time it yields a value [6]
# 
# - The function should accept a single argument: the list of words in the book
# - It should yield a tuple (word, word_len)
# - Call the function to create a generator but do not iterate over it at this stage

# %%
# Answer 5
# generator expression which yields a tuple of a word and its length
wordLenghtGenerator = ((word, len(word)) for word in book_no_punc)

# %% [markdown]
# ## 6) Use a comprehension over the generator you just made to list all the words with 9 letters [6]
# 
# - Print all those words
# - Extra points if each word is selected only once
    
# %%
# Answer 6

# generator expression which yields a tuple of a word of length 9 and its length, which is 9
wordLenghtGenerator = ((word, len(word)) for word in book_no_punc if len(word) == 9)

# printing words of lenght 9 using the generator expression
for word in wordLenghtGenerator:
    print(word)

# printing words of lenght 9 only once using the generator expression
seen_before = list()

for word in wordLenghtGenerator:
    if word not in seen_before:
        seen_before.append(word)

for word in seen_before:
    print(word)

# display(seen_before)

# %% [markdown]
# ## 7) Now iterate over your original list of words, `book_list` and find all the words with more than 14 letters, which do not contain any of these characters: [6]
# 
# `. - \ /`

# %%
# Answer 7
# generator to find words with 14 letters or more but without these special characaters `. - \ /` in them
fourteeen_letter = (word for word in book_no_punc if len(word) >= 14
    for c in word 
        if '-' not in word 
        if '.' not in word
        if '\\' not in word
        if '/' not in word)

for i in fourteeen_letter:
    print(i)

# %% [markdown]
# ## 8) Split the book into a list of chapters [6]
#  
#  - This should be a list of strings
#  - Hint - split on the word 'Chapter'
#  - Call the list `chapter_list`
#  

# %%
# This section answers Question 8 but it will also prepare the data to answer questions: 9, 10, 11, 12

# these lists will become our 2D tables of:
# this will contain 'Chapter N' and its 'Description'
table_of_contents = list()
# this will contain 'Chapter N' and its 'Content'
chapters_and_content = list()

# here we create our 2d tables
# we're iterating through all the words in the book using 'book_words' list
i = 0
while i < len(book_words):
    # Keep iterating until you encounter word "Chapter".
    # This means many things:
    if "Chapter" in book_words[i]:
        # Flush temporary holder lists to prepare them for the next chapters
        chapter_tag_holder = list()
        chapter_desc_holder = list()
        chapter_content_holder = list()

        # First, the next word is the chapter's number, so we save both in a list.
        chapter_tag_holder.append(book_words[i] + " " + book_words[i+1])
        # Second, the next words are all in capitals and are the chapter's description.
        j = i+2
        # We keep interating until there are no capital letters left.
        while book_words[j].isupper():
            # Save the chapter's description in a list.
            chapter_desc_holder.append(book_words[j])
            j+=1
        # Use the previous list containing the chapter's name and number, like 'Chapter I',
        # and the new list that has its description to create a 2d list of chapters and their descriptions
        table_of_contents.append([chapter_tag_holder, chapter_desc_holder])
        # Thirdly, if we keep going until we encounter the next word 'Chapter', 
        # we can get the entire chapter into a list!
        while book_words[j] != "Chapter" and j != len(book_words)-1:
            chapter_content_holder.append(book_words[j])
            j+=1
        # Use the list containing the chapter name and number and the list with its content
        # to create a 2d table of chapters and their content.
        chapters_and_content.append([chapter_tag_holder, chapter_content_holder])
        # Continue iterating from where 'j' is pointing to.
        current_word = book_words[j]
        i=j
    else:
        i+=1

# create a list of chapters
chapter_list = [table_of_contents[i][0] for i in range(len(table_of_contents))]
display(chapter_list)
# %% [markdown]
# ## 9) Remove the first entry from the chapter list [6]
# The first item in the chapter list is just the preface and chapter list. Copy that into a separate string variable and then remove it from the chapter list

# %%
# Answer 9
# This question was handeled differently and there was no need for removal of the first entry

# %% [markdown]
# ## 10) Now take each chapter and split it into a list of words, producing a list of lists - one for each chapter [6]

# %%
# This step was already done in the answer to Question 8
table_of_contents

# %% [markdown]
# ## 11) Print only the titles from each chapter [6]
# - Clue: The title of each chapter is written in UPPER CASE and is the first thing in each chapter. Therefore, printing words until you find one that is not upper case will print the title.

# %%
# Answer 11
for i in range(len(table_of_contents)):
    print(table_of_contents[i][1])

# %% [markdown]
# ## 12) Measure the length of each chapter and plot the values on a bar chart [9]
# - Draw a horizontal bar chart so you can read the chapter numbers down the left side
# - Set the headings to be `Chapter I` to `Chapter XXXVI` do this with code that extracts the chapter headings from the text, not by hand
# - Give the chart appropriate title and axis labels
# - Use whatever plotting library you like. Matplotlib is fine.

# %%
# Answer 12
# print chapters
for i in range(len(table_of_contents)):
    print(table_of_contents[i][0])

# %% [markdown]
# ## 13) Plot Locations Mentioned in the Book on a Map [9]
# 
# - Using a plotting package of your choice, plot the locations of all the cities mentioned in the book
# - You can use the file called `cities.txt` to look up city names and locations
# - Look at its contents to work out how to use it. The locations are given as latitude, longitude, altitude (you won't need that last one!)
# - You should then write code that searches the book for all the cities in `cities.txt`. Any that it finds should be plotted on the map
# - Here is a useful list of words that appear in the book, but are NOT to be plotted:
# 
# `['Victoria','San','Imperial','Come','San Pablo','Queenstown','Young','Lincoln','Forster','Formosa']`

# %%
# Put your answer: code and comment here

# %% [markdown]
# ## 14) NLTK Sentiment Analysis [9]
# 
# ## Use the VADER tool in the nltk library to analyse the sentiment of each chapter and plot the positive sentiment level over time on a chart

# %%
# Put your answer: code and comment here

# %% [markdown]
# ## 15) Now think of some further analysis you could do based on the text of this book [19]
# 
# It should use other data sources you find online and tell an additional story around the data. Suggested data and sources include:
# 
# - Travel and accommodation sites
# - User reviews of the book
# - Book sales data about this and other related books
# - News stories about places in the book
# - Travel times and distances
# - Pictures of places in the book
# 
# Your analysis might consider how Phileas Fogg would travel if he had to make the same journey today - what would it cost, where might he stay, what would be happening in the places he would visit? How would you aquire the data you need? Can you connect to data online using REST? Do you need to perform scraping with something like ScraPy? What other packages would you need and what would you use them for?
# 
# Write in English (not Python) about your idea including data sources, Python packages used, presentation and visualisation methods, and potential problems you can forsee. 
# 
# Add some example of code that perform some of the tasks required for your full analysis. You do not have to implement the whole idea, just some illustrative parts. 
# 
# Use as many cells below as you need - both code and markdown to explain your ideas. This part is worth 19 of the marks overall.
# 

# %%



