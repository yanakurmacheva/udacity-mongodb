#!/usr/bin/env python

import csv
import os
import re
from bs4 import BeautifulSoup


def check_contents(soup, id):
    '''Returns True if a specified element
    has any child nodes.
    '''
    element = soup.find(id=id)
    if element.contents:
        return True

def write_to_csv(filename, data):
    '''Writes data to CSV.'''
    filename = filename.split('.')[0] + '.csv'
    pathname = os.path.join('csv', filename)
    with open(pathname, 'w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(data)

def process_html(directory, filename):
    '''Extracts data from HTML tables.'''
    pathname = os.path.join(directory, filename)
    with open(pathname) as html:
        soup = BeautifulSoup(html, 'html.parser')

    if check_contents(soup, 'LblRecord'):
        print(f'{filename} - No Record Found.')
    else:
        data = []
        # get all th elements except for the last one
        ths = soup.find_all('th', scope='col')[:-1]
        header = [th.string.lower() for th in ths]
        data.append(header)

        # loop through each row
        for tr in soup.find_all('tr', class_='dataTDRight'):
            if tr.find('td', string='TOTAL'):
                continue # ignore year totals
            else:
                tds = tr.find_all('td')[:-1] # ignore monthly totals
                row = [re.sub('\xa0|,', '', td.string) for td in tds]
                data.append(row)

        write_to_csv(filename, data)

def process_all(directory):
    for filename in os.listdir(directory):
        process_html(directory, filename)


if __name__ == '__main__':
    process_all('html')
