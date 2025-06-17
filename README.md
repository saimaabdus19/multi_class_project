# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a car owner
So that I can keep a record of details about my tyres
I want to keep track of the tyres individually, by their position on my car

As a car owner
So that I have the two important pieces of data for a tyre
I want to be able to record both tyre pressure and tyre tread depth

As a car owner
So that I have a history of tyre readings
I want to be able to keep a record of historical readings, when those were, as well as current readings

As a car owner
So that I can see the details of my car at a glance
I want to list the tyres' positions, latest readings and when those were


## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
│ MusicPlayer                │
│                            │
│ - tracks                   │
│ - add(track)               │
│ - search_by_title(keyword) │
│   => [tracks...]           │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Track(title, artist)    │
│                         │
│ - title                 │
│ - artist                │
│ - format()              │
│   => "TITLE by ARTIST"  │
└─────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Car:
    # User-facing properties:
    #   tracks: list of instances of Track

    def __init__(self):
        pass # No code here yet
        self.car_dict = {}

    def add_tyre(self):
        # Parameters:
        #   track: add a tyre to the dict
        # Side-effects:
        #   Adds the track to the tracks property of the self object
        pass # No code here yet

    def add_tyre_readings(self, position):
        pass 
        

    def show_tyres(self):
        # Parameters:
        #   keyword: string
        # Returns:
        #   A dict of the car objects that have tyre readings for all 4 tyres 
        pass # No code here yet


class Tyre:
    # User-facing properties:
    #   title: string
    #   artist: string

    def __init__(self, position):
        # Parameters:
        #   title: string
        #   artist: string
        # Side-effects:
        #   Sets the title and artist properties
        pass # No code here yet
        self._tyre_readings = []

    def add_reading(self, tyre_pressure , tyre_tread_depth, current_date):
        # Returns:
        #   string of tyre position, pressure and tread depth
        pass # No code here yet

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given an instance
Test that is an instance of the class 
"""
tyre = Tyre()
isintance # => True 

"""
Given tyre readings
Test list returns tyre readings 
"""
tyre = Tyre("25", "4", "front_left")
tyre.add() # => ["25", "4", "front_left"]

"""
Given tyre readings
Return corrected formatted readings 
"""
tyre = Tyre("25", "4", "front_left")
tyre.add()
tyre.format() # => Tyre pressure: 25, tread depth 4 and positioned at front_left.

"""
Given multiple tyre readings of a single tyre 
Test list returns multiple readings 
"""
tyre = Tyre("front-right")
tyre.add("25", "4", "10/06/2020") # => ["25", "4", "10/06/2020" ]
tyre.add("24", "4", "12/06/2021") # => ["24", "4", "12/06/2021"]

"""
Given an instance
Test that is an instance of the class 
"""
car = Car()
car.car_dict = {}
isintance # => True 

"""
Given one tyre readings
Test to check if tyre been added to the car
"""

car = Car()
tyre = Tyre()
car.add_tyre("front_left") # => [{ left_tyre: [] }

"""
Given multiple tyre readings
Test to check if multiple readings been added to the car
"""

car = Car()
tyre = Tyre()
tyre2 = Tyre()
car.add_tyre("front_left") # => [{ left_tyre: [] }
car.add_tyre("front_right")  # => [ left_tyre: [], { right_tyre: []}

"""
Given a tyre reading 
Return the tyre reading addeded to the dictionary
"""
car = Car()
tyre = Tyre()
car.add_tyre("front_left")
car.add_tyre_readings("22", "1.5", "15/04/2022") # => [[{ left_tyre: ["22", "1.5", "12/06/2021"]}

"""
Given a car object
Return a dictionary with all the tyres readings
"""

car = Car()
tyre = Tyre()
car.add_tyre("front_left")
car.add_tyre("front_right")
car.add_tyre("back_right")
car.add_tyre("back_left")
car.show_tyres() # => [[{ left_tyre: ["22", "1.5", "12/06/2021"]}


```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
