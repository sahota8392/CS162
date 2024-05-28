# Author:  Harpreet Sahota
# GitHub:  Sahota8392
# Date:  7/14/2023
# Description: retrieve data from json and convert to formatted csv file

import json


class SatData:
    """reads json file of 2010 SAT results for NY City and writes data to text file"""

    def __init__(self):
        self._data = []

        with open('sat.json', 'r') as infile:
            self._data = json.load(infile)['data']

    def save_as_csv(self, dbns):
        """writes a csv outfile with the list of district bureau numbers specified"""

        dbn_set = set(dbns)  # make the dbn into a set
        all_data = [data for data in self._data if data[8] in dbn_set]
        sort_all_data = sorted(all_data, key=lambda data: data[8])  # sort by the DBN

        with open('output.csv', 'w') as outfile:
            outfile.write('DBN,'
                          'School Name,'
                          'Number of Test Takers,'
                          'Critical Reading Mean,'
                          'Mathematics Mean,'
                          'Writing Mean'

                          '\n')  # Header with line break at end for the data

            for data in sort_all_data:
                dbn = data[8]  # json file with index 8 = DBN
                school = data[9]
                test_takers = data[10]
                read_mean = data[11]
                math_mean = data[12]
                write_mean = data[13]

                outfile.write(f'{dbn},'
                              f'"{school}",'
                              f'{test_takers},'
                              f'{read_mean},'
                              f'{math_mean},'
                              f'{write_mean}'
                              '\n')


# sd = SatData()
# dbns = ["01M539", "02M294", "01M450", "02M418"]
# sd.save_as_csv(dbns)