# 
def bt(n:int):
    if n == 1:
        return 0
    if n == 2:
        return 0
    if n == 3:
        return 1

def main():
    n = int(input())
    dp(n)
