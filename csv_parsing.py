import csv
from city import City
from country import Country

def create_cities_countries_from_csv(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.

    :param path_to_csv: The path to the CSV file.
    """
    with open(path_to_csv, "r") as file:
        reader = csv.reader(file)
        # retrieve all the headers value and skips the line as well
        header = next(reader)

        city_ascii_index = -1   
        lat_index = -1   
        long_index = -1   
        country_name_index = -1   
        country_iso3_index = -1   
        city_type_index = -1   
        population_index = -1   
        city_id_index = -1   

        # go through the header, and assign the index variables to the index found
        for index, header_element in enumerate(header):
            if header_element == "city_ascii":
                city_ascii_index = index
            elif header_element == "lat":
                lat_index = index
            elif header_element == "lng":
                long_index = index
            elif header_element == "country":
                country_name_index = index
            elif header_element == "iso3":
                country_iso3_index = index
            elif header_element == "capital":
                city_type_index = index 
            elif header_element == "population":
                population_index = index
            elif header_element == "id":
                city_id_index = index
        
        # go through the values in the csv file, and assign each variable their value with now the index found
        # parsing was required for a few variables due to later needing it to be used as params for creating instances of certain classes
        for row in reader:
            city_name = row[city_ascii_index]
            coordinates = (float(row[lat_index]), float(row[long_index])) 
            country_name = row[country_name_index] 
            country_iso3 = row[country_iso3_index]
            city_type = row[city_type_index]
            # need the if statement, as some population was not provided in the csv file
            # set to 0, if population is empty
            if row[population_index] != "":
                population = int(row[population_index])
            else:
                population = 0
            city_id = int(row[city_id_index])
            
            # create a city instance
            city = City(city_name, coordinates, city_type, population, city_id)

            # create a new country instance and add the new city instance created to the country only if it is not already in name_to_countries
            # if country is found, we can just add the new city instance
            if country_name not in Country.name_to_countries:
                new_country = Country(country_name, country_iso3)
                new_country.add_city(city)
            else:
                Country.name_to_countries[country_name].add_city(city)


if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")
    for country in Country.name_to_countries.values():
        country.print_cities()