# Author: Harpreet Sahota
# GitHub: sahota8392
# Date: 7/17/23
# Description: class NobelData to read JSON file containing Nobel Prizes data allowing user to search the data

import json


class NobelData:
    """
    reads JSON file with data of Nobel Prizes and allows user to search the data
    """

    def __init__(self):
        """open the json file and store to private data member"""
        self._nobel_prizes = {}

        with open('nobels.json', 'r') as infile:
            self._nobel_prizes = json.load(infile)

    def get_nobel(self):
        """retrieves the nobel prize dictionary"""
        return self._nobel_prizes

    def search_nobel(self, year, category):
        """searches nobels.json file for the year and category returning the name and quote"""

        year = str(year)
        category = category.lower()
        winner = []

        for prize in self._nobel_prizes.get('prizes', []):
            if prize.get('year') == year and prize.get('category').lower() == category:
                laureates = prize.get('laureates', [])
                winner.extend([laureate.get('surname', "") for laureate in laureates])
        return sorted(winner)


nd = NobelData()
print(nd.search_nobel('2001', 'economics'))
