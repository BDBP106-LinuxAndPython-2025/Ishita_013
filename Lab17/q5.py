#!/usr/bin/python
#Remove all duplicate words from a given sentence using a dictionary. (Hint: Use the,set() function might be useful here.)

sent = "this is just a test but is it a test or maybe this is just lab pratice"
words = sent.split()
newsent = set(words)
finalsent = " ".join(newsent)
print(finalsent)

""" can also be done in the dictionary method
newsent = {}
for w in words:
newsent[w] = None  # The value can be anything, the key is what matters
result = ' '.join(newsent.keys())
print(result) """