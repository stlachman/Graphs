"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if str(vertex_id) not in self.vertices:
          self.vertices[f"{vertex_id}"] = set()
        else:
          print("Duplicate vertex")

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if str(v1) not in self.vertices:
          print("Vertex does not exist")
        else:
          self.vertices[str(v1)].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        neighbors = []
        if str(vertex_id) in self.vertices:
          for node in self.vertices[str(vertex_id)]:
            neighbors.append(node)
        else:
          return []
        return neighbors

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        hash = {}
        q = Queue()
        q.enqueue(starting_vertex)
        path = ""
        while q.size() > 0:
          current_node = q.dequeue()

          #add to hash
          if str(current_node) not in hash:
            path += f"{current_node}, "
            hash[str(current_node)] = True 

            for neighbor in self.get_neighbors(current_node):
              q.enqueue(neighbor)
        print(path[:-2])

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        hash = {}
        stack = Stack()
        stack.push(starting_vertex)
        path = ""
        while stack.size() > 0:
          current_node = stack.pop()

          #add to hash
          if str(current_node) not in hash:
            path += f"{current_node}, "
            hash[str(current_node)] = True 

            for neighbor in self.get_neighbors(current_node):
              stack.push(neighbor)
        print(path[:-2])

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        hash = {}
        path = ""
        def helper(self, current_vertex):
          nonlocal path 
          hash[f"{current_vertex}"] = True
          path += f"{current_vertex}, "
          # find all unvisited neighbors
          unvisited_neighbors = [neighbor for neighbor in self.get_neighbors(current_vertex) if str(neighbor) not in hash]

          if len(unvisited_neighbors) == 0:
            return
          else: 
            # loop through unvisited neighbors and call helper
            for unvisited_neighbor in unvisited_neighbors:
              # hash[str(unvisited_neighbor)] = True
              helper(self, unvisited_neighbor)
        helper(self, starting_vertex)
        print(path[:-2])


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
