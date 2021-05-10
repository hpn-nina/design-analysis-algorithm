from itertools import product 
class Solution:
    def exist(self, board, word):
        def dfs(ind, i, j):
            if self.Found: return        #neu word duoc tim thay thi quay ve

            if ind == k:
                self.Found = True                #Neu nhu so ky tu trong word bang so ky tu duoc tim thay thi tra ve True
                return 

            if i < 0 or i >= m or j < 0 or j >= n: return #Neu nhu di ra khoi bang thi quay ve truoc do
            tmp = board[i][j]
            if tmp != word[ind]: return #Neu nhu tai vi tri do khong phai tu tai ind thi quay lai

            board[i][j] = "#"
            for x, y in [[0,-1], [0,1], [1,0], [-1,0],[1,-1],[1,1],[-1,1],[-1,-1]]: #Kiem tra 8 vi tri xung quanh no
                dfs(ind + 1, i+x, j+y)
            board[i][j] = tmp
        
        self.Found = False
        m, n, k = len(board), len(board[0]), len(word)
        
        for i, j in product(range(m), range(n)):
            if self.Found: return True          #early stop if word is found
            dfs(0, i, j)
        return self.Found

word=input()
board=[]
lst=[]
while True:
    i=input()
    if i != '.':
        if i != '':
            for j in i:
                lst.append(j)
            x=lst.copy()
            board.append(x)
    else:
        break
    lst.clear()
solve=Solution()
if solve.exist(board,word):
    print('true')
else:
    print('false')
