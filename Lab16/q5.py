#a script to print the first half of a string, S.
S = input("Enter a string: ")
print(S[:len(S)//2])


#this too can be solved uing a for loop
S = input("Enter a string: ")
half = len(S) // 2

for i in range(half):
    print(S[i], end="")
print()
