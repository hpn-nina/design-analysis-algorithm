


t=int(input())
A=[]
for i in range(t):
    A.append(int(input()))
N=len(A)
def dandc(a):
    
    for length in range(1, N + 1): #length nam trong khoang tu 1 toi do dai cua A
        for left in range(1, N-length + 2):  #left nam trong khoang tu 1 toi do dai ban dau tru di do dai chuoi nho + them hai so 1
            right = left + length -1 #right bang phan tu trai + length - 1 de lay index
  
            # For a sub-array from indices left, right 
            # This innermost loop finds the last balloon burst 
            for last in range(left, right + 1): #Tim trai bong bop cuoi trong doan dai do
                dp[left][right] = max(dp[left][right], dp[left][last-1] + A[left-1]*A[last]*A[right + 1] + dp[last + 1][right]) 
    return(dp[1][N]) 


A.append(1)
A.insert(0,1)
dp = [[0 for x in range(N + 2)] for y in range(N + 2)]# Declare DP Array 
print(dandc(A))






