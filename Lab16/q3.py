#a script to check if a given number, N, is prime or not
import math
N = int(input("Enter a number: "))
if N >= 1:
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")
