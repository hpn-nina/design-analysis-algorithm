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
for i in range(t):
    T=input().split()
    n=int(T[0])
    m=int(T[1])
    a=input().split()
    b=input().split()
    k=(n+m)//2
    if (n+m)%2==1:
        K.append(Findk(a,b,k,n,m))
    else:
        k2=k-1
        k3=(int(Findk(a,b,k,n,m))+int(Findk(a,b,k2,n,m)))
        if k3%2==0:
            k3=int(k3/2)
        else:
            k3=k3/2
        K.append(k3)
for i in K:
    print(i)
