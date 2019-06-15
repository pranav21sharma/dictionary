#!/usr/bin/env python
# coding: utf-8

# In[9]:


def translate(w):
    import json 
    from difflib import get_close_matches
    data = json.load(open("C:/Users/Nilesh/Desktop/word-dict/data.json"))
    w = w.lower()
    w1 = w.upper()
    w2 = w.title()
    if w in data:
        return data[w]
    elif w1 in data:
        return data[w1]
    elif w2 in data:
        return data[w2]
    elif len(get_close_matches(w, data.keys())) >0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn  == "Y" or yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn =="N" or yn == "n":
            return "The word doesn't exit. Please double check it."
        else:
            return "We did't understand your entry."
    else:
        return "The word doesn't exit. Please double check it."
    
word = input("Enter a word ")   
output = translate(word)
if type(output) ==list:
    for item in output:
        print(item)
else:
    print(output)
    

