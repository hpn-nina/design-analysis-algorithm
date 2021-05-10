state = int(input())
x = []
O = {}
ttcollege = 0
memoi = memoi = [0 for i in range(state)]
for i in range(state):
    temp = input().split()
    temp[1],temp[2] = int(temp[1]),int(temp[2])
    ttcollege += temp[1] 
    temp = [temp[0],temp[1],temp[2]]
    x.append(temp)

def dandc(x,z,n):#z la so phieu dai cu tri da thang, n la so bang da kiem phieu xong
    if z >= ttcollege//2 + 1: #Neu nhu da kiem phieu xong thi ngung
        return 0 #Khong can thang them phieu nao nua
    if n == len(x):
        return float('inf')
    return min(dandc(x,z+x[n][1],n+1)+(x[n][2]//2+1),dandc(x,z,n+1))

def dp(x,z,n,memoi,O):
    if z >= ttcollege//2 + 1: #Neu nhu da kiem phieu xong thi ngung
        return 0 #Khong can thang them phieu nao nua
    if n == len(x):
        return float('inf')
    memoi[n] = min(dp(x,z+x[n][1],n+1,memoi,O)+(x[n][2]//2+1),dp(x,z,n+1,memoi,O))
    return memoi[n]

def bottomup(x,z,n,memoi,O):
    '''Bottom up co y tuong la lam tu duoi len, vi the chung ta phai tinh duoc '''
    if z >= ttcollege//2 + 1: #Neu nhu da kiem phieu xong thi ngung
        return 0 #Khong can thang them phieu nao nua
    for i in range(0,state):
        for j in range(0,state):
            if i == 0:
                memoi[i][j] = (x[j][1],x[j][2] // 2 + 1) 
            else:
                for temp in range(i):
                    if temp + j < state:
                        memoi[i][j] = (memoi[i][j][0] + memoi[i][temp+j][0],memoi[i][j][1] +memoi[i][temp + j][1])
                    else: 
                        memoi[i][j] = (memoi[i][j][0] + memoi[i][j-temp][0],memoi[i][j][1] + memoi[i][j-temp][1])
    mini = float('inf')
    for i in range(0,state-1):
        mini = min(memoi[state-1][i],memoi[state-1][i+1])
    return mini
def sum_elect_vote(arr):
    sum = 0
    for i in arr:
        sum += i[1]
    return sum

def dp22(arr):
    require = sum_elect_vote(arr) // 2 + 1
    max_ele = max([a[1] for a in arr])
    memoi = [2*[0] for i in range(require + max_ele)]

    for index in range(-1, len(arr)):
        for elect_vote in range(0,require + 2):
            if elect_vote <= 0: memoi[elect_vote][index%2] = 0
            elif index < 0:
                memoi[elect_vote][index % 2] = float('inf')
            else: 
                win = memoi[elect_vote - arr[index][1]][(index - 1) % 2]
                lose = memoi[elect_vote][index % 2] 
                memoi[elect_vote][index % 2]= min(win,lose)
    return memoi[require][(len(arr) - 1) % 2]

print(dp22(x))








