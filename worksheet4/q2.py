#!/usr/bin/python3
"""Write a list comprehension to output the AT content in % in a list of DNA sequences.
For example, sequences=["ATGC", "GGCC","AATT","GCGC"]"""

print("Given gene sequences:")
sequences=["ATGC", "GGCC","AATT","GCGC"]
print(sequences)
#list comprehension
at_amount = [((i.count('A')+i.count('T'))/len(i))*100 for i in sequences]
print("The percentage content of AT in the sequences are: " , at_amount)

#the syntax for list expression is [expression for item in iterable if condition]
#therefore though the for loop may seem to come at the end or after the operations
#the expression is simply before the for loop



#without list comprehensiom
at_content = []
for seq in sequences:
    a_count = seq.count('A')
    t_count = seq.count('T')
    percentage = (a_count + t_count) / len(seq) * 100
    at_content.append(percentage)
