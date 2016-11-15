import copy

class graph:
    def __init__(self):
        self.vertices = []
        self.edgelist = []

    def initialize(self, fname):
        f = open(fname, 'r')
        n = int(f.readline())
        for i in range(n):
            self.vertices.append(-1)
        e = int(f.readline())
        for x in range(e):
            s = f.readline().split()
            self.edgelist.append((int(s[0])-1, int(s[1])-1))

    @staticmethod
    def edge_length(vertices, e):
        u, v = e
        if (vertices[u] == -1 or vertices[v] == -1):
            return -1
        else:
            return abs(vertices[u] - vertices[v])

    @staticmethod
    def bandwidth(edgelist, vertices):
        max = 0
        for e in edgelist:
            x = graph.edge_length(vertices, e)
            if (x > max):
                max = x
        return max

    def is_solution(self):
        for v in self.vertices:
            if v == -1:
                return False
        return True



    def min_bandwidth(self, k, solution):

        if graph.bandwidth(self.edgelist,self.vertices)>= graph.bandwidth(self.edgelist,solution):
            return
        if self.is_solution():
            solution.clear()
            solution.extend(self.vertices)
            return
        for i in range(len(self.vertices)):
            if i not in self.vertices:
                self.vertices[k] = i
                graph.min_bandwidth(self,k+1,solution)
                self.vertices[k] = - 1

    def candidates(self,k,candidates,n,max):
        for e in self.edgelist:
            u, v = e
            for i in range(n):
                if k==u and self.vertices[v] != -1 and abs(i-self.vertices[v]-i)<max:
                    candidates.append(i)

                elif k==v and self.vertices[u] !=-1 and abs(self.vertices[u]-i)<max:
                    candidates.append(i)

