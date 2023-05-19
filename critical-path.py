#Lauren Coleman C00101517
#Certification of Authenticity:
#I certify that this assignment is entirely my own work.
import math
def create_graph(graph):
    """Create adjacency list from directed graph G. Returns adjacency list."""
    vertices = input("How many vertices are in the matrix? ")
    for i in range(int(vertices) + 2):
        graph[i] = []
    for i in range(int(vertices)):
        while True:
            arr = []
            number = (input("Type a child number for " + str(i) +
                           " or type -1 to move on.\n"))
            if(number == "-1"):
                break;
            weight = input("Type a weight for " + number + "\n")
            arr = [int(number), int(weight)]
            graph[i].append(arr)
    #connect s and t       
    for node, children in graph.items():
        if(node == len(graph) - 2):
            break;
        hasChild = False
        hasPred = False
        if(children != []):
            hasChild = True
        for node2, children2 in graph.items():
            for child in children2:
                if(node2 < len(graph) - 2):
                    if(node == child[0]):
                        hasPred = True
                        break;   
        if(not hasPred):
            graph[len(graph) - 2].append([node, 0])
        if(not hasChild):
            graph[node].append([len(graph) - 1, 0])
    return graph


def print_graph(graph):
    node = "Node s:->"
    for child in graph[len(graph) - 2]:
        node += "(" + str(child[0]) + "," + str(child[1]) + ")" + "->"
    node += "NULL\n"
    for i in range(len(graph) - 2):
        node += "Node " + str(i)+ ":->"
        for child in graph[i]:
            if child[0] == len(graph) - 1:
                node += "(t," + str(child[1]) + ")" + "->"
            else:
                node += "(" + str(child[0]) + "," + str(child[1]) + ")" + "->"
        node += "NULL\n"
    node += "Node t:->"
    for child in graph[len(graph) - 1]:
        node += "(" + str(child[0]) + "," + str(child[1]) + ")" + "->"
    node += "NULL\n"
    print(node)


def critical_path(graph):
    """
    Input: G = (V,E,s), a weighted dag with a source s
    Output: pred, an array of size |V| such that pred[i] is the predecessor
    of node i along the critical path from s to i
    dist, an array of size |V| such that dist[i] contains the length
    of the critical path from s to i
    """
    pred = []
    dist = []
    for i in range(len(graph)):
        pred.append(-1)
        dist.append(-math.inf)
    dist[len(graph) - 2] = 0;
    sorted_graph = topological_sort(graph)

    for u in sorted_graph:
        for child in graph[u]:
            if dist[u] == -math.inf:
                var = child[1]
            else:
                var = dist[u] + child[1]
            if dist[child[0]] < var:
                dist[child[0]] = var
                pred[child[0]] = u
    #print the nodes on the critical path
    for i in range(len(pred)):
        if pred[i] == len(graph)- 2:
            pred[i] = "s"
    i = len(graph) - 1
    path = "t"
    while i != "s":
        i = pred[i]
        path = str(i) + "->" + str(path)
    print("Critical path: " + str(path))


def topological_sort(graph):
    """
    Input: G = |V,E|, a dag
    Output: sorted, a list of size |V| with the nodes of the graph in
    topological order
    """
    visited = []
    sorted_graph = []
    for i in range(len(graph)):
        visited.append(False)

    for i in range(len(graph)):
        if not visited[i]:
            dfs_topological_sort(graph, i, visited, sorted_graph)
    sorted_graph.reverse()
    return sorted_graph


def dfs_topological_sort(graph, node, visited, sorted_graph):
    """
    Input: graph = (V,E), a dag
    node, a node in graph
    Data: visited, an array of size |V|
    sorted_graph, a list
    Result: visited[i] is true if node i is reachable from node
    sorted contains in its start, in reverse order, the dead-ends we
    reached using depth-first search starting from node
    """
    visited[node] = True
    for child in graph[node]:
        if not visited[child[0]]:
            dfs_topological_sort(graph, child[0], visited, sorted_graph)
    sorted_graph.append(node)


def main():
    graph = {}
    adj_list = []
    menu = """
    Enter the letter below that corresponds to the desired singly-linked list operation:
    A. Input a task scheduling graph, G, similar to Figure 6.9, and generate
    the adjacency list for graph G.
    B. Calculate and print the nodes that are on the critical path.
    C. Print the adjacency list (i.e., the list of singly-linked lists) for graph G.
    D. End program.
    """
    while True:
        choice = input(menu)
        if choice.casefold() == 'a':
            create_graph(graph)
        elif choice.casefold() == 'b':
            critical_path(graph)
        elif choice.casefold() == 'c':
            adj_list = print_graph(graph)
        elif choice.casefold() == 'd':
            break;
        else:
            print("Invalid option! Please enter A, B, C or D.")

if __name__== "__main__":
    main()
