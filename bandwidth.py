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
            self.edgelist.append((int(s[0]) - 1, int(s[1]) - 1))

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

    def min_bandwidth(self, k, solution, max):
        if k > len(self.vertices):
            return
        candidates = []

        max = graph.bandwidth(self.edgelist, solution)
        if self.is_solution():
            solution.clear()
            solution.extend(self.vertices)
            return
        self.candidates(k, candidates, max)
        for i in range(len(candidates)):
            self.vertices[k] = candidates[i]
            graph.min_bandwidth(self, k + 1, solution, max)
            self.vertices[k] = - 1

    def candidates(self, k, candidates, max):
        for i in range(len(self.vertices)):
            candidates.append(i)
        for e in self.edgelist:
            u, v = e
            if (k != u and self.vertices[u] != -1):
                if self.vertices[u] in candidates:
                    candidates.remove(self.vertices[u])
            if (k != v and self.vertices[v] != -1):
                if self.vertices[v] in candidates:
                    candidates.remove(self.vertices[v])
            for i in range(len(self.vertices)):

                if (k == u and self.vertices[v] != -1 and abs(self.vertices[v] - i) >= max):
                    if i in candidates:
                        candidates.remove(i)

                elif (k == v and self.vertices[u] != -1 and abs(self.vertices[u] - i) >= max):
                    if i in candidates:
                        candidates.remove(i)
