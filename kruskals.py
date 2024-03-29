from unionfind import unionfind
import matplotlib.pyplot as plt
import networkx as nx



def make_graph():
    # identical graph as the YouTube video: https://youtu.be/71UQH7Pr9kU
    # tuple = (cost, n1, n2)
    return {
        'A': [(9, 'B', 'A'), (8, 'C', 'A'), (12, 'D', 'A'), (3, 'E', 'A'), (15, 'F', 'A')],
        'B': [(9, 'A', 'B'), (5, 'C', 'B'), (6, 'D', 'B'), (13, 'E', 'B'), (10, 'F', 'B')],
        'C': [(5, 'B', 'C'), (8, 'A', 'C'), (4, 'D', 'C'), (14, 'E', 'C'), (2, 'F', 'C')],
        'D': [(4, 'C', 'D'), (6, 'B', 'D'), (12, 'A', 'D'), (16, 'E', 'D'), (11, 'F', 'D')],
        'E': [(16, 'D', 'E'), (14, 'C', 'E'), (13, 'B', 'E'), (3, 'A', 'E'), (7, 'F', 'E')],
        'F': [(7, 'E', 'F'), (11, 'D', 'F'), (2, 'C', 'F'), (10, 'B', 'F'), (15, 'A', 'F')],
    }


def load_edges(G):
    num_nodes = 0
    edges = []

    for _, value in G.items():
        num_nodes += 1
        edges.extend(value)

    return num_nodes, sorted(edges)


def conv_char(c):
    return ord(c) - 65


def kruskals(G):
    total_cost = 0
    MST = []

    num_nodes, edges = load_edges(G)
    uf = unionfind(num_nodes)

    for edge in edges:
        cost, n1, n2 = edge[0], edge[1], edge[2]

        if not uf.issame(conv_char(n1), conv_char(n2)):
            total_cost += cost
            uf.unite(conv_char(n1), conv_char(n2))
            MST.append((n1, n2, cost))

    return MST, total_cost


def draw_graph(MST):
    G = nx.Graph()

    for edge in MST:
        G.add_edge(edge[0], edge[1], weight=edge[2])

    pos = nx.spring_layout(G)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12, font_weight='bold',font_color='green')

    nx.draw(G, pos, with_labels=True, node_size=500, node_color='Black', font_size=10, font_color='White', font_weight='bold')
    plt.title("Minimum Spanning Tree")
    plt.show()

def main():
    G = make_graph()
    MST, total_cost = kruskals(G)

    print("Edges of tree in order they are added:")
    print()
    for i, edge in enumerate(MST, start=1):
        print(f"{i}. Edge {edge[0]},{edge[1]} (Weight: {edge[2]})")
    print()
    print(f'Total weight/length: {total_cost}')
    print()

    draw_graph(MST)

main()