import csv
import heapq

def getinfo(fileName):
    file = open(fileName)
    csvreader = csv.reader(file)
    info = []
    for row in csvreader:
        info.append(row)
    file.close()
    return info

def createSPtable(graphInfo):
    vertices =  {}
    for i in range(len(graphInfo)):
        for j in range(2):
            if(graphInfo[i][j] != '0'):
                vertices[graphInfo[i][j]] = [float('inf'), '-']
            else:
                vertices[graphInfo[i][0]] = [0, '-']
    # [print(key,':',value) for key, value in vertices.items()]
    return vertices

def findSP(graphInfo, vertices, start):
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

            if(adjacentnode and (not(adjacentnode == '0'))):
                if(adjacentnode in visited): continue
                else:
                    newcost = (int)(graphInfo[i][2]) + oldcost
                    if(vertices[adjacentnode][0] > newcost):
                        vertices[adjacentnode] = [newcost, node]
                        heapq.heappush(pq, (newcost, adjacentnode))
        # [print(key,':',value) for key, value in vertices.items()]
    return vertices

def getPath(vertices, start, end):
    prevnode = end
    revpath = [] 
    revpath.append(end)
    while not(prevnode == start):
        if not(vertices[prevnode][1] == '-'):
            prevnode = vertices[prevnode][1]
            revpath.append(prevnode)
        else: revpath = []

    if(revpath):
        path = start
        for i in range(len(revpath)):
            node = revpath.pop()
            if(not(node == start)): path = path + "->" + node
        return path
    else:
        return("No path")

def getSP(vertices, end):
    return vertices[end][0]

    
# fileName = input("What is graph file name: ")
# graphInfo = getinfo(fileName)
graphInfo = getinfo("graph.csv")
start = input("What is start node: ").upper()
end = input("What is goal node: ").upper()

vertices = createSPtable(graphInfo)
if (not(start in vertices) or not(end in vertices)):
    print("No path")
elif ((start == end) and ((start in vertices) or (end in vertices))): 
    print("Path from " + start + " to " + end + " is " + start +"->" + end + ", and have cost 0.")
elif ((vertices[start] == [0, '-']) or (vertices[end] == [0, '-'])):
    print("No path")
else:
    shortestpath = findSP(graphInfo, vertices, start)
    path = getPath(vertices, start, end)

    if(not(path == 'No path')):
        sp = vertices[end][0]
        print("Path from " + start + " to " + end + " is " + path + ", and have cost " + str(sp) + ".")
    else:
        print("No path")