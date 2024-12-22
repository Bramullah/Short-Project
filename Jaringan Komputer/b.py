import networkx as nx
import matplotlib.pyplot as plt

def draw_odd_even_network(n):
    G = nx.Graph()
    
    # Add nodes
    for i in range(1, n+1):
        for j in range(1, n+1):
            G.add_node((i, j))
    
    # Add edges for odd-even network merging
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j % 2 == 0:
                # Horizontal edges
                if i < n:
                    G.add_edge((i, j), (i+1, j))
                # Vertical edges
                if j < n:
                    G.add_edge((i, j), (i, j+1))
            else:
                # Horizontal edges
                if i > 1:
                    G.add_edge((i, j), (i-1, j))
                # Vertical edges
                if j < n:
                    G.add_edge((i, j), (i, j+1))
    
    # Draw the network
    pos = {node: node for node in G.nodes()}
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold', font_color='black')
    plt.title(f"(n,n) odd-even network merging for n = {n}")
    plt.show()

# Example usage:
draw_odd_even_network(8)
