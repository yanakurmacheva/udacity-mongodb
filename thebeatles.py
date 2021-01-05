# Quiz: Parsing CSV files
# Starter code provided by Udacity

import csv
import os

DIRECTORY = "data"
FILE = "thebeatles-discography.csv"

def parse_file(datafile):
    '''Converts each of the first 10 lines in datafile (not including the header)
    into a dictionary of column name/field value pairs.
    '''
    with open(datafile, 'r') as f:
        lines = f.readlines()
        albums = [line.strip().split(',') for line in lines[0:11]]
        data = [dict(zip(albums[0], album)) for album in albums[1:11]]
    return data

# handle the problematic line
def parse_csv(datafile):
    with open(datafile, 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data

def test():
    datafile = os.path.join(DIRECTORY, FILE)
    result = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert result[0] == firstline
    assert result[9] == tenthline


test()
