import networkx as nx
import matplotlib.pyplot as plt

def draw_interconnection_network(n):
    # Create a directed graph
    G = nx.DiGraph()

    # Add processing elements (PEs)
    for i in range(n):
        G.add_node(f'PE{i}')

    # Add edges for each stage
    stages = [
        ('S1', ['PE0', 'PE7', 'PE1', 'PE6', 'PE2', 'PE5', 'PE3', 'PE4']),
        ('S2', ['PE0', 'PE4', 'PE1', 'PE5', 'PE2', 'PE6', 'PE3', 'PE7']),
        ('S3', ['PE0', 'PE2', 'PE1', 'PE3', 'PE4', 'PE6', 'PE5', 'PE7']),
        ('S4', ['PE0', 'PE1', 'PE2', 'PE3', 'PE4', 'PE5', 'PE6', 'PE7'])
    ]

    for stage, pe_list in stages:
        G.add_node(stage)
        for i in range(len(pe_list) - 1):
            G.add_edge(pe_list[i], pe_list[i+1])

    # Define layout manually
    pos = {
        'S1': (0, 3),
        'S2': (1, 2),
        'S3': (2, 1),
        'S4': (3, 0)
    }

    for i, pe in enumerate(G.nodes()):
        pos[pe] = (i % 4, i // 4)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, nodelist=G.nodes(), node_color='skyblue', node_size=700)
    nx.draw_networkx_labels(G, pos)

    # Draw edges
    for stage, pe_list in stages:
        for i in range(len(pe_list) - 1):
            nx.draw_networkx_edges(G, pos, edgelist=[(pe_list[i], pe_list[i+1])], arrows=True, connectionstyle='arc3,rad=0.1')

    plt.title(f"Interconnection Network for Odd-Even Merge Sorting (n = {n})")
    plt.axis('off')
    plt.show()

# Example usage with n = 8
draw_interconnection_network(4)
