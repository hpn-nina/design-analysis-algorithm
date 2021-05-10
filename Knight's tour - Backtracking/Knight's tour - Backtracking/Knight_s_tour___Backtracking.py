

si1=[[1,2],[2,1],[-1,2],[2,-1],[-2,1],[-2,-1],[1,-2],[-1,-2]]
class Solution:
    def exist(self,board,bas):
        self.row,self.col,self.base = int(board[0]),int(board[1]),bas #Xem nhu chu la col
        def check(i,j):
            return i >= 0 and i < self.row and j >= 0 and j < self.col
        def dfs(path,i,j):

            if len(path) == self.row*self.col:
                return True

            for x, y in si1:
                newi=str(i + x + 1) #Hang moi(de luu lai) bang row curr + x + 1
                newj=chr(j + y + ord('a')) #Cot moi = doi thanh chu cua col curr + y + ascii 'a'
                if check(i+x,j+y):
                    new = newj+newi
                    if new in path: continue
                    path.append(new)
                    if dfs(path,i + x,j + y): return True
                    path.pop()
            return False
        
        path=[]
        path.append(self.base)
        if dfs(path,int(self.base[1])-1,ord(self.base[0])-ord('a')):
            print(*path)

def main():
    enter=input().split()
    base=input() #Se gom hai ky tu, mot chu mot so
    B=Solution()
    B.exist(enter,base)

if __name__ == '__main__':
    main()