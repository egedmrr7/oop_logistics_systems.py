import heapq

def dijkstra(graph, start, end):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        path = path + [node]
        visited.add(node)

        if node == end:
            return path, cost

        for neighbor, weight in graph.get(node, {}).items():
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path))

    return None, float("inf")


def group_packages(packages):
    grouped = {}
    for p in packages:
        grouped.setdefault(p.destination, []).append(p)
    return grouped
