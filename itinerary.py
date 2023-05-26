from math import radians, cos, sin, asin, sqrt
from city import City, create_example_cities, get_cities_by_name

class Itinerary():
    """
    A sequence of cities.
    """

    def __init__(self, cities: list[City]) -> None:
        """
        Creates an itinerary with the provided sequence of cities,
        conserving order.
        :param cities: a sequence of cities, possibly empty.
        :return: None
        """
        self.cities = cities            
    
    def total_distance(self) -> int:
        """
        Returns the total distance (in km) of the itinerary, which is
        the sum of the distances between successive cities.
        :return: the total distance.
        """
        distance_total = 0
        for index in range(0, len(self.cities)):
            if index+1 < len(self.cities): 
                distance_total += self.cities[index].distance(self.cities[index+1])

        return distance_total

    def append_city(self, city: City) -> None:
        """
        Adds a city at the end of the sequence of cities to visit.
        :param city: the city to append
        :return: None.
        """
        self.cities.append(city)

    def min_distance_insert_city(self, city: City) -> None:
        """
        Inserts a city in the itinerary so that the resulting
        total distance of the itinerary is minimised.
        :param city: the city to insert
        :return: None.
        """
        min_distance = float('inf')
        best_index = 0

        # the reason the range +1 because the loop includes an additional iteration that allows for the new city to be compared to th elast city in the iternery
        # find the minimum distance as well as the best index to insert the city in the certain path
        for index in range(len(self.cities) + 1):
            new_distance = 0
            if index == 0:
                new_distance = city.distance(self.cities[0])
            elif index == len(self.cities):
                new_distance = city.distance(self.cities[-1])
            else:
                # the first value calculates the distance between city and the prevous city
                # the second value calculates distance between city and the next city
                # the third value calculates the distance between previous city and next city
                # we subtract to see what is the new distance if the city is inserted at this index
                new_distance = city.distance(self.cities[index-1]) + city.distance(self.cities[index]) - self.cities[index-1].distance(self.cities[index])

            if new_distance < min_distance:
                min_distance = new_distance
                best_index = index

        self.cities.insert(best_index, city)

    def __str__(self) -> str:
        """
        Returns the sequence of cities and the distance in parentheses
        For example, "Melbourne -> Kuala Lumpur (6368 km)"

        :return: a string representing the itinerary.
        """
        route = ""
        if len(self.cities) == 0:
            route = "(" + str(Itinerary.total_distance(self)) + " km)"
            return route
        
        for index, city in enumerate(self.cities): 
            if index != len(self.cities)-1:
                route += city.name + " -> "
            else:
                route += city.name + " (" + str(Itinerary.total_distance(self)) + " km)"
        
        return route


if __name__ == "__main__":
    create_example_cities()
    test_itin = Itinerary([get_cities_by_name("Melbourne")[0],get_cities_by_name("Kuala Lumpur")[0]])
    print(test_itin)

    #we try adding a city
    test_itin.append_city(get_cities_by_name("Baoding")[0])
    print(test_itin)

    #we try inserting a city
    test_itin.min_distance_insert_city(get_cities_by_name("Sydney")[0])
    print(test_itin)

    #we try inserting another city
    test_itin.min_distance_insert_city(get_cities_by_name("Canberra")[0])
    print(test_itin)

    # city1 = City('Melbourne', (-37.8136, 144.9631), 'primary', 1000000, 1)
    # city2 = City('Sydney', (-33.8688, 151.2093), 'primary', 5000000, 2)
    # city3 = City('Brisbane', (-27.4698, 153.0251), 'primary', 2000000, 3)
    # itinerary1 = Itinerary([city1, city2, city3])
    
    # city4 = City('Perth', (-31.9505, 115.8605), 'primary', 2000000, 4)
    # itinerary1.min_distance_insert_city(city4)
    # print(itinerary1)

    # city5 = City('Adelaide', (-34.9285, 138.6007), 'primary', 2000000, 5)
    # itinerary1.min_distance_insert_city(city5)
    # print(itinerary1)
