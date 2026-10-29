
graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}

h = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G": 0
}


def search(graph, h, start, goal):
    waiting = [(h[start], 0, start, [start])]
    best = {start: 0}
    expanded = []

    while waiting:
        waiting.sort()
        f, g, node, path = waiting.pop(0)

        if g != best[node]:
            continue

        expanded.append(node)

        if node == goal:
            return g, path, expanded

        for next_node, cost in graph[node]:
            new_cost = g + cost

            if new_cost < best.get(next_node, float("inf")):
                best[next_node] = new_cost
                total = new_cost + h[next_node]

                waiting.append(
                    (total, new_cost, next_node, path + [next_node])
                )

    return None, [], expanded


# A* search
print("A* Search")
cost, path, expanded = search(graph, h, "S", "G")
print("Path:", path)
print("Path cost:", cost)
print("Expanded nodes:", expanded)
print("Expansion count:", len(expanded))


# UCS search
zero_h = {
    "S": 0,
    "A": 0,
    "B": 0,
    "C": 0,
    "G": 0
}

print("\nUCS Search")
cost, path, expanded = search(graph, zero_h, "S", "G")
print("Path:", path)
print("Path cost:", cost)
print("Expanded nodes:", expanded)
print("Expansion count:", len(expanded))
