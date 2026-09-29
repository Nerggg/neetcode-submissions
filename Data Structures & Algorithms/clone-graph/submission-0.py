class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        neighbors = [node]
        visited = set()
        d = {}

        # creating the nodes
        while neighbors:
            for i in range(len(neighbors)):
                curr_node = neighbors.pop()
                if curr_node.val not in visited:
                    # print(curr_node.val)
                    d[curr_node] = Node(curr_node.val)
                    visited.add(curr_node.val)

                neighbors = curr_node.neighbors

        # inserting the neighbors
        neighbors = [node]
        visited = set()

        while neighbors:
            for i in range(len(neighbors)):
                curr_node = neighbors.pop()

                if curr_node.val not in visited:
                    for n in curr_node.neighbors:
                        d[curr_node].neighbors.append(d[n])

                    visited.add(curr_node.val)

                neighbors = curr_node.neighbors

        return d[node]

