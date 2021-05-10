import copy
si= [(-1,0,1),(-1,1,0),(1,-1,0),(1,0,-1),(0,-1,1),(0,1,-1)]
def find_num_in_place(final:str,curr:str): 
    ind=-1
    final = final.split('.')
    curr = curr.split('.')
    for i in final[2][:len(curr[2])]:
        if i == curr[2][ind+1]:
            ind+=1
        else: break
    return ind #return ind of the max alike peg(C) with curr if not return -1
def change_peg_to_string(peg:list):
    string=''
    for i in range(3):
        for j in peg[i]:
            string+=j
        string+='.'
    return string[:-1] #return 3 pegs into string seperated by dot

def change_string_to_peg(string:str):
    peg=[[],[],[]]
    string= string.split('.')
    count=0
    for i in string:
        for j in i:
            peg[count].append(j)
        count+=1
    return peg # return at string with dot separate as row to be peg

def find_where_find_is(curr,find):
    curr = curr.split('.')
    for i in range(len(curr)):
        for j in range(len(curr[i])):
            if curr[i][j] == str(find):
                return i,j
def pickpeg(peg,row_find):
    #Neu ton tai mot cot bi trong thi sao
    if len(peg[row_find - 1]) == 0:
        if row_find == 0: return 2
        return row_find - 1
    if len(peg[row_find - 2]) == 0:
        if row_find == 1: return 2
        if row_find == 0: return 1
        return 0
    #Xet cho nho hon de quang, so sanh cai nao 
    tmp1 = int(peg[row_find - 1][-1]) - int(peg[row_find][-1])
    tmp2 = int(peg[row_find - 2][-1]) - int(peg[row_find][-1])

    if abs(tmp1) > abs(tmp2): #khoang cach gan hon nhung neu lon hon thi khong lay
        if tmp2 < 0:
            if row_find - 2 < 0:
                return 3 + row_find -2 
            return row_find - 2
        if tmp1 < 0:
            if row_find - 1 < 0:
                return 3 + row_find -1
            return row_find - 1
        if row_find - 2 < 0:
            return 3 + row_find -2 
        return row_find - 2
    else:
        if tmp1 < 0:
            if row_find - 1 < 0:
                return 3 + row_find -1
            return row_find - 1
        if tmp2 < 0:
            if row_find - 2 < 0:
                return 3 + row_find -2 
            return row_find - 2
        if row_find - 1 < 0:
            return 3 + row_find -1
        return row_find - 1

def checkadjacent(pegs):
    if len(pegs[0]) != 0 and len(pegs[1]) !=0:
        if abs(int(pegs[0][-1]) - int(pegs[1][-1])) == 1:
            if int(pegs[0][-1]) > int(pegs[1][-1]): return 0,1
            return 1,0
    if len(pegs[1]) != 0 and len(pegs[2]) !=0:
        if abs(int(pegs[1][-1]) - int(pegs[2][-1])) == 1:
            if int(pegs[1][-1]) > int(pegs[2][-1]): return 1,2
            return 2,1
    if len(pegs[0]) != 0 and len(pegs[2]) !=0:
        if abs(int(pegs[0][-1]) - int(pegs[2][-1])) == 1:
            if int(pegs[0][-1]) > int(pegs[2][-1]): return 0,2
            return 2,0
    return None

