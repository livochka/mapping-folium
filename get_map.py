# Part of web_map module
# Created to make a map
import folium
from folium.plugins import MarkerCluster


def create_map(info, year):
    '''
    Creates map with films made in a specified year
    (int) -> none
    year: year, info about you want to see on map
    return: none
    '''
    map_1 = folium.Map(tiles='CartoDB dark_matter',
                       location=[48.137154, 11.576124],
                       zoom_start=7)
    print("Please, wait a little :)")
    for country in info:
        # Using of MarkerCluster instead of FeatureGroup makes you map
        # more easy, results more obvious
        marker_cluster = MarkerCluster(name=country).add_to(map_1)
        for film in info[country]:
            popup = folium.Popup(film[0], parse_html=True)
            folium.CircleMarker(location=[film[1], film[2]],
                                popup=popup,
                                icon=folium.Icon()).add_to(marker_cluster)

    map_1.add_child(folium.LayerControl())
    map_1.save("Map_" + str(year) + ".html")
