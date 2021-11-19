# # initiate 3 hash table
#
# graph = {}
#
# graph['start'] = {}
# graph['start']["a"] = 6
# graph['start']["b"] = 2
#
# graph['a'] = {}
# graph['a']['fin'] = 1
#
# graph['b'] = {}
# graph['b']['a'] = 3
# graph['b']['fin'] = 5
#
# graph['fin'] = {}
#
# infinity = float('inf')
# costs = {}
# costs['a'] = 6
# costs['b'] = 2
# costs['fin'] = infinity
#
# parent = {}
# parent['a'] = 'start'
# parent['b'] = 'start'
# parent['fin'] = None
#
# processed = []
#

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]

        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# node = find_lowest_cost_node(costs)
# while node is not None:
#     cost = costs[node]
#     neighbors = graph[node]
#
#     for n in neighbors.keys():
#         new_cost = cost + neighbors[n]
#         if costs[n] > new_cost:
#             costs[n] = new_cost
#             parent[n] = node
#
#     processed.append(node)
#     node = find_lowest_cost_node(costs)
#
# print(costs)


##practice
graph = {}
graph['a'] = {}
graph['a']['b'] = 2
graph['a']['c'] = 5

graph['b'] = {}
graph['b']['c'] = 8
graph['b']['d'] = 7

graph['c'] = {}
graph['c']['d'] = 2
graph['c']['e'] = 4

graph['d'] = {}
graph['d']['f'] = 1

graph['e'] = {}
graph['e']['d'] = 6
graph['e']['f'] = 3

graph['f'] = {}

costs = {}
costs['b'] = 2
costs['c'] = 5
for i in ('d', 'e', 'f'):
    costs[i] = float('inf')

parents = {}
parents['b'] = 'a'
parents['c'] = 'a'

processed = []

for i in ('d', 'e', 'f'):
    parents[i] = None

node = find_lowest_cost_node(costs)
while node is not None:

    cost = costs[node]
    neighbors = graph[node]

    for neighbor in neighbors.keys():
        new_cost = cost + neighbors[neighbor]

        if new_cost < costs[neighbor]:
            costs[neighbor] = new_cost
            parents[neighbor] = node

    processed.append(node)

    node = find_lowest_cost_node(costs)


print(costs)
print(parents)