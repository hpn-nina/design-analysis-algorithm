#Trả về dict
import random 
from random import randint, choice
def RandomGenerate(n:int):
    relationships = {} #Luu cac lk da co
    for i in range(n):
        a = randint(1,n)
        b = randint(1,n)

        #Do là dict nên phải get xong rồi mới đếm
        while (sum(relationships[i].count(a) for i in relationships)) > 2:
            a = randint(1,n)
        #Đã có a để có thể kiểm tra
        if a not in relationships.keys():
          while (sum(relationships[i].count(b) for i in relationships)) > 2:
            b = randint(1,n)
        else: 
          while (sum(relationships[i].count(b) for i in relationships)) > 2 or b in relationships[a] or a == b:
            b = randint(1,n)

        if a not in relationships.keys():
          relationships[a] = [b]
        else: 
          newre = relationships.get(a)
          newre.append(b)

        if b not in relationships.keys():
          relationships[b] = [a]
        else: 
          newre = relationships.get(b)
          newre.append(a)
        
    return relationships
def CheckBacktracking(array, colors, currsub, newcolor): #Hàm kiểm tra có thể lựa chọn newcolor cho currsub hay không
    if currsub not in array.keys(): #Nếu như nó không có quan hệ nào thì chọn màu gì cũng được
        return True
    
    tocheckList = array[currsub] #list chứa những phần tử quan hệ của currsub
  
    for i in tocheckList: #Với mỗi phần tử có trong quan hệ
        if newcolor == colors[i - 1]: #Nếu màu mới bằng với màu hiện tại của một trong những môn khác thì không nhận. Lưu ý, ind màu sẽ lệch 1 so với array
            return False

    return True

def checktoOut(array,color): #Hàm kiểm tra toàn thời khóa biểu xem đã phù hợp tiêu chuẩn chưa
    if color.count(0) >= 1: return False
    for i in array:
        tocheckList = array[i]

        for j in tocheckList:
            if color[i - 1] == color[j - 1]:
                return False
    return True

import sys
def Backtracking(currsub: int, n: int, colors: list, array):

    if checktoOut(array,colors) or currsub > n:
        return True

    for color in range(1,4+1): #Có 4 màu sắc từ 1->4
        if CheckBacktracking(array, colors, currsub, color):
                colors[currsub - 1] = color
                if Backtracking(currsub + 1, n, colors, array): return True
                colors[currsub - 1] = 0

    return False
import time
for i in range(5,100000,10):
  array = {} #Array là một dictionary chứa quan hệ giữa các môn học, format {3: [4,5], 4:[3], 5: [3]} nghĩa là môn học thứ
                                    # 3 có liền kề với môn học thứ 4,5 và ngược lại. Không có trong array nghĩa là không 
                                    # liền kề
  array = RandomGenerate(i) 
  colors = [0] * i
  start = time.time()
  Backtracking(1, i, colors, array)
  end = time.time()
  print(i,end - start)