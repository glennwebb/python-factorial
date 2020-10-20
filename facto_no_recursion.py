#!/usr/bin/env python3
import sys

def factorial(mynum):
    facto = 1
    for i in range(1,mynum+1):
        facto = facto*i
    return facto


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('You must pass a number to this program.')
        sys.exit(1)
    print(factorial(int(sys.argv[1])))
    
