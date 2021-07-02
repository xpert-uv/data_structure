import unittest
from graph import Graph, Node

class TestGraph(unittest.TestCase):
    def test_create(self):
        self.empty_graph = Graph()
        self.assertEqual(len(self.empty_graph.nodes), 0)

    def test_add_node(self):
        self.graph = Graph()
        a = Node("A")
        b = Node("B")
        c = Node("C")
        self.assertFalse(a in self.graph.nodes)
        self.assertFalse(b in self.graph.nodes)
        self.assertFalse(c in self.graph.nodes)
        self.graph.add_node(a)
        self.graph.add_node(b)
        self.graph.add_node(c)
        self.assertTrue(a in self.graph.nodes)
        self.assertTrue(b in self.graph.nodes)
        self.assertTrue(c in self.graph.nodes)

    def test_add_nodes(self):
        self.graph = Graph()
        a = Node("A")
        b = Node("B")
        c = Node("C")
        self.assertFalse(a in self.graph.nodes)
        self.assertFalse(b in self.graph.nodes)
        self.assertFalse(c in self.graph.nodes)
        self.graph.add_nodes([a, b, c])
        self.assertTrue(a in self.graph.nodes)
        self.assertTrue(b in self.graph.nodes)
        self.assertTrue(c in self.graph.nodes)

    def test_add_edge(self):
        self.graph = Graph()
        a = Node("A")
        b = Node("B")
        c = Node("C")
        d = Node("D")
        self.graph.add_nodes([a, b, c, d])
        self.graph.add_edge(a, b)
        self.graph.add_edge(a, c)
        self.graph.add_edge(b, d)
        self.graph.add_edge(c, d)
        self.assertTrue(b in a.adjacent)
        self.assertTrue(c in a.adjacent)
        self.assertTrue(a in b.adjacent)
        self.assertTrue(d in b.adjacent)
        self.assertTrue(a in c.adjacent)
        self.assertTrue(d in c.adjacent)
        self.assertTrue(c in d.adjacent)
        self.assertTrue(b in d.adjacent)

    def test_remove_node(self):
        self.graph = Graph()
        a = Node("A")
        b = Node("B")
        c = Node("C")
        d = Node("D")
        self.graph.add_nodes([a, b, c, d])
        self.graph.add_edge(a, b)
        self.graph.add_edge(a, c)
        self.graph.add_edge(b, d)
        self.graph.add_edge(c, d)

        self.graph.remove_edge(b, a)
        self.graph.remove_edge(c, d)

        self.assertFalse(b in a.adjacent)
        self.assertFalse(d in c.adjacent)

    def test_remove_node(self):
        self.graph = Graph()
        a = Node("A")
        b = Node("B")
        c = Node("C")
        d = Node("D")
        self.graph.add_nodes([a, b, c, d])
        self.graph.add_edge(a, b)
        self.graph.add_edge(a, c)
        self.graph.add_edge(b, d)
        self.graph.add_edge(c, d)

        self.graph.remove_node(c)
        self.graph.remove_node(d)

        self.assertTrue(a in self.graph.nodes)
        self.assertTrue(b in self.graph.nodes)
        self.assertFalse(c in self.graph.nodes)
        self.assertFalse(d in self.graph.nodes)

        self.assertFalse(c in a.adjacent)
        self.assertFalse(d in b.adjacent)
        self.assertTrue(b in a.adjacent)
        self.assertTrue(b in a.adjacent)

    def test_list_dfs(self):
        self.graph = Graph()
        S = Node('S')
        P = Node('P')
        U = Node('U')
        X = Node('X')
        Q = Node('Q')
        Y = Node('Y')
        V = Node('V')
        R = Node('R')
        W = Node('W')
        T = Node('T')

        self.graph.add_nodes([S,P,U,X,Q,Y,V,R,W,T])

        self.graph.add_edge(S, P)
        self.graph.add_edge(S, U)

        self.graph.add_edge(P, X)
        self.graph.add_edge(U, X)

        self.graph.add_edge(P, Q)
        self.graph.add_edge(U, V)

        self.graph.add_edge(X, Q)
        self.graph.add_edge(X, Y)
        self.graph.add_edge(X, V)

        self.graph.add_edge(Q, R)
        self.graph.add_edge(Y, R)

        self.graph.add_edge(Y, W)
        self.graph.add_edge(V, W)

        self.graph.add_edge(R, T)
        self.graph.add_edge(W, T)

        result = ["S", "P", "X", "Y", "R", "T", "W", "V", "Q", "U"]
        self.assertEqual(len(result), 10)
        self.assertEqual(set(self.graph.list_dfs(S)), set(result))

    def test_list_bfs(self):
        self.graph = Graph()
        S = Node('S')
        P = Node('P')
        U = Node('U')
        X = Node('X')
        Q = Node('Q')
        Y = Node('Y')
        V = Node('V')
        R = Node('R')
        W = Node('W')
        T = Node('T')

        self.graph.add_nodes([S,P,U,X,Q,Y,V,R,W,T])

        self.graph.add_edge(S, P)
        self.graph.add_edge(S, U)

        self.graph.add_edge(P, X)
        self.graph.add_edge(U, X)

        self.graph.add_edge(P, Q)
        self.graph.add_edge(U, V)

        self.graph.add_edge(X, Q)
        self.graph.add_edge(X, Y)
        self.graph.add_edge(X, V)

        self.graph.add_edge(Q, R)
        self.graph.add_edge(Y, R)

        self.graph.add_edge(Y, W)
        self.graph.add_edge(V, W)

        self.graph.add_edge(R, T)
        self.graph.add_edge(W, T)

        result = ["S", "P", "U", "Q", "X", "V", "R", "Y", "W", "T"]
        self.assertEqual(len(result), 10)
        self.assertEqual(set(self.graph.list_bfs(S)), set(result))

    def test_shortest_path(self):
        self.graph = Graph()
        S = Node('S')
        P = Node('P')
        U = Node('U')
        X = Node('X')
        Q = Node('Q')
        Y = Node('Y')
        V = Node('V')
        R = Node('R')
        W = Node('W')
        T = Node('T')

        self.graph.add_nodes([S,P,U,X,Q,Y,V,R,W,T])

        self.graph.add_edge(S, P)
        self.graph.add_edge(S, U)

        self.graph.add_edge(P, X)
        self.graph.add_edge(U, X)

        self.graph.add_edge(P, Q)
        self.graph.add_edge(X, Q)
        self.graph.add_edge(X, Y)

        self.graph.add_edge(Q, R)
        self.graph.add_edge(Y, R)
        self.graph.add_edge(R, T)
        
        self.graph.add_edge(V, W)

        self.assertEqual(self.graph.shortest_path(S, R), 3)
        self.assertEqual(self.graph.shortest_path(S, V), -1)
        self.assertEqual(self.graph.shortest_path(S, T), 4)
        self.assertEqual(self.graph.shortest_path(S, S), 0)
        self.assertEqual(self.graph.shortest_path(V, W), 1)

    def test_are_connected_bfs(self):
        self.graph = Graph()
        a = Node("A")
        b = Node("B")
        c = Node("C")
        d = Node("D")
        self.graph.add_nodes([a, b, c, d])
        self.graph.add_edge(a, b)
        self.graph.add_edge(a, c)

        self.assertTrue(self.graph.are_connected_bfs(a, b))
        self.assertTrue(self.graph.are_connected_bfs(c, b))
        self.assertFalse(self.graph.are_connected_bfs(a, d))
        self.assertFalse(self.graph.are_connected_bfs(d, c))

    def test_are_connected_dfs(self):
        self.graph = Graph()
        a = Node("A")
        b = Node("B")
        c = Node("C")
        d = Node("D")
        self.graph.add_nodes([a, b, c, d])
        self.graph.add_edge(a, b)
        self.graph.add_edge(a, c)

        self.assertTrue(self.graph.are_connected_dfs(a, b))
        self.assertTrue(self.graph.are_connected_dfs(c, b))
        self.assertFalse(self.graph.are_connected_dfs(a, d))
        self.assertFalse(self.graph.are_connected_dfs(d, c))