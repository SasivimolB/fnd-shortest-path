import csv
import heapq
from operator import le
from re import A
def getinfo(fileName):
    file = open(fileName)
    csvreader = csv.reader(file)
    info = []
    for row in csvreader:
        info.append(row)
    file.close()
    return info
    
# fileName = input("What is graph file name: ")
# graphInfo = getinfo(fileName)
start = input("What is start node: ")
end = input("What is goal node: ")

graphInfo = getinfo("graph.csv")

vertices =  {}
for i in range(len(graphInfo)):
    for j in range(2):
        if(graphInfo[i][j] != '0'):
            vertices[graphInfo[i][j]] = [1000, '-']

# start = 'F'
vertices[start] = [0, '-']
visited = set()
pq = []
heapq.heappush(pq, (0, start))
while pq:
    oldcost, node = heapq.heappop(pq)
    visited.add(node)
    for i in range(len(graphInfo)):
        adjacentnode = ''
        if(graphInfo[i][0] == node): adjacentnode = graphInfo[i][1]
        elif(graphInfo[i][1] == node): adjacentnode = graphInfo[i][0]
        
        print(adjacentnode)

        if(adjacentnode and (not(adjacentnode == '0'))):
            if(adjacentnode in visited): continue
            else:
                newcost = (int)(graphInfo[i][2]) + oldcost
                if(vertices[adjacentnode][0] > newcost):
                    vertices[adjacentnode] = [newcost, node]
                    heapq.heappush(pq, (newcost, adjacentnode))
            
                if(adjacentnode in visited): continue
                else:
                    newcost = (int)(graphInfo[i][2]) + oldcost
                    if(vertices[adjacentnode][0] > newcost):
                        vertices[adjacentnode] = [newcost, node]
                        heapq.heappush(pq, (newcost, adjacentnode))
    # [print(key,':',value) for key, value in vertices.items()]

# end = 'C'
prevnode = end
revpath = [] 
revpath.append(end)
while revpath:
    if prevnode == start: break
    else:
        prevnode = vertices[prevnode][1]
        revpath.append(prevnode)

# print(revpath)
path = start
for i in range(len(revpath)):
    node = revpath.pop()
    if(not(node == start)): path = path + "->" + node
print("Path from " + start + " to " + end + " is " + path + ", and have cost " + str(vertices[end][0]) + ".")
    
