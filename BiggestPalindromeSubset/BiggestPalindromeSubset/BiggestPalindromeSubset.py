def symmetry(s):
    a = [[0 for x in range(len(s))] for y in range(len(s))] #Tao ra mot mang chua len(s) phtu la mang dai len(s)
    for i in range(len(s)):
        a[i][i] = 1 #Tai vi tri i trong tap i se co do dai = 1
    for i in range(1, len(s)):
        for j in range(len(s) - i):
            print(i,j)
            k = j + i
            if s[j] == s[k]:
                a[j][k] = a[j+1][k-1] + 2
            else:
                a[j][k] = max(a[j+1][k], a[j][k-1])#Doan co chieu dai i bat dau tu j co do lon cua chuoi palindrom la max bn 
            print(a)
    return a[0][-1]

s = str(input()) #Nhap chuoi
print(symmetry(s)) #Goi ham
