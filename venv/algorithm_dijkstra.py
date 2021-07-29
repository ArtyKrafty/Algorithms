def find_lowest_cost(costs):

    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
        return lowest_cost_node

def find_way(graph, costs, parents):

    node = find_lowest_cost (costs)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost (costs)
    return new_cost, processed

if __name__ == '__main__':

    '''Взвешенный граф'''

    graph = {}

    graph['start'] = {}
    graph['start']['a'] = 5
    graph['start']['b'] = 2
    graph['a'] = {}
    graph['a']['d'] = 2
    graph['a']['c'] = 4
    graph['b'] = {}
    graph['b']['a'] = 8
    graph['b']['d'] = 7
    graph['c'] = {}
    graph['c']['d'] = 6
    graph['c']['fin'] = 3
    graph['d'] = {}
    graph['d']['fin'] = 1
    graph['fin'] = {}

    '''Таблица стоимостей'''

    infinity = float('inf')
    costs = {}
    costs['a'] = 5
    costs['b'] = 2
    costs['c'] = 4
    costs['d'] = 6
    costs['fin'] = infinity

    '''Таблица родителей'''

    parents = {}
    parents['a'] = 'start'
    parents['b'] = 'start'
    parents['c'] = 'a'
    parents['d'] = 'b'

    parents['fin'] = None

    processed = []

    print(find_way(graph, costs, parents))

