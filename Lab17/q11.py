#!/usr/bin/python


def magic_date(d, m, y):
    if((d * m) == (y % 100)):
        print( "is a Magic Date")
    else:
        print("is not a Magic Date")



def date20thcentury():
    for y in range(1901, 2001):   # 20th century: 1901-2000
        for m in range(1, 13):    # Months 1-12
            for d in range(1, 32): # Days 1-31
                if magic_date(d, m, y):
                    print(f"{d:02d}/{m}/{y} is a Magic Date")
                else:
                    print(f"{d:02d}/{m}/{y} is not a Magic Date")




magic_date(2,4,2008)
date20thcentury()
