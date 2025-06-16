from lib.car import *
from lib.tyre import *

def test_add_tyre_to_the_car():
    car = Car()
    tyre = Tyre()
    
    assert car._car_dict == {}
