class Hamiltoniano:
    def __init__(self, graph):
        self.nodeStart = ()
        self.graph = graph
        self.pathsHamilton = []
        self.paths = []

    def getRelations(self, node):
        relations = []
        for edge in self.graph.edges:
            if edge.nodeStart == node:
                relations.append(edge.nodeEnd)
            else:
                if edge.nodeEnd == node:
                    relations.append(edge.nodeStart)
        return relations

    def runPath(self, path):
        relations = self.getRelations(path[-1])
        for relation in relations:
            if not relation in path:
                newPath = path.copy()
                newPath.append(relation)
                self.paths.append(newPath)
        
    def testPaths(self):
        self.pathsHamilton.clear()
        self.paths.clear()
        self.paths.append([self.nodeStart])
        while True:
            numPaths = 0
            for path in self.paths:
                if len(path) < int(len(self.graph.nodes)/2)+1:
                    self.runPath(path)
                    self.paths.remove(path)
                else: numPaths += 1
            if numPaths >= len(self.paths): break

    def oddPaths(self,path):
        relations = self.getRelations(path[-1])
        newPaths = []
        for relation in relations:
            if not relation in path:
                newPath = path.copy()
                newPath.append(relation)
                newPaths.append(newPath)
        return newPaths

    def comparePath(self):
        for i in range(1,len(self.paths)):
            if self.paths[0][-1] == self.paths[i][-1]:
                state = True
                for j in range(1,len(self.paths[0])-1):
                    if self.paths[0][j] in self.paths[i]:
                        state = False
                        break
                if state:
                    path = self.paths[0].copy()
                    [path.append(self.paths[i][k]) for k in reversed(range(len(self.paths[i])-1))]
                    self.pathsHamilton.append(path)
        self.paths.pop(0)
    
    def compareOddPath(self):
        paths = self.oddPaths(self.paths[0])
        for path in paths: 
            for i in range(1,len(self.paths)):
                if path[-1] == self.paths[i][-1]:
                    state = True
                    for j in range(1,len(path)-1):
                        if path[j] in self.paths[i]:
                            state = False
                            break
                    if state:
                        path = path.copy()
                        [path.append(self.paths[i][k]) for k in reversed(range(len(self.paths[i])-1))]
                        self.pathsHamilton.append(path)
        self.paths.pop(0)

    def test(self, nodeStart):
        self.nodeStart = nodeStart
        self.testPaths()
        while len(self.paths) > 0:
            if len(self.graph.nodes)%2 != 0:
                self.compareOddPath()
            else: self.comparePath()
        if len(self.pathsHamilton) > 0: return self.pathsHamilton
        else: return False