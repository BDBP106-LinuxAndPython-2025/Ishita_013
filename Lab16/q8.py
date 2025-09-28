#a script to count the number of occurrences of a word, W, in a sentence,
S = input("Enter a sentence: ")
W = input("Enter the word to be counted: ")
print(S.split().count(W))
