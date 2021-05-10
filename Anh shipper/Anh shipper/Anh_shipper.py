import heapq
def check(solution,currver,vertexs):
    if len(solution) == vertexs and solution[0] == currver:
        return True
    if len(solution) == vertexs and solution[0] != currver:
        return False
    for i in solution:
        if currver == i:
            return False
    return True
def backtracking(dict,weigth,solution,currvertex,finalweight,vertexs):

    if len(finalweight) != 0:
        if finalweight[0][0] < weigth:
            return False
    if solution[-1] == solution[0] and len(solution) == vertexs + 1 :
        if (weigth,solution) not in finalweight:
            heapq.heappush(finalweight, (weigth,solution))
        return True
    try:
        lst = dict[currvertex]
    except: return False
    for i in lst:
        if check(solution,i[1],vertexs) is False: continue
        backtracking(dict,weigth+i[0],solution+i[1],i[1],finalweight,vertexs)
    
    return False

#key la cac dinh, gia tri la cac gia tri co the den duoc tu dinh do
def main():
    edges, start = (i for i in input().split())
    edges=int(edges)
    pq=[]
    dict={}
    #u,i,n Tu u den i se co do dai n 
    for vertex in range(edges):
        source,des,length = [str(i) for i in input().split()]
        length = int(length)
        if dict.get(source) is None:
            dict[source] = []
        heapq.heappush(dict[source],(length,des))

    finalweigth=[]
    #No se tra ra mot cai dict voi key la dinh, value la nhung dict nho hon voi moi dict chua length
    backtracking(dict,0,start,start,finalweigth,len(dict))

    if len(finalweigth) != 0:
        min,solution = finalweigth[0][0],finalweigth[0][1]
        for i in finalweigth:
            if i[0] < min:
                min,solution = i[0],i[1]
        print(*solution)
            
if __name__ == '__main__':
    main()

