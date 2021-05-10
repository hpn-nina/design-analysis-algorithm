#Truoc dau cham thi phai lon hon bang 0 be hon bang 255
def check(s,index,count,string):
    tstring=string.split('.')
    if count == 1 and len(s) - len(string)+1 > 9:
        return 0
    if count == 2 and len(s) - len(string)+2 > 6:
        return 0
    if count == 3 and len(s) - len(string)+3 > 3:
        return 0
    if (count == 4 and len(s)+4 != len(string)) or (count == 4 and string[-1] == '.' and string[-2] == '.'):
        return 0
    for i in tstring:
        if len(i) > 1:
            if i[0] == '0' or int(i) > 255: 
                return 0
    return 1
def Ip_Dot(s,index,count,string,lst):
    if count == 4 and check(s,index,count,string)== 1:
        if string[0:-1] not in lst:
            lst.append(string[0:-1])
        return
    if check(s,index,count,string) == 1 and count < 4 :
        for i in range(1,4):
            Ip_Dot(s,index+i,count+1,string+s[index:index+i]+'.',lst)

s=input()
string=''
lst=[]
Ip_Dot(s,0,0,string,lst)
for i in lst:
    print(i)


