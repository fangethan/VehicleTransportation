from mpl_toolkits.basemap import Basemap 
import matplotlib.pyplot as plt
from itinerary import Itinerary
from city import City, create_example_cities, get_cities_by_name

def plot_itinerary(itinerary: Itinerary, projection = 'robin', line_width=2, colour='b') -> None:
    """
    Plots an itinerary on a map and writes it to a file.
    Ensures a size of at least 50 degrees in each direction.
    Ensures the cities are not on the edge of the map by padding by 5 degrees.
    The name of the file is map_city1_city2_city3_..._cityX.png.

    :param itinerary: The itinerary to plot.
    :param projection: The map projection to use.
    :param line_width: The width of the line to draw.
    :param colour: The colour of the line to draw.
    """

    #Setting up the workspace for the map
    plt.figure(figsize=(12, 8))
    plt.title("World Map")

    # Creating the map
    m = Basemap(projection='cyl',resolution='c')

    lats, lons = [], []
    order = 0
    ##
    for city in itinerary.cities:  
        # lat        
        lats.append(city.coordinates[0])        
        # lng
        lons.append(city.coordinates[1])
        order += 1
        #adding name of city
        plt.text(city.coordinates[1], city.coordinates[0], f"{city.name} ({order})",fontsize=7,style='italic',fontweight='bold',ha='left',va='top',color='red')


    #Adding padding of 5 degrees.
    lat_min, lat_max = min(lats)-5, max(lats)+5
    lon_min, lon_max = min(lons)-5, max(lons)+5
    
    # Ensure the map has a minimum size of 50 degrees in each direction
    if lon_max - lon_min < 50:
        lon_mid = (lon_min + lon_max) / 2
        lon_min, lon_max = lon_mid - 25, lon_mid + 25
    if lat_max - lat_min < 50:
        lat_mid = (lat_min + lat_max) / 2
        lat_min, lat_max = lat_mid - 25, lat_mid + 25

    m.drawcoastlines()
    m.drawcountries(linewidth=0.5)
    m.drawstates(linewidth=0.5)
    m.fillcontinents(color='tan',lake_color='lightblue')
    m.drawmapboundary(fill_color='lightblue')

    x, y = m(lons, lats)
    m.plot(x, y, linewidth=line_width, color=colour)

    #Saving the map
#   filename = f"map_{'_'.join(itinerary)}.png"
    filename = "test.png"
    plt.savefig(filename)



if __name__ == "__main__":
    # create some cities
    city_list = list()

    city_list.append(City("Melbourne", (-37.8136, 144.9631), "primary", 4529500, 1036533631))
    city_list.append(City("Sydney", (-33.8688, 151.2093), "primary", 4840600, 1036074917))
    city_list.append(City("Brisbane", (-27.4698, 153.0251), "primary", 2314000, 1036192929))
    city_list.append(City("Perth", (-31.9505, 115.8605), "1992000", 2039200, 1036178956))

    # plot itinerary
    plot_itinerary(Itinerary(city_list))


    

