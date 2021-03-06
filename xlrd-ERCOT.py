# Quiz: Reading Excel Files
# Starter code provided by Udacity

import pprint
import os
import xlrd
import numpy as np

DIRECTORY = 'datasets'
FILE = '2013_ERCOT_Hourly_Load_Data.xls'

def parse_file(pathname):
    '''Returns the min, max, and average hourly load for the COAST region
    along with the corresponding timestamps.
    '''
    workbook = xlrd.open_workbook(pathname)
    sheet = workbook.sheet_by_index(0)

    hourly_load = sheet.col_values(1, start_rowx=1)
    timestamps = sheet.col_values(0, start_rowx=1)

    mintime = xlrd.xldate_as_tuple(timestamps[np.argmin(hourly_load)], 0)
    maxtime = xlrd.xldate_as_tuple(timestamps[np.argmax(hourly_load)], 0)

    hsl = {
       'maxtime': maxtime,
       'maxvalue': np.max(hourly_load),
       'mintime': mintime,
       'minvalue': np.min(hourly_load),
       'avgcoast': np.mean(hourly_load)
    }

    return hsl

def test():
    hsl = parse_file(os.path.join(DIRECTORY, FILE))
    pprint.pprint(hsl)

    assert hsl['mintime'] == (2013, 2, 3, 4, 0, 0)
    assert round(hsl['minvalue'], 10) == round(6602.113899, 10)


test()
