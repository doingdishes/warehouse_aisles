#defines the item class. 
#items are stored in aisles

class Item:

    def __init__(self, category, ORMD,):
        """
        Constructor to initialize instance attributes.
        """
        self.category = category
        self.ORMD = True

    def create_item(self):
        """
        Method performing an action using instance attributes.
        """
        return f"Method 1: {self.instance_attribute1}"

    def method2(self, parameter):
         """
         Method performing an action using instance attributes and parameters.
         """
         return f"Method 2: {self.instance_attribute2}, {parameter}"