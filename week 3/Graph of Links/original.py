'''Link notes'''
import re
import os
def build_graph_from_note(note_path, graph = None):
    '''
    Build graph from note.
    '''
    def find_links(file_path):
        with open(file_path, mode = 'r', encoding='utf-8') as f:
            links = re.findall(r'\[\[(.*?)\]\]', f.read())
        return links

    def make_graph(note_path, graph):
        if not graph:
            graph = {}

        note_filename = os.path.basename(note_path).split('.')[0]

        linked_notes = find_links(note_path)

        graph[note_filename] = linked_notes

        for linked_note in linked_notes:
            linked_note_path = os.path.join(os.path.dirname(note_path), linked_note + ".md")
            if linked_note not in graph:
                graph = make_graph(linked_note_path, graph)

        return {key: val for key, val in graph.items() if val}

    return make_graph(note_path, graph)


def convert_to_dot(graph):
    '''
    Write graph into a dot file.
    '''
    with open('graph.dot', mode='w', encoding='utf-8') as f:
        dot_graph = "diagraph {\n"
        for (key, val) in graph.items():
            dot_graph += f'{key} -> {val}\n'
        dot_graph += "}"
        f.write(dot_graph)