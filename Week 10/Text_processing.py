# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# <h1>ITNPDB2 Representing and Manipulating Data</h1>
# <h3>University of Stirling<br>Dr. Saemundur Haraldsson</h3>
# <h2>Text processing</h2>
# <h4>        
#     <ul>
#         <li>Natural language processing</li>
#         <ul>
#             <li>
#                 Lexical analysis (Tokenization)
#             </li>
#             <li>Natural Language Toolkit <a href="http://www.nltk.org/book/">(Useful book)</a><br>
#                 Vader -- sentiment analysis
#             </li>
#         </ul>
#     </ul>
# </h4>
# %% [markdown]
# ## Lexical analysis or Tokenization
# ### is the process of converting a string or text into tokens <br> Paragraphs -> Sentences -> Clauses  -> Words
# 
# #### Depending on the purpose we include/exclude:   
#     - punctuations (. , ; : )
#     - white space
#     - others
# 

# %%
# We read in the whole document
with open('for_lexical.txt','r') as fid:
    text = fid.read()
print(text)

# %% [markdown]
# # Paragraphs (in our text) will be delimited by 2 newline characters
# - This usually has to be checked manually

# %%
paragraphs = text.split('\n\n')
display(paragraphs)

# %% [markdown]
# ## We notice that there are a lot of extra newline characters \n in each paragraph <br> we don't need them
# - We'll use __replace__ to exclude them from our tokens 

# %%
paragraphs = [i.replace('\n',' ') for i in paragraphs]
display(paragraphs)

# %% [markdown]
# ## Sentences are usually delimited by full stops
# - and as sentences are a smaller entity than paragraphs we can work from there
# - watch out though, splitting each paragrap gives us a separate list. We'll use list comprehension to flatten the resulting list of lists

# %%
sentences = [i for j in paragraphs for i in j.split('.')]
display(sentences)

# %% [markdown]
# ## Sentences are made up of clauses
# - There are a number of grammatical rules to define a clause but we'er going to simplify it a bit for this exercise
# - Let's define a clause as anything that comes before or after the following conjunctions:
#  - __and__
#  - __or__
#  - __but__
#  - __nor__
# 
# ### Working onwards from sentences we split each into clauses
# - __Not grammatically correct__ as we're not concerned with that at the moment
# - __split__ only takes one argument but we want to split on any occurance of our conjunctions which are many
# - we can iterate through the sentences and make an overly complicated __if then else__ script
# - or we can use __re__, python's regular expression package
# - we still use list comprehension 

# %%
import re
clauses = [i for j in sentences for i in re.split(r' and | or | but | nor ',j)]
# This is very simplified regular expression
display(clauses)

# %% [markdown]
# ## And lastly we want the words
# - we could split the entire text on white spaces as in __text.split(' ')__
#  - That would give us everything but the white spaces, i.e. leaves in the punctuation
# - Simplest way is to use __re.split()__ and split on words 
#     - __\W__ is a predifined special sequence for any character that is not a word character
#     - __\s__ is white space
#     - __re.split()__ will __not__ treat consecutive separators as a single one

# %%
words = re.split(r'\W\s*|\s',text) # This will also split hyphenated words and words with Apostrophes
display(words)

# %% [markdown]
# ## Now what to do with these tokens?
# ### We can count the number of unique tokens in each token class

# %%
print("Number of paragraphs is {}, thereof unique {}".format(len(paragraphs),len(set(paragraphs))))
print("Number of sentences is {}, thereof unique {}".format(len(sentences),len(set(sentences))))
print("Number of clauses is {}, thereof unique {}".format(len(clauses),len(set(clauses))))
print("Number of words is {}, thereof unique {}".format(len(words),len(set(words))))

# %% [markdown]
# ### Let's count occurrences of each word

# %%
# We save it in a list of tuples
word_count = [(word,words.count(word)) for word in set(words)]
display(word_count)

# %% [markdown]
# ### Let's see a few of the most frequent words
# - couple of things happening in the following line
# - but only in a single function call
#  - we're using the __key__ and __reverse__ keyword arguments for sorted
#  - and only displaying the first 15 

# %%
display(sorted(word_count,key=lambda x:x[1],reverse=True)[:15])

# %% [markdown]
# <h2>
#     Tokenization is sometimes a preprocess for plagiarism detection.<br>
#     Words as tokens would not be very useful for that task.<br>
#     Clauses, sentences, and paragraphs are rather language specific ways.
# </h2>
# 
# ### A really simple* plagiarism technique would be to split into overlapping set lenght "word windows"
# - Let's try it out with every pairs of 7 words.
# - We don't need white space characters so we'll use the word list which is in the correct order already
#  - but we need to clean it a bit first
#  - there are some whitespaces.
#  - we also know that any single instance of __s__ should be part of the word before (right?)
#  - can you think of any other obvious things we should look out for as well?
# - We could use functions and tools from __itertools__ https://docs.python.org/3.7/library/itertools.html
# - Or we can make our own one-liner
# 
# *This is far from state-of-the-art, actually would probably not really work in praxis

