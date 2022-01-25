import csv
import heapq

class ShortestPath:

    def getinfo(self, fileName):
        file = open(fileName)
        csvreader = csv.reader(file)
        info = []
        for row in csvreader:
            info.append(row)
        file.close()
        return info

    def createSPtable(self, graphInfo):
        vertices =  {}
        for i in range(len(graphInfo)):
            for j in range(2):
                if(graphInfo[i][j] != '0'):
                    vertices[graphInfo[i][j]] = [float('inf'), '-']
                else:
                    vertices[graphInfo[i][0]] = [0, '-']
        # [print(key,':',value) for key, value in vertices.items()]
        return vertices

    def findSP(self, graphInfo, vertices, start, end):
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
        return vertices[end][0]

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

# spa = ShortestPath()

# graphInfo = spa.getinfo("graph.csv")
# start = input("What is start node: ").upper()
# end = input("What is goal node: ").upper()

# vertices = spa.createSPtable(graphInfo)
# sp = spa.findSP(graphInfo, vertices, start, end)
# path = spa.getPath(vertices, start, end)
 
# if(not(path == 'No path')):
#     print("Path from " + start + " to " + end + " is " + path + ", and have cost " + str(sp) + ".")
# else: print("No path")