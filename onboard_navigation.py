from city import City, get_cities_by_name
from vehicles import Vehicle, create_example_vehicles
from csv_parsing import create_cities_countries_from_csv
from path_finding import find_shortest_path
from map_plotting import plot_itinerary

def onboard_navigation_user():
    #we create some vehicles
    vehicles = create_example_vehicles()
    # create an array to hold our vehicle_options_input_list
    vehicle_options_input_list = []

    # get a list of all our vehicle_options_input_list
    for index in range(0,len(vehicles)):
        vehicle_options_input_list.append(index+1)

    valid_vehicle = False
    valid_departure_city = False
    valid_arrival_city = False

    # checks if we inputed a valid option from the option list
    # except catches any ValueErrors of any invalid inputs that are not part of the vehicle_options_input_list list
    while not valid_vehicle:
        try:
            vehicle_option = int(input("Choose a vehicle (Options are " + str(vehicle_options_input_list) + "): "))
            if vehicle_option not in vehicle_options_input_list:
                raise ValueError
            valid_vehicle = True
        except ValueError:
            print("Invalid vehicle option. Please enter a valid number.")

    # checks if we inputed a valid departure city
    # except catches any ValueErrors if input doesn't match the departure cities we have
    while not valid_departure_city:
        try:
            departure_city_chosen = input("Choose a departure city: ")
            if get_cities_by_name(departure_city_chosen):
                departure_city_chosen = get_cities_by_name(departure_city_chosen)
                valid_departure_city = True
            else:
                raise ValueError
        except ValueError:
            print("Invalid departure city. Please enter a valid city name.")

    # checks if we inputed a valid arrival city
    # except catches any ValueErrors if input doesn't match the arrival cities we have
    while not valid_arrival_city:
        try:
            arrival_city_chosen = input("Choose an arrival city: ")
            if get_cities_by_name(arrival_city_chosen):
                arrival_city_chosen = get_cities_by_name(arrival_city_chosen)
                valid_arrival_city = True
            else:
                raise ValueError
        except ValueError:
            print("Invalid arrival city. Please enter a valid city name.")

    # after all inputs are valid, we find the shortest path
    itinerary = find_shortest_path(vehicles[vehicle_option-1], departure_city_chosen[0], arrival_city_chosen[0])

    # check if the shortest path found is not none
    #  if it isn't, we plot a map of the shortest path
    if itinerary is not None:
        plot_itinerary(itinerary)
    
    exit()

if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")

    onboard_navigation_user()
