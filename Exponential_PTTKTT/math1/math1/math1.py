from decimal import *
import math

c=1000000007

def power(a,b):
    
    if b > 1:
        if b%2 == 0:
            return ((power(a,b/2))**2)%c
        else:
            return (((power(a,(b-1)/2)%c)**2)*(a%c))%c
    elif b == 1:
        return a
    elif b == 0:
        return 0

def main():
    n=input()
    n=n.split()
    #print((int(n[0])**int(n[1]) )%c)
    print(power(int(n[0]),int(n[1])))

main()
