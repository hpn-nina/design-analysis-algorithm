def check(string,left,right): 
    sstring=string[left:right+1]
    if sstring == sstring[::-1]:
        return 1
    return 0

def SStringpalindrome(s,index,n,lstcurr,lstall): 
    if index >= n:
        x=lstcurr.copy()
        lstall.append(x)
        return

    for i in range(index,n):
        if check(s,index,i):
            lstcurr.append(s[index:i+1])
            SStringpalindrome(s,i+1,n,lstcurr,lstall)
            lstcurr.pop()

def PrintSSPalindrome(string):
    n=len(string)
    lstcurr=[]
    lstall=[]
    SStringpalindrome(string,0,n,lstcurr,lstall)
    for i in lstall:
        for j in i:
            print(j,end=' ')
        print()
s=input()
PrintSSPalindrome(s)



