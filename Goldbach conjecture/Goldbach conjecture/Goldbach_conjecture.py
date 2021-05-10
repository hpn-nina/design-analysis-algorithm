def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]
def interpolationSearch(arr, n, x): 
    lo = 0
    hi = (n - 1) 
   
    while lo <= hi and x >= arr[lo] and x <= arr[hi]: 
        if lo == hi: 
            if arr[lo] == x:  
                return lo; 
            return -1; 
          
        pos  = lo + int(((float(hi - lo) / 
            ( arr[hi] - arr[lo])) * ( x - arr[lo]))) 
  
        if arr[pos] == x: 
            return pos 
   
        if arr[pos] < x: 
            lo = pos + 1; 
   
        else: 
            hi = pos - 1; 
      
def Goldbach(num):
    count=0
    lst=primes1(num)
    for i in range(0,len(lst)):
        j= num - lst[i]
        if j % 2 == 1:
            pos=interpolationSearch(lst,len(lst),j)
            if pos is not None:
                if pos >= i:
                    count+=1

    return count
num=int(input())
print(Goldbach(num))