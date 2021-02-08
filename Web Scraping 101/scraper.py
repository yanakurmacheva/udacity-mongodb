#!/usr/bin/env python

'''
Getting data on domestic and international flights
from the Bureau of Transportation Statistics.
'''

import time
import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def option_values(soup, id):
    '''Retrieves values of option elements nested
    inside a specified selector.
    '''
    values = []
    selector = soup.find(id=id)

    for option in selector.find_all('option'):
        if not option['value'].startswith('All'):
            values.append(option['value'])
    return values

def hidden_fields(soup, id):
    '''Gets names and values of hidden input elements.'''
    attributes = {}
    form = soup.find(id=id)

    for input in form.find_all('input', type='hidden'):
        name = input['name']
        value = input['value']
        attributes[name] = value
    return attributes

def save_html(html, carrier, airport):
    '''Saves the response content to a file.'''
    filename = f'{carrier}-{airport}.html'
    pathname = os.path.join('html', filename)
    with open(pathname, 'w') as file:
        file.write(html)

def main():
    url = 'https://www.transtats.bts.gov/Data_Elements.aspx?Data=2'

    session = requests.Session()
    response = session.get(url, verify='certificate.pem')
    soup = BeautifulSoup(response.text, 'html.parser')

    carriers = option_values(soup, 'CarrierList')
    airports = option_values(soup, 'AirportList')
    # carrier-airport tuples
    # subset for testing - JFK
    flights = [(c, a) for c in carriers for a in airports if a in ['JFK']]
    # for the POST request
    fixed = hidden_fields(soup, 'form1')
    fixed.update({'Submit': 'Submit'})

    for flight in tqdm(flights):
        data = {}
        data.update(fixed)
        # add carrier and airport
        data.update({'CarrierList': flight[0],
                     'AirportList': flight[1]})

        response = session.post(url, data=data)
        save_html(response.text, flight[0], flight[1])

        time.sleep(10)


if __name__ == '__main__':
    main()