# %%
# cleans out whitespaces:
clean_words = [i.strip() for i in words if len(i.strip())>0] 
# find the single s character:
ind_of_s = [ind for ind,w in enumerate(clean_words) if w=='s'] 
# Add the apostrophe and s:
clean_words = [word+"´s" if ind+1 in ind_of_s else word for ind,word in enumerate(clean_words) ] 
ind_of_s.reverse() # Why do you think we're reversing the index list?
# Remove the single s characters:
for ind in ind_of_s: 
    del(clean_words[ind])

# Now we'll make our list of 7-grams from the cleaned list of words:
seven_grams = [' '.join(clean_words[i:i+6]) for i in range(len(clean_words) - (6))]
display(seven_grams)

# %% [markdown]
# # NLTK
# ## Natural Language Toolkit
# - There's a package for what we were doing
# - __and so much more__

# %%
# First some imports that we'll need
import nltk
import matplotlib
import matplotlib.pyplot as plt

# %% [markdown]
# ## Tokenization

# %%
display(nltk.tokenize.sent_tokenize(text)) # sentence tokens
display(nltk.word_tokenize(text)) # word/type tokens, includes punctuation

# %% [markdown]
# ## Let's load some data that is more interesting than we had before

# %%
from nltk.book import *

# %% [markdown]
# ## The previous cell loaded a bunch of books into memory as NLTK text objects
# - They provide some interesting methods 
# - Let's explore it a bit
# %% [markdown]
# ## We can do a simple wordcount

# %%
display(len(text2))
display(len(set(text2)))
display(len(text2)/len(set(text2))) # Lexical diversity


# %%
display(text1) # What is in text1?
display(dir(text1)) # What attributes can we see?

# %% [markdown]
# ## We can search for words and their context

# %%
text2.concordance('honour')

# %% [markdown]
# ## Search for words in similar context

# %%
text2.similar('honour')

# %% [markdown]
# ## List the similar contexts of two words

# %%
text2.common_contexts(['very','monstrous'])

# %% [markdown]
# ## Visualise where words appears

# %%
fig = plt.figure(figsize=(10,10))
text2.dispersion_plot(['honour','decent','lovely'])

# %% [markdown]
# ## Frequency distribution of the 50 most frequent tokens
# FreqDist() is part of the nltk.book module

# %%
fdist = FreqDist(text2)
vocabulary = sorted(list(fdist.items()),key=lambda x:x[1],reverse=True)
display(vocabulary[:50])
plt.figure(figsize=(12,12))
fdist.plot(50)

# %% [markdown]
# ## That wouldn't tell us much about the text, what about the most infrequent words?
# - Those that only occur once
# - __hapaxes__

# %%
# How many are they?
len(fdist.hapaxes())

# %% [markdown]
# ## Okay, that's a bit too many rare words to tell us anything of importance
# ## Let's try something else
# - Do you know what we're doing here?

# %%
interesting_words = sorted([w for w in set(text2) if len(w) > 11 and fdist[w] > 7])
display(interesting_words)

# %% [markdown]
# ## Let's visualise where the words found above are in the text

# %%
plt.figure(figsize=(12,12))
text2.dispersion_plot(interesting_words)

# %% [markdown]
# ## We can also see commonly co-occurring words

# %%
text2.collocations(num=20,window_size=2)

# %% [markdown]
# # Sentiment analysis using VADER
# - Attempts to extract opinions or "feelings" from text

# %%
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

# %% [markdown]
# ## Polarity scores estimate the sentiment of text
# - __neg__: Negative sentiment between 0 and 1
# - __pos__: Positive sentiment between 0 and 1
# - __neu__: Neutral sentiment between 0 and 1
# - __compound__: Normalised sum of the three above between -1 and 1

# %%
score = analyser.polarity_scores("This is an awful sentence that I've written.")
display(score)

# %% [markdown]
# ## Let's check the sentiment for the first 100 sentences of book 2

# %%
text2_sentences = nltk.sent_tokenize(' '.join(text2))
score = analyser.polarity_scores(' '.join(text2_sentences[:100]))
display(score)


# %%
len(text2_sentences)

# %% [markdown]
# ## Can we plot how the sentiment evolves per sentence throughout the book?

# %%
scores = [analyser.polarity_scores(sent)['compound'] for sent in text2_sentences]#[0::50]]
fig = plt.figure(figsize=(12,12))
plt.plot(scores)
plt.show()


