"""
The LED Class and its DimmableLED subclass
"""
class LED:
    def __init__(self, color, pin) -> None:
        self._color = color # _color is the attribute
        self._pin = pin   # custom is to put a _ in front to indicate private
        print(f"Adding a {color} LED on pin {pin}")

    """
    Turn on the LED
    """
    def turnOn(self):
        print(f"Turn on the {self._color} LED")

    """
    Turn off the LED
    """
    def turnOff(self):
        print(f"Turn off the {self._color} LED")

    """
    Blink the LED
    """
    def blink(self):
        print(f"Blinking the {self._color} LED")

"""
Dimmable LED subclass of the LED class
"""
class DimmableLED(LED):
    # constructor - needs to call superclass constructor
    def __init__(self, color, pin, brightness):
        super().__init__(color, pin) # call superclass constructor
        self._brightness = brightness

    """
    Set brightness method - set the brighness of the
    LED to a certain level
    """
    def setBrightness(self, level):
        self._brightness = level
        print("Set the brightness of the LED")
