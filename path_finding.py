import math
import networkx

from city import City, get_city_by_id, get_cities_by_name
from itinerary import Itinerary
from vehicles import Vehicle, create_example_vehicles, TeleportingTarteTrolley
from csv_parsing import create_cities_countries_from_csv

# a list of all the city values
city_nodes = City.id_to_cities.values()


def find_shortest_path(
    vehicle: Vehicle, from_city: City, to_city: City
) -> Itinerary | None:
    """
    Returns a shortest path between two cities for a given vehicle as an Itinerary,
    or None if there is no path.

    :param vehicle: The vehicle to use.
    :param from_city: The departure city.
    :param to_city: The arrival city.
    :return: A shortest path from departure to arrival, or None if there is none.
    """

    # networkx can add_node and add_edge
    # For us, a node would represent a city (for example, Melbourne):
    # An edge is a link between two nodes
    # (for example, between the Melbourne and Kuala Lumpur nodes):
    # In order to represent the fact that there is a travel duration, we add weights on edges:

    # create a graph
    graph = networkx.Graph()

    # add all the nodes to the graph
    graph.add_nodes_from(city_nodes)

    for departure_city in city_nodes:
        for arrival_city in city_nodes:
            if departure_city != arrival_city:
                # check if we have add this edge already or not
                if graph.has_edge(departure_city, arrival_city):
                    continue
                # calculate travel time
                travel_time = vehicle.compute_travel_time(departure_city, arrival_city)
                # check if travel time isn't inf before adding an edge between cities
                if travel_time != math.inf:
                    #  add edge
                    graph.add_edge(departure_city, arrival_city, weight=travel_time)

    # we try to find the shortest path and return it as well as make sure it isn't None
    # if the try fails, due to no path was found, we return None
    try:
        shortest_path = networkx.shortest_path(
            graph, from_city, to_city, weight="weight"
        )
        if vehicle.compute_travel_time(shortest_path[0], shortest_path[1]) == math.inf:
            return None

        return Itinerary(shortest_path)
    except networkx.NetworkXNoPath:
        return None


if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")

    from_cities = set()

    for city_id in [1036533631, 1036142029, 1458988644]:
        from_cities.add(get_city_by_id(city_id))

    # we create some vehicles
    vehicles = create_example_vehicles()

    # test_vehicle = TeleportingTarteTrolley(1,50)
    # paris = get_city_by_id(1250015082)
    # auckland = get_city_by_id(1554435911)

    # shortest_path = find_shortest_path(test_vehicle, auckland, paris)
    # print(f"\t{test_vehicle.compute_itinerary_time(shortest_path)}"
    #         f" hours with {test_vehicle} with path {shortest_path}.")

    to_cities = set(from_cities)
    for from_city in from_cities:
        to_cities -= {from_city}
        for to_city in to_cities:
            print(f"{from_city} to {to_city}:")
            for test_vehicle in vehicles:
                shortest_path = find_shortest_path(test_vehicle, from_city, to_city)
                print(
                    f"\t{test_vehicle.compute_itinerary_time(shortest_path)}"
                    f" hours with {test_vehicle} with path {shortest_path}."
                )
