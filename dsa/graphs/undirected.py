class UndirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = set()
            print(f"Vertex '{vertex}' added.")
        else:
            print(f"Vertex '{vertex}' already exists.")

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            # Remove all edges connected to this vertex
            for adjacent in list(self.graph[vertex]):
                self.graph[adjacent].remove(vertex)
            # Remove the vertex itself
            del self.graph[vertex]
            print(f"Vertex '{vertex}' removed.")
        else:
            print(f"Vertex '{vertex}' does not exist.")

    def add_edge(self, vertex1, vertex2):
          # Ensure both vertices exist in the graph
          if vertex1 not in self.graph:
              self.add_vertex(vertex1)
          if vertex2 not in self.graph:
              self.add_vertex(vertex2)

          # Add edge in both directions (undirected graph)
          if vertex2 not in self.graph[vertex1]:
              self.graph[vertex1].append(vertex2)
          if vertex1 not in self.graph[vertex2]:
              self.graph[vertex2].append(vertex1)
          print("Edge added.")

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)
            print(f"Edge between '{vertex1}' and '{vertex2}' removed.")
        else:
            print(f"Edge between '{vertex1}' and '{vertex2}' does not exist.")

    def display(self):
        if not self.graph:
            print("The graph is empty.")
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {', '.join(map(str, edges))}")

def main():
    g = UndirectedGraph()

    while True:
        print("\n1. Add Vertex")
        print("2. Remove Vertex")
        print("3. Add Edge")
        print("4. Remove Edge")
        print("5. Display Graph")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            vertex = input("Enter vertex to add: ")
            g.add_vertex(vertex)
        elif choice == '2':
            vertex = input("Enter vertex to remove: ")
            g.remove_vertex(vertex)
        elif choice == '3':
            vertex1 = input("Enter the first vertex: ")
            vertex2 = input("Enter the second vertex: ")
            g.add_edge(vertex1, vertex2)
        elif choice == '4':
            vertex1 = input("Enter the first vertex: ")
            vertex2 = input("Enter the second vertex: ")
            g.remove_edge(vertex1, vertex2)
        elif choice == '5':
            print("Graph:")
            g.display()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
