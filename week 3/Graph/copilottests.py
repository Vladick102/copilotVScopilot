import unittest
import tempfile
import os
from copilot_edit import get_graph_from_file, to_edge_dict, is_edge_in_graph, add_edge, del_edge, add_node, del_node, convert_to_dot

class TestGraphFunctions(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.write(b'1,2\n3,4\n1,5\n')
        self.temp_file.close()
        self.graph = {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}

    def tearDown(self):
        os.unlink(self.temp_file.name)

    def test_get_graph_from_file(self):
        result = get_graph_from_file(self.temp_file.name)
        self.assertEqual(result, [[1, 2], [3, 4], [1, 5]])

    def test_to_edge_dict(self):
        result = to_edge_dict([[1, 2], [3, 4], [1, 5]])
        self.assertEqual(result, self.graph)

    def test_is_edge_in_graph(self):
        self.assertTrue(is_edge_in_graph(self.graph, [1, 2]))
        self.assertFalse(is_edge_in_graph(self.graph, [2, 3]))

    def test_add_edge(self):
        add_edge(self.graph, [2, 3])
        self.assertTrue(is_edge_in_graph(self.graph, [2, 3]))
        print(self.graph)
        add_edge(self.graph, [1, 2])
        self.assertEqual(self.graph[1], [2, 5])

    def test_del_edge(self):
        del_edge(self.graph, [1, 2])
        self.assertFalse(is_edge_in_graph(self.graph, [1, 2]))

    def test_add_node(self):
        add_node(self.graph, 6)
        self.assertIn(6, self.graph)

    def test_del_node(self):
        del_node(self.graph, 1)
        self.assertNotIn(1, self.graph)

    def test_convert_to_dot(self):
        dot_file = self.temp_file.name + '.dot'
        convert_to_dot(self.temp_file.name)
        self.assertTrue(os.path.exists(dot_file))
        os.unlink(dot_file)

if __name__ == '__main__':
    unittest.main()
