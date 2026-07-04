import osmnx as ox
import networkx as nx

from routing.check_traffic import predict_traffic


def calculate_route(traffic):

    print("Loading saved graph...")

    G = ox.load_graphml("datasets/vijayawada.graphml")

    print("Graph loaded successfully!")

    # Example coordinates
    start = (16.5062, 80.6480)
    end = (16.5150, 80.6300)

    # Find nearest graph nodes
    orig_node = ox.distance.nearest_nodes(G, start[1], start[0])
    dest_node = ox.distance.nearest_nodes(G, end[1], end[0])

    # Dijkstra shortest path
    route = nx.shortest_path(G, orig_node, dest_node, weight="length")

    distance = nx.shortest_path_length(
        G,
        orig_node,
        dest_node,
        weight="length"
    )

    print("Distance:", round(distance / 1000, 2), "km")

    # Traffic Prediction
    input_data = [[9, 2, 7, 1, 3]]

    traffic = predict_traffic(input_data)


    if traffic < 10:
        speed = 40
    elif traffic < 20:
        speed = 30
    else:
        speed = 20

    time_minutes = (distance / 1000) / speed * 60

    print("Estimated Time:", round(time_minutes, 2), "minutes")

    return route, distance, time_minutes


if __name__ == "__main__":

    route, distance, eta = calculate_route()

    print("\nRoute Nodes:", len(route))