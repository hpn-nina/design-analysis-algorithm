def Findk(a,b,k,n,m):
    if k >= n: #Tim moc ben phai
        i = n-1
    else:
        i=k
    if k>=m:
        j = m-1
    else:
        j=k
    while i>=0 and j>=0: 
        if int(a[i]) > int(b[j]):
            if i+j+1 == k:
                return a[i]
            i-=1

        else:
            if i+j+1 == k:
                return b[j]
            j-=1
        if i==-1:
            while j>=0: #Dich chuyen vi tri tuong xung vs so i da dich
                if i+j+1 == k:
                    return b[j]
            j-=1
        if j ==-1:
            while i>=0: #Dich chuyen tuong ung voi so j da dich
                if i+j+1 == k:
                    return a[i]
            i-=1
            
t=int(input())
K=[]
for i in range (t):
    T=input().split()
    n=int(T[0])
    m=int(T[1])
    k=int(T[2])
    a=input().split()
    b=input().split()
    K.append(Findk(a,b,k,n,m))
for i in K:
    print(i)