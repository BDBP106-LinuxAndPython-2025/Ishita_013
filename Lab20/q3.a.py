# Q3_a
""" (a) Create a simple text file containing the following string matrix, and save it as
‘stringmatrix.dat’. This should be saved as a separate program called ”Q3 a.py”.
(Hint: For those aware of ascii values for alphabets and know how to use them, the
ascii value of ‘A’ is 65, and one can get the alphabet string by calling chr(65).)
A B C D
E F G H
I J K L"""
f = open("stringmatrix.dat", "w")   # Manually open the file
ascii_code = 65                     # ASCII code for 'A'
for row in range(3):                # 3 rows
    elements = []
    for col in range(4):            # 4 columns
        elements.append(chr(ascii_code))
        ascii_code += 1
    f.write(' '.join(elements) + "\n")
f.close()                           # Manually close the file
