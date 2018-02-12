# The module created to read and evaluate .csv files
import pandas as pd
import chardet


def read_location(path):
    '''
    file -> dictionary
    path: path to file
    return: dictionary with year as key, list with name, latitude and
    longtitude as values
    '''
    # Figuring out encoding of file
    with open(path, 'rb') as f:
        result = chardet.detect(f.read())

    file = pd.read_csv(path, encoding=result['encoding'])
    info = {}
    nm, ctr, lt, ln, = file['film'], file['country'], \
                       file['lat'], file['long']
    for name, country, lat, long in zip(nm, ctr, lt, ln):
        if country not in info:
            info[country] = [[name, lat, long]]
        else:
            info[country].append([name, lat, long])
    return info
