# Quiz: Fixing the Area
# Starter code provided by Udacity

import csv
import os
import pprint

DIRECTORY = '../datasets'
CITIES = 'cities.csv'

def skip_lines(file, n):
    '''Skips the first n lines of a file.'''
    for i in range(0, n):
        next(file)

def fix_area(area):
    '''Returns the value with more significant digits
    when areaLand contains an array.
    '''
    if area == 'NULL':
        return None
    elif area.startswith('{'):
        values = area.strip('{}').split('|')
        values.sort(key=lambda s: len(s), reverse=True)
        value = values[0]
        return float(value)
    else:
        return float(area)

def process_file(pathname):
    data = []

    with open(pathname) as file:
        reader = csv.DictReader(file)
        skip_lines(reader, 3)

        for line in reader:
            if 'areaLand' in line:
                line['areaLand'] = fix_area(line['areaLand'])
            data.append(line)
    return data


def test():
    pathname = os.path.join(DIRECTORY, CITIES)
    data = process_file(pathname)

    print('Printing three example results:')
    for n in range(5,8):
        pprint.pprint(data[n]['areaLand'])

    assert data[3]['areaLand'] == None
    assert data[8]['areaLand'] == 55166700.0
    assert data[20]['areaLand'] == 14581600.0
    assert data[33]['areaLand'] == 20564500.0


test()
