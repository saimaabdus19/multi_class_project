
from datetime import datetime

class Tyre():
    
    def __init__(self, position):
        self.position = position
        self._tyre_readings = {position: []}


    def add_reading(self, tyre_pressure, tyre_tread_depth):
        date = datetime.now().date()
        reading = []
        reading.append(tyre_pressure)
        reading.append(tyre_tread_depth)
        reading.append(str(date))
        
      
        
        
        self._tyre_readings[self.position].append(reading)
       
    

    