def backtracking(pattern:list,curr:str,max_disk:int,final:str):
    if final == curr: 
        Print(pattern)
        return True #If the final stage is the same to curr one, we have found the way

    pegs = change_string_to_peg(curr)
    similar_to_ind = find_num_in_place(final,curr) #La moc 

    #Now we need to create a list of step to iterate 
    if similar_to_ind == -1:
        find = max_disk -1
    else:
        find = max_disk - 1 - similar_to_ind - 1 #Tim duoc dia so dang con thieu
    row_find,ind_find = find_where_find_is(curr,fin)
    

    if len(pegs[row_find]) != 1:
        times_pop = len(pegs[row_find]) - ind_find - 1
    else:
        times_pop = 0

    #Rang moi find dat len tam nao do, tao thanh mot cot trong sau do quang thu tu hai cot kia vao
    #Bay gio la van moi ra het cai hang cua find trc da, trong luc moi thi quang qua cot ma co so gan no nhat
    #Sau do moi luon cai kia quang len dau cua mot trong hai cot gan no, sau do moi sach mot cot
    #Sau khi moi sach mot cot thi tinh tong luong can moi de nhet find vao vi tri can thiet, quang lan luot hai cot sang cho toi khi find thi quang cot 2
    while times_pop > 0:
        pegs[pickpeg(pegs,row_find)].append(pegs[row_find].pop())
        pattern.append(change_peg_to_string(pegs))
        times_pop -= 1 #Da don toi cho cua find

    #find se quang qua 1 trong hai cot kia 
    if pegs[row_find][-1] == str(find) and similar_to_ind + 1 == len(pegs[2]): #neu nhu no o tren dau san thi cu quang qua thoi
        pegs[2].append(pegs[row_find].pop())
        pattern.append(change_peg_to_string(pegs))
        if backtracking(pattern,change_peg_to_string(pegs),max_disk,final): return True

    tmp = pickpeg(pegs,row_find) #Cot dang chua find
    #Neu ma lo chon cot 2, thi phai chon cot khac cot cu va khac 2
    pegs[tmp].append(pegs[row_find].pop()) #da lay find nhet vao mot trong hai cot kia
    pattern.append(change_peg_to_string(pegs))

    #So sanh giua hai cot 0 va 1, cot nao ngan hon thi lam trong
    peg_empty , peg_fill = 0,1
    if len(pegs[0]) > len(pegs[1]): peg_empty,peg_fill = 1,0
    if tmp == peg_empty: tmp = peg_fill

    while len(pegs[peg_empty]) > 0: 
        if len(pegs[2]) != 0 and len(pegs[peg_empty]) == 1:
            if pegs[peg_empty][-1] < pegs[peg_fill][-1] and pegs[peg_empty][-1] < pegs[2][-1]: break
        pegs[pickpeg(pegs,peg_empty)].append(pegs[peg_empty].pop())
        pattern.append(change_peg_to_string(pegs)) #Da lam trong mot cot

    #Bay gio, mot cot da trong, bat dau xet so phan tu quang vao
    
    #So phan tu can quang o cot khong trong 1 or 0
    row_find = tmp
    if row_find == 2: #Se bi remove chung
        #Se phai xet quang o ca hai cot
        #Xet tren dinh, vi find se la lon nhat
        while pegs[2][-1] != str(find):
            if int(pegs[2][-1]) < int(pegs[peg_fill][-1]):
                pegs[peg_empty].append(pegs[2].pop())
                pattern.append(change_peg_to_string(pegs))
            else:
                pegs[peg_empty].append(pegs[peg_fill].pop())
                pattern.append(change_peg_to_string(pegs))
        #find da o tren dinh
        while similar_to_ind != len(pegs[2]) - 1: #Van con phan tu duoi find khong thuoc chain
            #Neu nhu thay find thi chuyen qua cot nhieu phan tu hon hoac gan hon
                if pegs[2][-1] == str(find):
                    if len(pegs[1]) ==0:
                        pegs[0].append(pegs[2].pop())
                        pattern.append(change_peg_to_string(pegs))
                    elif len(pegs[0]) ==0:
                        pegs[1].append(pegs[2].pop())
                        pattern.append(change_peg_to_string(pegs))
                pegs[pickpeg(pegs,2)].append(pegs[2].pop())
                pattern.append(change_peg_to_string(pegs))
        #Lua tren dinh hai cot kia
        if pegs[peg_empty][-1] > pegs[peg_fill][-1]:
            pegs[2].append(pegs[peg_empty].pop())
        else:
            pegs[2].append(pegs[peg_fill].pop())
        pattern.append(change_peg_to_string(pegs))
    else: #Neu nhu find nam trong cot 1 or 0
        times_remove_toadd = len(pegs[2]) - 1 - similar_to_ind #So phan tu can quang o cot 2

        while times_remove_toadd > 0:
            pegs[peg_empty].append(pegs[2].pop())
            pattern.append(change_peg_to_string(pegs))
            times_remove_toadd-=1 #bay gio cot hai da trong cho de add find
        
        if row_find == 0: to_be_add = 1
        else: to_be_add = 0 
        while pegs[row_find][-1] != str(find):
            pegs[to_be_add].append(pegs[row_find].pop())
            pattern.append(change_peg_to_string(pegs))

        pegs[2].append(pegs[row_find].pop())
        pattern.append(change_peg_to_string(pegs))

    if backtracking(pattern,change_peg_to_string(pegs),max_disk,final): return True


def Print(pattern):
    for i in pattern:
            i=i.split('.')
            for j in i:
                for k in j:
                    print(k,end=' ')
                print()
            print('#')

def main():
    #Process input of three peg enter in 3 row
    peg=[]
    for i in range(3):
        row=[str(i) for i in input().split()]
        peg.append(row)

    #Create final stage
    final=[[],[],[]]
    for i in range(len(peg[0]) + len(peg[1]) + len(peg[2]) - 1,-1,-1):
        final[2].append(str(i))
    final = change_peg_to_string(final)

    pattern=[change_peg_to_string(peg)] #This is a list of string which will contain all the step

    backtracking(pattern,change_peg_to_string(peg),len(peg[0]) + len(peg[1]) + len(peg[2]),final)

if __name__ == '__main__':
    main()