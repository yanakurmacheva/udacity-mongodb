# Quiz: Parsing CSV files
# Starter code provided by Udacity

import csv
import os

DIRECTORY = 'datasets'
FILE = 'thebeatles-discography.csv'

def parse_file(pathname):
    '''Converts each of the first 10 lines in file (not including the header)
    into a dictionary of column name/field value pairs.
    '''
    with open(pathname, 'r') as file:
        lines = file.readlines()[:11]
        lines = [line.strip().split(',') for line in lines]
        header = lines[0]
        albums = [dict(zip(header, line)) for line in lines[1:]]
    return albums

# handle the problematic line
def parse_csv(pathname):
    with open(pathname, 'r') as file:
        reader = csv.DictReader(file)
        albums = [row for row in reader]
    return albums

def test():
    pathname = os.path.join(DIRECTORY, FILE)
    result = parse_file(pathname)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert result[0] == firstline
    assert result[9] == tenthline


test()
