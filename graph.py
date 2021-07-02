"""
Graph class
"""
class Node():
    """
    class for graph node
    """
    def __init__(self, name):
        self.name = name
        self.adjacent = set()


class Graph():
    """
    basic graph class
    """
    def __init__(self):
        self.nodes = set()

    def add_node(self, node):
        self.nodes.add(node)

    def add_nodes(self, nodes):
        for node in nodes:
            self.nodes.add(node)

    def add_edge(self, node1, node2):
        node1.adjacent.add(node2)
        node2.adjacent.add(node1)

    def remove_edge(self, node1, node2):
        node1.adjacent.discard(node2)
        node2.adjacent.discard(node1)

    def remove_node(self, node):
        neighbors = node.adjacent
        self.nodes.discard(node)
        for neighbor in neighbors:
            neighbor.adjacent.discard(node)

    def list_dfs(self, node):
        """
        returns list of all nodes the given node is connected to, 
        depth-first pathing
        """
        arr = []
        stack = [node]
        seen = {node}
        while len(stack) > 0:
            # print("Stack:", [n.name for n in stack])
            current_node = stack.pop()
            arr.append(current_node.name)
            # print("List:", arr)
            # print("Seen:", [n.name for n in seen])

            for neighbor in current_node.adjacent:
                if neighbor not in seen:
                    stack.append(neighbor)
                    seen.add(neighbor)
        return arr

    def list_bfs(self, node):
        """
        returns list of all nodes the given node is connected to, 
        bredth-first pathing
        """
        arr = []
        queue = [node]
        seen = {node}
        while len(queue) > 0:
            current_node = queue.pop(0)
            arr.append(current_node.name)

            for neighbor in current_node.adjacent:
                if neighbor not in seen:
                    queue.append(neighbor)
                    seen.add(neighbor)
        return arr

    def shortest_path(self, start, end):
        """
        finds shortest path between two nodes
        returns -1 if no path found
        """
        queue = [(start, 0)]
        seen = {start}
        while len(queue) > 0:
            (current_node, distance) = queue.pop(0)
            if current_node == end:
                return distance

            for neighbor in current_node.adjacent:
                if neighbor not in seen:
                    queue.append((neighbor, distance + 1))
                    seen.add(neighbor)
        return -1

    def are_connected_bfs(self, node1, node2):
        """
        based on video
        returns True if two nodes are connected, false otherwise
        uses breadth-first search
        """
        queue = [node1]
        seen = {node1}
        while len(queue) > 0:
            current_node = queue.pop(0)

            if current_node == node2:
                return True

            for node in current_node.adjacent:
                if node not in seen:
                    queue.append(node)
                    seen.add(node)
        return False

    def are_connected_dfs(self, node1, node2):
        """
        based on video
        returns True if two nodes are connected, false otherwise
        uses depth-first search
        """
        stack = [node1]
        seen = {node1}
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node == node2:
                return True

            for node in current_node.adjacent:
                if node not in seen:
                    stack.append(node)
                    seen.add(node)
        return False
