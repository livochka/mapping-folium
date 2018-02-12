# Program exist to show movies filmed in specified year on map
# The main module
# Program uses information from locations.list rewritten to different csv
# files divided by year

from get_info_year import read_location
from get_map import create_map


def main():
    '''
    Main function, in result you get a map with information about movies filmed
    in year you want
    none -> none
    return: none
    '''
    print("Hello!")
    print('We can create the film-map for you, all you need - entering a year'
          ' information about you want to see on map. Information includes '
          'film name and location.')
    year = get_year()
    info = read_location('data/' + str(year) + '.csv')
    create_map(info, year)
    print("Excellent! Look for Map_{}.html "
          "in this directory".format(str(year)))


def get_year():
    '''
    Getting year from user
    (none) -> int
    return: year
    '''
    for i in range(3):
        try:
            year = int(input('Enter a year: '))
            return year
        except Exception:
            continue


main()
