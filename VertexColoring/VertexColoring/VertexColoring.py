import random
import time
def randominit(graph):
    for i in range(len(graph)):
        for j in range(i,len(graph[i]),1):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = random.randint(0,1000000000) % 2
                graph[j][i] = graph[i][j]
    for i in graph:
        count=0
        for j in i:
            if j == 1: break
            else: count +=1
        if count == len(graph): randominit(graph)

    return graph
def checkcolor(graph,color): #check if adjendent vertex have the same color
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] and color[i] == color[j]:
                return False
    return True
def printSolution(color):
    print("Solution Exists:" " Following are the assigned colors ")
    for i in range(len(color)):
        print(color[i],end=" ")

def main():
    maxnumofvertex = int(input())
    numofcolor = int(input())
    for vertex in range(3,maxnumofvertex,2):
        graph = [[0 for i in range(vertex)] for i in range(vertex)]
        color = [0 for i in range(vertex)]
        randominit(graph)
        #This is naive 
        def Naive(graph, nocolor, index, color):
            if index >= vertex:
                if checkcolor(graph,color):
                    return True
                return False
            for j in range(1,numofcolor+1):
                color[index] = j
                if Naive(graph,nocolor,index+1,color):
                    return True
                color[index] = 0
            return False
        start = time.time()
        Naive(graph, numofcolor, 0, color)
        end = time.time()
        print(vertex,numofcolor,end - start)
        color = [0 for i in range(vertex)]
        def Backtracking(graph, nocolor, color, v):
            if v == vertex:
                return True
            

if __name__ == '__main__':
    main()