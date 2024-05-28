# Author:  Harpreet Sahota
# GitHub:  Sahota8392
# Date:  7/14/2023
# Description: Add, Delete and search owner of pets

import json


class DuplicateNameError(Exception):
    """Exception raised when adding pet to pet list and name exists"""


class NeighborhoodPets:
    """Class with adding, removing and searching pet name, breed and owner"""

    def __init__(self):
        """Initial method"""
        self._pet_list = {}

    def get_pet_list(self):
        """Returns the pet list"""
        return list(self._pet_list.values())

    def add_pet(self, name, breed, owner):
        """Add pets to the pet list"""
        if name in self._pet_list:
            raise DuplicateNameError(f'{name} already exists in the Pet List')

        new_pet = {
            'name': name,
            'breed': breed,
            'owner': owner
        }
        self._pet_list[name] = new_pet

    def delete_pet(self, name):
        """Delete the pet from the pet list"""
        if name in self._pet_list:
            del self._pet_list[name]

    def get_owner(self, name):
        """Returns name of pet and its owner"""
        if name in self._pet_list:
            return self._pet_list[name]['owner']

    def save_as_json(self, filename):
        """Saves the file as a JSON file"""
        with open(filename, 'w') as outfile:
            json.dump(self._pet_list, outfile)

    def read_json(self, filename):
        """Reads the json file"""
        with open(filename, 'r') as infile:
            self._pet_list = json.load(infile)

    def get_all_species(self):
        """Returns python set of the breed of all pets"""
        species = set()

        for pet in self._pet_list.values():
            species.add(pet['breed'])
        return species


np = NeighborhoodPets()
try:
    np.add_pet("Fluffy", "gila monster", "Oksana")
    np.add_pet("Tiny", "stegasaurus", "Rachel")
    np.add_pet("Spot", "zebra", "Farrokh")
except DuplicateNameError:
    print('You tried to enter a pet with the same name as another pet.')
np.save_as_json("pets.json")
np.delete_pet("Tiny")
spot_owner = np.get_owner("Spot")
np.read_json("other_pets.json")  # where other_pets.json is a file it saved in some previous session
species_set = np.get_all_species()
print(np.get_all_species())
