#  # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

 
#first one we did
nurko= Graph(6) 
nurko.graph =[[0, 1, 2, 0, 0, 0],
               [1, 0, 0, 0, 3, 0],
               [2, 3, 0, 1, 4, 0],
               [0, 0, 1, 0, 1, 0],
               [0, 3, 4, 1, 0, 2],
               [0, 0, 0, 0, 2, 0]]

nurko.dijkstra(0)  


#second one  we did
nur= Graph(6)
nur.graph = [[0 , 2, 0, 4, 1, 0],
             [2 , 0, 2, 1, 0, 0],
             [0 , 2, 0, 3, 4, 1],
             [4 , 1, 3, 0, 1, 0],
             [1 , 0, 4, 1, 0, 1],
             [0 , 0, 1, 0, 1, 0]]

nur.dijkstra(0)
