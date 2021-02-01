# Quiz: Correcting Validity
# Starter code provided by Udacity

import csv
import re
import os

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def skip_lines(file, n):
    '''Skips the first n lines of a file.'''
    for i in range(0, n):
        next(file)

def filter_year(reader):
    '''Defines a category for each row based on
    the productionStartYear field.

    Categories - {good, bad}.
    '''
    good, bad = [], []
    year_re = re.compile('\d{4}(?=-)')

    for row in reader:
        timestamp = row['productionStartYear']
        match = year_re.search(timestamp)

        try:
            year = int(match.group())
            row['productionStartYear'] = year

            if 1885 < year < 2015:
                good.append(row)
            else:
                bad.append(row)
        except:
            bad.append(row)

    return good, bad

def write_to_csv(filename, data, header):
    '''Writes data to CSV.'''
    with open(filename, 'w') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=header)
        writer.writeheader()
        writer.writerows(data)

def process_file(input_file, output_good, output_bad):
    with open(input_file) as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames

        skip_lines(reader, 3)
        good, bad = filter_year(reader)

    write_to_csv(output_good, good, header)
    write_to_csv(output_bad, bad, header)


def test():
    pathname = os.path.join('../datasets', INPUT_FILE)
    process_file(pathname, OUTPUT_GOOD, OUTPUT_BAD)


test()
