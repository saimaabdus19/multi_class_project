from lib.tyre import *



def test_tyre_instance():
    tyre = Tyre("front_right")
    isinstance(tyre, Tyre)


def test_returns_one_reading():
    tyre = Tyre("front_tyre")
    tyre.add_reading(20,5)
    assert tyre._tyre_readings == {"front_tyre": [[20,5, "2025-06-17"]]}

    

def test_returns_multiple_readings():
    tyre = Tyre("front_tyre")
    tyre.add_reading(20,5)
    tyre.add_reading(10,8)
    assert tyre._tyre_readings == {"front_tyre": [[20,5,"2025-06-17"], [10,8,"2025-06-17"] ]}
