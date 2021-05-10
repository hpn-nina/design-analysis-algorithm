import math
import random


def count(a):
    n=len(a)
    i=0
    count=1 #i=0
    while i<n-1:
        count+=2 #i<n-1
        j=0

        while j< n-i-1 :
            count+=3 #j<n-i-1
            
            count+=2 #if
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
                count+=4 #swap
            
            j+=1
            count+=1 #j++
        
        count+=3 #j<n-i-1
        j=0
        count+=1 #j=0
        i+=1
        count+=1 #i++
    
    count+=2 #i=n-1
    return count

def Ran_create(n):
    A=[]
    for i in range(n):
        new=random.randint(-20000,20000)
        A.append(new)
    return A

def Create_List_Arr():
    i=80
    Array=[]
    j=0
    while j > -1: #j la bien chat tao thanh mang chua k phan tu
        arr = Ran_create(i)
        a = count(arr)
        n=len(arr)
        
        sarr=[] #Tao list nho chua n va a 
        sarr.append(n)
        sarr.append(a)
        print(n,',',a)
        Array.append(sarr)
        
        i *= 1.1 # Moi i cach nhau 10%
        i=int(i)
        j+=1 #Tang them mot phan tu cho List_arr
    return Array

#Day la phan xu ly so lieu lon
def power(x):
    
    if 'e' not in x:
        return str(int(x)**2)
    else:
        x=x.split('e+')
        x[0]=int(x[0])**2
        x[1]=int(x[1])*2
        x=str(x[0])+'e+'+str(x[1])
        return x

def convert(a):
    a=a.split('e+')
    t=len(a[0])
    if t > 6:
        a[0]=a[0][:6]
        tam=t-6
        a[1]=int(a[1])+tam
        a=str(a[0])+'e+'+str(a[1])
        return a

def readcsv():
    filef=open('giaithua.csv','r')
    file=filef.readlines()
    for i in file:
        if i==0:
            break
        i=power(i)
        i=convert(i)
        print(i)

readcsv()










    

            

