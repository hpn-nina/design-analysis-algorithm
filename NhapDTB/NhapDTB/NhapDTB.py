import math
def check(lst,lstan,avg):
    if len(lst) != 0:
        left=100
        avgt=0
        for i in range(len(lst)):
            left-=lstan[i]
            avgt+=(lst[i]*lstan[i])

        if len(lst) == len(lstan):
            num=(avgt%100)%10
            if num >= 5:
                avgt+=(10-num)
            avgt/=100
            if round(avgt,1) == avg:
                return 1
        else:
            x = (100*avg - avgt)/left
            if x >= -0.9 and x <= 10.9:
                return 1
    else:
        return 1
    return 0
def AVGScore(lstscore,lstan,avg,n,lstt,index):
    if index >= n and check(lstt,lstan,avg)==1 and len(lstan) == len(lstt):
           x=lstt.copy()
           lstscore.append(x)
           return
    if check(lstt,lstan,avg) == 0 and index < n and len(lstt) != 0:
        return
    for j in range(index,n):
        for i in [0.25,0.5,0.75,1,1.25,1.5,1.75,2,2.25,2.5,2.75,3,3.25,3.5,3.75,4,4.25,4.5,4.75,5,5.25,5.5,5.75,6,6.25,6.5,6.75,7,7.25,7.5,7.75,8,8.25,8.5,8.75,9,9.25,9.5,9.75,10]:
            lstt.append(i)
            AVGScore(lstscore,lstan,avg,n,lstt,j+1)
            lstt.pop()

def PrintAllAVGScore(n,lstan,avg):
    lstscore=[]
    lstt=[]
    AVGScore(lstscore,lstan,avg,n,lstt,0)
    for i in lstscore:
        for j in i:
            print(j,end=' ')
        print()
def init():
    n=int(input()) #So he so
    lstan=[] #List chua he so
    for i in range(n):
        lstan.append(int(input()))
    avg=float(input()) #Nhap diem trb
    PrintAllAVGScore(n,lstan,avg)

def main():
    init()
    
if __name__ == "__main__":
    main()