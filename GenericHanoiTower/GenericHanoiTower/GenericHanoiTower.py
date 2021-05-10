import functools 
import sys
sys.setrecursionlimit(10**6)
#maxDisk = 0
def CreatePerfectSol(inp): #Ham tra ve du lieu chuan cuoi cung
    maximum=0
    for i in inp:
        if maximum < max(i):
            maximum = max(i)
    perfect=[]
    for i in range(3):
        tmp=[]
        if i == 2:
            for j in range(maximum,-1,-1):
                tmp.append(j)
        perfect.append(tmp)
    return perfect
def check(curr,pattern,nogo):
    for x in nogo: #nogo is a list of deadroad where it has been search and can not find another way
        if functools.reduce(lambda i, j : i and j, map(lambda m, k: m == k, x, curr),True): return False
    
    for x in pattern:
        if functools.reduce(lambda i, j : i and j, map(lambda m, k: m == k, x, curr),True): return False

    return True
#Di chuyen tu A->B , A->C,B->A, B->c, C->A,c->B 


def copying(list):
    new_list=[]
    for i in list:
        tmpl=[]
        for j in i:
            tmp=j
            tmpl.append(tmp)
        new_list.append(tmpl)
    return new_list
def CreateSmartSi(curr):
    si = [[-1,1,0],[-1,0,1],[0,-1,1],[1,0,-1],[0,1,-1],[1,-1,0]]
    count=[]
    for i in range(3):
        if len(curr[i]) == 0:
            count.append(-1)
        else:
            count.append(curr[i][-1] % 2)

    empty= count.count(-1)
    one=count.count(1)
    zero=count.count(0)
    newsi=[]
    left=[]
    if empty != 0:
        find = count.index(-1)
        #Neu nhu ton tai cot de nhay len nhung la so cung dang voi i[find] thi nhay qua cot trong
        if one == 2 or zero == 2:
            for i in si:
                if i[find] == 1:
                    newsi.append(i)
                else:
                    left.append(i)
            for i in left:
                newsi.append(i)
            return newsi
        for i in si:
            if i[find] == 0:
                newsi.append(i)
            else:
                left.append(i)
        for i in left:
            newsi.append(i)
        return newsi
    if one == 2:
        find = count.index(0)
        for i in si:
            if i[find] == 1 or i[find] == -1:
                newsi.append(i)
            else:
                left.append(i)
        for i in left:
            newsi.append(i)
        return newsi
    if zero == 2:
        find = count.index(1)
        for i in si:
            if i[find] == 1 or i[find] == -1:
                newsi.append(i)
            else:
                left.append(i)
        for i in left:
            newsi.append(i)
        return newsi
    return si

def backtracking(pattern,curr,final,nogo,depth,last, maxDisk, cnt):
    
    #Neu co n-1 dia thi day tu 1->2
    #Neu co 1 dia thi day tu A->c
    #print(maxDisk)
    if cnt >=1:
        maxDisk = 350
    if curr == final and depth <=maxDisk:
        return True
    if depth > maxDisk:
        return False
    for i in CreateSmartSi(curr):

        tem=copying(curr) #Duplicate of curr
        tmp1=i.index(-1)
        tmp2=i.index(1)
            
        #tmp1 se dua dia cho tmp2
        if len(tem[tmp1]) == 0: continue
        if len(tem[tmp2]) != 0: 
            if tem[tmp1][-1] > tem[tmp2][-1]: continue
            if last == tem[tmp1][-1] and last is not None: continue

        tmp=tem[tmp1].pop()
        tem[tmp2].append(tmp)

        if check(tem,pattern,nogo):
            pattern.append(tem)
            curr=copying(tem)
            if backtracking(pattern,curr,final,nogo,depth+1,tmp, maxDisk,cnt):
                return True
            x = pattern.pop()
            nogo.append(x)
            cnt+=1
    return False

def run(inp, maxDisk):
    pattern=[inp]
    nogo=[]
    final=CreatePerfectSol(inp)
    if backtracking(pattern,inp,final,nogo,0,None, maxDisk, 0):
        for i in pattern:
            for j in range(3):
                for index in range(len(i[j])):
                    print(i[j][index],end=' ')
                print()
            print('#')



    #Se co ba hang, moi hang se nhap mot so luong dia nhat dinh
inp=[] #Mang chua cac cot
maxDisk = 0
for i in range(3): #This is for entering 3 col of the game
    inp.append(input().split())

for i in range(len(inp)):
    length=len(inp[i])
    for j in range(length):
         inp[i][j]=int(inp[i][j])
         if maxDisk < inp[i][j]:
             maxDisk = inp[i][j]
maxDisk+=1
t = 2**maxDisk-1
run(inp, t)