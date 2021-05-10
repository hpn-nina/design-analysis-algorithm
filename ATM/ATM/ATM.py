C = (50, 20, 10, 5, 2)
def Fbottom(X):
    memmoi = (X+51) * [0]
    for i in range(2,X+1):
        if i in C:
            memmoi[i] = 1
        else:
            B = [memmoi[i-x] for x in C]
            B = [j for j in B if j > 0]
            if len(B) == 0:
                memmoi[i] = 0
            else:
                memmoi[i] = 1+ min(B)
        pass
    return memmoi[X]

X = int(input())
X = X//10000
print(Fbottom(X))
