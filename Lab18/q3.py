#!/usr/bin/python
a = []
for i in range(1, 51):   # creates [1, 2, ..., 50]
    a.append(i)

#Create a string by joining the numbers in the above list a using the comma.
b = [",".join([str(x) for x in a])]
print(b)
# Output: '1,2,3,4,5'

#Create a string by joining the numbers in the above list a using the period.
c = [".".join([str(x) for x in a])]
print(c)

#Create a string by joining the numbers in the above list a using the ‘—’.
d = ["-".join([str(x) for x in a])]
print(d)

""" Create a new string by first creating a list of squares of the elements in a,
then listing them alongside the elements of a line by line. In other words,
we want a data set that looks like """
e = ["{} {}".format(x**2, x) for x in a]
print(e)

#Make a list of 10 people you know,
names = ['ishita badola','akshata badola','anoushka badola','anchal kumari','aisha khan','margarita kumar', ' saniya shaikh','nayonika sur', 'manu jain', 'daksh puri']
print(names)
#Convert each element in the list to upper case using list comprehension
x = [[x.upper() for x in names]]
print(x)
#Swap the first name and surname of each element in the list
y = [[" ".join(x.split()[::-1]) for x in names]]
print(y)
#Join the first name and surname in each element as ’First.Last’. Note that the first letter of the first name and first letter of the surname should be upper case.
z = [["{}.{}".format(x.split()[0].capitalize(), x.split()[1].capitalize()) for x in names]]
print(z)


#Find the longest word in this sentence using list comprehension: ”She sells sea shells that she collects from the sea floor”.
str = "”She sells sea shells that she collects from the sea floor"
w = [w for w in str.split(' ')]
maxword = max(w, key=len)
print(maxword)

#Create a list of the words that are repeated in the above sentence
words = str.split()
repeats = [w for w in set(words) if words.count(w) > 1]
print(repeats)