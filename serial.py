"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    Attributes:
        start - starting serial number
        serial - current serial number
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    def __init__(self, start = 100):
        self.start = start
        self.serial = start
    @classmethod
    def __str__(self):
        return f"Intial serial number {self.start} - current serial number {self.serial}"
    
    @classmethod
    def __repr__(self):
        return f"start: [{self.start}], serial: [{self.serial}]"

    def generate(self):
        """Prints current serial updates the next serial number"""
        print(self.serial)
        self.serial +=1
    
    def reset(self):
        """sets the serial number to the intial serial number"""
        self.serial = self.start

    


