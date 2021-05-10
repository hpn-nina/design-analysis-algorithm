
def ATM(money):
    count=0
    min_to=0
    tam = int(money/10000)
    t500=0
    t200=0
    t100=0
    t50=0
    t20=0
    for a in range (0, tam//50 +1):
        for b in range (0,(tam - 50*a)// 20 + 1):
            for c in range (0, (tam - 50*a - 20*b)// 10 + 1):
                for d in range (0, (tam - 50*a - 20*b - 10*c) // 5 + 1):
                    for e in range (0, (tam - 50*a - 20*b - 10*c - 5*d) // 2 + 1):
                        if a*50 + b*20 + c*10 + d*5 + e*2 == tam:
                            count+=1
                            min_to = a + b + c + d + e
    return count,min_to
            
money=int(input())
tam=ATM(money)
print(tam[0],tam[1])