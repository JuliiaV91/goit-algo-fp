
import heapq

graph = {
    "Ravensburg": {"München": 3, "Stuttgart": 2},
    "München": {"Ravensburg": 3, "Berlin": 11, "Dresden": 5, "Frankfurt": 6, "Düsseldorf": 9, "Stuttgart": 4},
    "Frankfurt": {"Düsseldorf": 2, "München": 6, "Stuttgart": 4, "Berlin": 8, "Wiesbaden": 1},
    "Düsseldorf": {"München": 9, "Berlin": 4, "Stuttgart": 5, "Frankfurt": 2, "Dresden": 3},
    "Dresden": {"Düsseldorf": 3, "Berlin": 5},
    "Berlin": {"Stuttgart": 6, "Frankfurt": 8, "Düsseldorf": 4, "Dresden": 5},
    "Stuttgart": {"München": 4, "Frankfurt": 4, "Düsseldorf": 5, "Berlin": 6, "Ravensburg": 2}, 
    "Wiesbaden": {"Frankfurt": 1}
}

def dijkstra(graph, start):
    
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    shortest_paths = {vertex: [] for vertex in graph}
    shortest_paths[start] = [start]

    while priority_queue:
        
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                shortest_paths[neighbor] = shortest_paths[current_vertex] + [neighbor]
     
    return distances, shortest_paths

distances, shortest_paths = dijkstra(graph, "Ravensburg")

# Виведення результатів
print("Найкоротші відстані:", distances)
print("Найкоротші шляхи:", shortest_paths)
