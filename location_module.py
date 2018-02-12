# Created to get locations of filming movies in a specified year
# Writes information about films in specified year in .csv file
# File name - year.csv
# Working with dictionary returned by read_file from get_info module

import googlemaps
from get_info import read_file


def get_coordinates(year):
    '''
    (int) -> set
    year: year information about we want to display
    return: set with tuple as information about film
    '''
    films = read_file()[year]
    # Creating of set with films
    locations = set()
    gmaps = googlemaps.Client(key='AIzaSyDSMV9xTNUkw1KzM8Qo3ZRh96snLJDQFvw')
    for film in films:
        try:
            location = gmaps.geocode(film[1])[0]['geometry']['location']
            country = film[1].split(',')[-1]
            locations.add((film[0], country, location['lat'],
                           location['lng']))
        except Exception:
            continue
    write_to_file(locations, year)
    return locations


def write_to_file(info, year):
    '''
    Writes information about films created in this year into the file
    (tuple) -> none
    info: information about film
    year: year film was created
    return: none
    '''
    with open(str(year) + '.csv', 'w', encoding='utf-8') as file:
        file.write('film,country,lat,long\n')
        for i in info:
            part = ''
            for x in range(len(i)):
                part += str(i[x]).replace(',', '') + ','
            file.write(part[0:-1] + '\n')
