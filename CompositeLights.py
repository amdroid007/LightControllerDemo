"""
The composite lights - this has the definiteion of the
Compositelight, Pixel and TrafficLight classes
"""
# If you need classes from other files,
# you have to import them
from LED import LED, DimmableLED

"""
The compositelight superclass
"""
class CompositeLight:
    def __init__(self) -> None:
        # this is not needed now, but just to show you 
        # how you create associations
        self._lights = [] # an array to hold the lights

    """
    The sequence method will be overridden
    by subclasses, so we don't need too much now
    """
    def sequence(self):
        pass

"""
TrafficLight as a subclass of compositelight
For now, just create the class, methods, and put
some print statements.
"""
class TrafficLight(CompositeLight):
    # constructor needs to send the red, yellow green
    def __init__(self, red, yellow, green):
        super().__init__()
        # again not needed for this assignment
        # but here is how you can add things to the array
        self._lights.append(red)
        self._lights.append(yellow)
        self._lights.append(green)

    def stop():
        print("Turn traffic light red")

    def caution():
        print("Turn traffic light yellow")

    def go():
        print("Turn traffic light green")

"""
Pixel subclass of compositelight
"""
class Pixel(CompositeLight):

    # Constructor of pixel
    def __init__(self, R, G, B):
        super().__init__()
        self._lights.append(R)
        self._lights.append(G)
        self._lights.append(B)

    # defColor Mehtod
    def setColor(self, rr, gg, bb):
        print("Set the color of the pixel to specific values")
        
