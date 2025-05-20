#defines the aisle class

class Aisle:

    def __init__(self, instance_attribute1, instance_attribute2):
        """
        Constructor to initialize instance attributes.
        """
        self.instance_attribute1 = instance_attribute1
        self.instance_attribute2 = instance_attribute2

    def method1(self):
        """
        Method performing an action using instance attributes.
        """
        return f"Method 1: {self.instance_attribute1}"

    def method2(self, parameter):
         """
         Method performing an action using instance attributes and parameters.
         """
         return f"Method 2: {self.instance_attribute2}, {parameter}"