import unittest
import tempfile
from git_edit import get_graph_from_file, to_edge_dict, is_edge_in_graph, add_edge, del_edge, add_node, del_node, convert_to_dot

class TestGraphFunctions(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.write(b'1,2\n3,4\n1,5\n')
        self.temp_file.close()

        self.edge_list = [[1, 2], [3, 4], [1, 5]]
        self.edge_dict = {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}

    def test_get_graph_from_file(self):
        result = get_graph_from_file(self.temp_file.name)
        self.assertEqual(result, self.edge_list)

    def test_to_edge_dict(self):
        result = to_edge_dict(self.edge_list)
        self.assertEqual(result, self.edge_dict)

    def test_is_edge_in_graph(self):
        self.assertTrue(is_edge_in_graph(self.edge_dict, [1, 2]))
        self.assertFalse(is_edge_in_graph(self.edge_dict, [2, 3]))

    def test_add_edge(self):
        result = add_edge(self.edge_dict, [2, 3])
        self.edge_dict[2].append(3)
        self.edge_dict[3] = [2]
        self.assertEqual(result, self.edge_dict)

    def test_del_edge(self):
        result = del_edge(self.edge_dict, [1, 2])
        self.edge_dict[1].remove(2)
        self.edge_dict[2].remove(1)
        self.assertEqual(result, self.edge_dict)

    def test_add_node(self):
        result = add_node(self.edge_dict, 6)
        self.edge_dict[6] = []
        self.assertEqual(result, self.edge_dict)

    def test_del_node(self):
        result = del_node(self.edge_dict, 1)
        del self.edge_dict[1]
        for edges in self.edge_dict.values():
            if 1 in edges:
                edges.remove(1)
        self.assertEqual(result, self.edge_dict)

    def test_convert_to_dot(self):
        convert_to_dot(self.temp_file.name)
        with open(self.temp_file.name + '.dot', 'r') as f:
            content = f.read()
        expected_content = 'digraph {\n1 -> 2;\n3 -> 4;\n1 -> 5;\n}\n'
        self.assertEqual(content, expected_content)

if __name__ == '__main__':
    unittest.main()