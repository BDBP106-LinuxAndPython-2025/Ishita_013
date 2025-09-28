#a script to check if two strings are anagrams of each other . Eg. listen and silent are anagrams, gram and arm are not anagrams

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(sorted(s1) == sorted(s2))
