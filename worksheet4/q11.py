#!/usr/bin/python3
#How would you read and write binary data to a file? Illustrate with suitable programs.


# Writing binary data
f = open('binaryfile.bin', 'wb')
data = bytes([120, 3, 255, 0, 100])  # example binary data
f.write(data)
f.close()  # manually close the file

# Reading binary data
f = open('binaryfile.bin', 'rb')
content = f.read()
f.close()  # manually close the file

print(list(content))  # Output: [120, 3, 255, 0, 100]
