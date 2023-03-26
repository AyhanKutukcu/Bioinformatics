from suffix_trees import STree

def suffix_tree_edges(s):
    # Construct the suffix tree of s
    tree = STree.STree(s)
    
    # Traverse the suffix tree to obtain the substrings encoding the edges
    edges = []
    for node in tree.nodes.values():
        if node.id == 0:
            continue
        edges.append(s[node.edge_start:node.edge_end])
        
    return edges

# Example usage
s = "ATATCGTTTTATCGT"
edges = suffix_tree_edges(s)
print(edges)
