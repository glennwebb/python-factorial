#!/usr/bin/env python3
import sys

def factorial(n): 
    if n <= 1: 
        return n 
    return n*factorial(n-1) 


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('You must pass a number to this program.')
        sys.exit(1)
    print(factorial(int(sys.argv[1])))
    
