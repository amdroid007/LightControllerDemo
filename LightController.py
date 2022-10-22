"""
This is the lightcontroller demo class
"""
from CompositeLights import TrafficLight
from LED import LED

class LightController:

    def __init__(self) -> None:
        print("LightController constructor")

    def addLight(self, newlight):
        print("Add a new light to lightcontroller")


# Entry point of application
# can be in any file but you need to run that
# file
if __name__ == "__main__":
    # Create an instance of lightcontroller
    # and call some methods

    mylightcontroller = LightController()

    red = LED("red", 5)
    yellow = LED("yellow", 6) 
    green = LED("green", 7)

    mytrafficlight = TrafficLight(red, yellow, green)
    mylightcontroller.addLight(mytrafficlight)

    