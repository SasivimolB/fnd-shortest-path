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
    
# fileName = input("What is graph file name: ")
# graphInfo = getinfo(fileName)
start = input("What is start node: ").upper()
end = input("What is goal node: ").upper()

graphInfo = getinfo("graph.csv")

vertices =  {}
for i in range(len(graphInfo)):
    for j in range(2):
        if(graphInfo[i][j] != '0'):
            vertices[graphInfo[i][j]] = [float('inf'), '-']
        else:
            vertices[graphInfo[i][0]] = [0, '-']

# [print(key,':',value) for key, value in vertices.items()]

if (not(start in vertices) or not(end in vertices)):
    print("No path")
elif ([0, '-'] in vertices.values()):
    print("No path")
else:
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
                
                    if(adjacentnode in visited): continue
                    else:
                        newcost = (int)(graphInfo[i][2]) + oldcost
                        if(vertices[adjacentnode][0] > newcost):
                            vertices[adjacentnode] = [newcost, node]
                            heapq.heappush(pq, (newcost, adjacentnode))
        # [print(key,':',value) for key, value in vertices.items()]

    prevnode = end
    revpath = [] 
    revpath.append(end)
    while revpath:
        if prevnode == start: break
        elif not(vertices[prevnode][1] == '-'):
            prevnode = vertices[prevnode][1]
            revpath.append(prevnode)
        else:
            revpath = []

    if(revpath):
        path = start
        for i in range(len(revpath)):
            node = revpath.pop()
            if(not(node == start)): path = path + "->" + node
        print("Path from " + start + " to " + end + " is " + path + ", and have cost " + str(vertices[end][0]) + ".")
    else:
        print("No path")
        
