#!/usr/bin//env python3
#dzoyem meli armand
#addition

import sys

def add(a,b):

       return a + b

if __name__ == "__main__" :

         if len(sys.argv) > 3 :
             print("on a besoin de deux arguments")

         elif (len(sys.argv) == 3) :
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            print(add(a,b))

         else:
            print("les arguments sont inssuffissants")
            a = int(input())
            b = int(input())
            print(add(a,b))
