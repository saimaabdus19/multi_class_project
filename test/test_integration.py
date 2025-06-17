from lib.car import *
from lib.tyre import *
import pytest

def test_add_tyre_to_the_car():
    car = Car()
    right_tyre = Tyre("right_tyre")
    car.add_tyre(right_tyre)
    assert car._car_dict == {"right_tyre": right_tyre}


def test_add_multiple_tyre_readings():
    car = Car()
    right_tyre = Tyre("right_tyre")
    left_tyre = Tyre("left_tyre")
    car.add_tyre(right_tyre)
    car.add_tyre(left_tyre)
    assert car._car_dict == {"right_tyre": right_tyre, "left_tyre": left_tyre}


def test_one_reading_added_to_dict():
    car = Car()
    right_tyre = Tyre("right_tyre")
    car.add_tyre(right_tyre)
    car.add_tyre_readings("right_tyre", 25, 6.6)
    assert right_tyre._tyre_readings == {"right_tyre": [[25,6.6,"2025-06-17"]]}

    


def test_multiple_readings_added_to_dict():
    car = Car()
    front_right_tyre = Tyre("front_right_tyre")
    front_left_tyre = Tyre("front_left_tyre")
    back_left_tyre = Tyre("back_left_tyre")
    back_right_tyre = Tyre("back_right_tyre")
    car.add_tyre(front_right_tyre)
    car.add_tyre(front_left_tyre)
    car.add_tyre(back_left_tyre)
    car.add_tyre(back_right_tyre)
    car.add_tyre_readings("front_right_tyre", 25, 4)
    car.add_tyre_readings("front_left_tyre", 26, 6.6)
    car.add_tyre_readings("back_right_tyre", 22, 7.6)
    car.add_tyre_readings("back_left_tyre", 27, 3.6)
    assert car.show_tyres() == {"front_right_tyre": [25, 4,"2025-06-17"], "front_left_tyre": [26, 6.6,"2025-06-17"], "back_right_tyre": [22, 7.6,"2025-06-17"], "back_left_tyre": [27, 3.6, "2025-06-17"] }

    



def test_raises_error_given_no_readings():
    car = Car()

    with pytest.raises(Exception) as error:
        car.show_tyres()
    assert str(error.value) == "No readings been found!"




    


