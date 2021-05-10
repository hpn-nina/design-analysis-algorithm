def parenthesis(string,n,open,close):
    if close == 0:
        for i in string:
            print(i,end='')
        print()
        return
    else:
        if open < close:
            parenthesis(string+')',n,open,close-1)
        if open > 0:
            parenthesis(string+'(',n,open-1,close)
        
n=int(input())
str = ''
if n > 0:
    parenthesis(str,n,n,n)