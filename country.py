from tabulate import tabulate
from city import City, create_example_cities

class Country():
    """
    Represents a country.
    """

    name_to_countries = dict() # a dict that associates country names to instances.

    # dictionary to associate cities that are associated to that country
    # key is country name
    # value is an array of city instances
    countries_and_their_cities = dict()

    def __init__(self, country_name: str, country_iso3: str) -> None:
        """
        Creates an instance with a country name and a country ISO code with 3 characters.

        :param country_name: The name of the country
        :param country_iso3: The unique 3-letter identifier of this country
	    :return: None
        """
        self.name = country_name
        self.iso3 = country_iso3
        
        Country.name_to_countries[self.name] = self

    def add_city(self, city: City) -> None:
        """
        Adds a city to the country.

        :param city: The city to add to this country
        :return: None
        """
        # process to add new city into the country by the dict countries_and_their_cities
        # if statement is to check if a country key exist or not first to see if its a new country needed to be added along with the city
        # if not, we just add a new city instance to the country key and update the dict
        if self.name not in Country.countries_and_their_cities:
            Country.countries_and_their_cities.update({self.name: [city] })
        else:
            old_value = Country.countries_and_their_cities[self.name]
            new_list = []
            for value in old_value:
                new_list.append(value)
            new_list.append(city)
            Country.countries_and_their_cities.update({self.name: new_list })
        

    def get_cities(self, city_type: list[str] = None) -> list[City]:
        """
        Returns a list of cities of this country.

        The argument city_type can be given to specify a subset of
        the city types that must be returned.
        Cities that do not correspond to these city types are not returned.
        If None is given, all cities are returned.

        :param city_type: None, or a list of strings, each of which describes the type of city.
        :return: a list of cities in this country that have the specified city types.
        """
        city_list = []

        if city_type != None:
            for city in Country.countries_and_their_cities[self.name]:
                for city_type_selected in city_type:
                    if city.city_type == city_type_selected:
                        city_list.append(city)
        elif self.name in Country.countries_and_their_cities.keys():
            for city in Country.countries_and_their_cities[self.name]:
                city_list.append(city)
        
        return city_list

    def print_cities(self) -> None:
        """
        Prints a table of the cities in the country, from most populous at the top
        to least populous. Use the tabulate module to print the table, with row headers:
        "Order", "Name", "Coordinates", "City type", "Population", "City ID".
        Order should start at 0 for the most populous city, and increase by 1 for each city.
        """
        print("Cities of " + self.name)

        headers=["Order", "Name", "Coordinates","City type", "Population", "City ID"]
        table = [headers]

        cities = Country.countries_and_their_cities[self.name]
        cities.sort(key=lambda city: city.population, reverse=True)
        
        for index, city in enumerate(cities):
            table.append([str(index), city.name, str(city.coordinates), city.city_type, str(city.population), str(city.city_id)])
                
        print(tabulate(table, numalign="left"))
    
    def __str__(self) -> str:
        """
        Returns the name of the country.
        """
        return self.name


def add_city_to_country(city: City, country_name: str, country_iso3: str) -> None:
    """
    Adds a City to a country.
    If the country does not exist, create it.

    :param country_name: The name of the country
    :param country_iso3: The unique 3-letter identifier of this country
    :return: None
    """
    if country_name not in Country.name_to_countries:
        new_country = Country(country_name, country_iso3)
        new_country.add_city(city)
    else:
        Country.name_to_countries[country_name].add_city(city)
 

def find_country_of_city(city: City) -> Country:
    """
    Returns the Country this city belongs to.
    We assume there is exactly one country containing this city.

    :param city: The city.
    :return: The country where the city is.
    """
    for country in Country.countries_and_their_cities.keys():
        for index in range(0,len(Country.countries_and_their_cities[country])):
            if Country.countries_and_their_cities[country][index] == city:
                if country in Country.name_to_countries:
                    return Country.name_to_countries[country]

def create_example_countries() -> None:
    """
    Creates a few countries for testing purposes.
    Adds some cities to it.
    """
    create_example_cities()
    malaysia = Country("Malaysia", "MAS")
    kuala_lumpur = City.name_to_cities["Kuala Lumpur"][0]
    malaysia.add_city(kuala_lumpur)
    print(malaysia)
    
    for city_name in ["Melbourne", "Canberra", "Sydney"]:
        add_city_to_country(City.name_to_cities[city_name][0], "Australia", "AUS")
    
    malaysia.get_cities()

    # # australia = Country("Australia", "AUS")
    # new_zealand = Country("New Zealand", "NZL")

    # # melbourne =  City("Melbourne", (-37.8136, 144.9631), "admin", 4529500, 1036533631)
    # # auckland = City("Auckland", (-35.2931, 149.1269), "primary", 381488, 1036142029)

    # # add_city_to_country(melbourne, "Australia", "AUS")
    # # add_city_to_country(auckland, "New Zealand", "NZL")

    # # print(australia.get_cities())
    # print(new_zealand.get_cities())

def test_example_countries() -> None:
    """
    Assuming the correct countries have been created, runs a small test.
    """
    Country.name_to_countries["Australia"].print_cities()
    # Country.name_to_countries["New Zealand"].print_cities()


if __name__ == "__main__":
    create_example_countries()
    test_example_countries()
