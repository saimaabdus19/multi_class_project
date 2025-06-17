from lib.tyre import *

class Car():

    def __init__(self):
        self._car_dict = {}

    def add_tyre(self, tyre):

        position = tyre.position
        self._car_dict[position] = tyre
        


    def add_tyre_readings(self,position, tyre_pressure, tyre_tread_depth):

        self._car_dict[position].add_reading(tyre_pressure, tyre_tread_depth)

#

# dictionary = {key: expression for (key, value) in iterable}

    def show_tyres(self):

        if self._car_dict == {}:
            raise Exception("No readings been found!")
        
        result = {key: value._tyre_readings[value.position][-1] for (key,value) in self._car_dict.items()}
        return result
