

def eulerian(graph, start):
    path =[]
    stack = [start]
    curr = graph[start].pop()
    temp = list(graph.keys())
    while len(stack) != 0:
        if (curr not in temp) or (len(graph[curr]) == 0):
            path.append(curr)
            curr = stack.pop()
        else:
            #stack += [curr]
            stack.append(curr)
            curr = graph[curr].pop()
    path.append(start)
    return path[::-1]


def SetStart(graph, inarg, outarg):
    indegarg = list(inarg.keys())
    outdegarg = list(outarg.keys())
    for key in outdegarg:
        if key in indegarg:
            if inarg[key] < outarg[key]:
                start=key
        else:
            start = key
    return start


def FindDegree(graph):
    indeg = {}
    outdeg = {}
    for edge in edges:
        start_node, end_node = edge.strip().split('->')
        end_node = end_node.split(",")
        start_node = start_node.strip()
        for lastnode in end_node:
            try:
                indeg[lastnode] += 1
            except:
                indeg[lastnode] = 1
        try:
            outdeg[start_node] += len(end_node)
        except:
            outdeg[start_node] = len(end_node)
    return indeg, outdeg
def makegraph(edges):
    graph = dict()
    for edge in edges:
        start_node, end_node = edge.strip().split(' -> ')
        end_node = end_node.split(",")
        start_node = start_node.strip()
        try:
            graph[start_node].extend(end_node)
        except:
            graph[start_node] = end_node
    return graph
def format(start_end):
    final = start_end[0]
    for edge in start_end[1:]:
        final += "->" + edge
    return final

with open("sample.txt","r") as file:
    edges = file.read().splitlines()
edges = file.read().splitlines()
graph = makegraph(edges)
indegree, outdegree = FindDegree(edges)
starting = SetStart(graph, indegree, outdegree)
start_end = eulerian(graph, starting)
answer = format(start_end)
print(graph)
print(answer)
#outdeg, indeg = FindDegree(graph)