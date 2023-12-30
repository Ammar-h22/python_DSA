"""
Graphs:

Graphs have vertices(nodes) and edges(connections).

We can represent graph using Adjacency matrix and Adjacency list.

Adjacency list is much more simpler and efficient than adjacency matrix.


Space complexity:
Adjacency matrix = O(|V|2)
Adjaceny list = O(|V| + |E|)

Time Complexity:
Adding a vertex: (Not connecting the edge)
Adjacency matrix = O(|V|2)
Adjaceny list = O(1)

Adding a vertex: (Connecting the edge)
Adjacency matrix = O(1)
Adjaceny list = O(1)

Removing a vertex: (Disconnecting the edge)
Adjacency matrix = O(1)
Adjaceny list = O(E)

Removing a vertex: (Removing the node)
Adjacency matrix = O(|V|2)
Adjaceny list = O(|V| + |E|)

"""
