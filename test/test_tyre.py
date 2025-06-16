from lib.tyre import *



def test_tyre_instance():
    tyre = Tyre("front_right")
    isinstance(tyre, Tyre)


def test_returns_one_reading():
    tyre = Tyre("front_tyre")
    tyre.add_reading(20,5,"10/06/2025")
    assert tyre._tyre_readings == {"front_tyre": [[20,5,"10/06/2025"]]}

    

def test_returns_multiple_readings():
    tyre = Tyre("front_tyre")
    tyre.add_reading(20,5,"10/06/2025")
    tyre.add_reading(10,8, "06/06/2025")
    assert tyre._tyre_readings == {"front_tyre": [[20,5,"10/06/2025"], [10,8, "06/06/2025"] ]}
