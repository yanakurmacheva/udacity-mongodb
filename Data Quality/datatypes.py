# Quiz: Auditing Data Quality
# Starter code provided by Udacity

import csv
import os
import pprint

DIRECTORY = '../datasets'
CITIES = 'cities.csv'

FIELDS = ['name', 'timeZone_label', 'utcOffset', 'homepage', 'governmentType_label',
          'isPartOf_label', 'areaCode', 'populationTotal', 'elevation',
          'maximumElevation', 'minimumElevation', 'populationDensity',
          'wgs84_pos#lat', 'wgs84_pos#long', 'areaLand', 'areaMetro', 'areaUrban']

def skip_lines(file, n):
    '''Skips the first n lines of a file.'''
    for i in range(0, n):
        next(file)

def is_integer(string):
    '''Checks whether a string can be converted
    to an integer.
    '''
    try:
        int(string)
        return True
    except ValueError:
        return False

def is_float(string):
    '''Checks whether a string can be converted
    to a float.
    '''
    try:
        float(string)
        return True
    except ValueError:
        return False

def audit_file(pathname, fields):
    '''Lists all data types found in a field.'''
    fieldtypes = {}
    for field in fields:
        fieldtypes[field] = set()

    with open(pathname) as file:
        reader = csv.DictReader(file)
        skip_lines(reader, 3)

        for row in reader:
            for field in fields:
                if row[field] == 'NULL' or row[field] == '':
                    fieldtypes[field].add(type(None))
                elif row[field].startswith('{'):
                    fieldtypes[field].add(type(list()))
                elif is_integer(row[field]):
                    fieldtypes[field].add(type(int()))
                elif is_float(row[field]):
                    fieldtypes[field].add(type(float()))
                else:
                    fieldtypes[field].add(type(str()))

    return fieldtypes


def test():
    pathname = os.path.join(DIRECTORY, CITIES)
    fieldtypes = audit_file(pathname, FIELDS)
    pprint.pprint(fieldtypes)

    assert fieldtypes['areaLand'] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])


test()
