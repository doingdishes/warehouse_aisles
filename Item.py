#defines the item class. 
#items are stored in aisles
#need to work on CRUD commands

class Item:

    def __init__(self, name, count, ORMD, sku):
        """
        the item class defines the stockable goods
        in each aisle object
        goal is to be able to perform
        CRUD operations on items
        """
        self.name = str(name) #name of the item
        self.count = int(count) #quantity/count of the item
        self.sku = str(sku) #Stock Keeping Unit number
        self.ORMD = True

    def create_item(self, name, count, sku):
        """
        Method that creates an item object
        """
        item_name = str(input('Item Name: '))
        item_count = int(input('Item Count (as an integer): '))
        item_sku = str(input('Item SKU (as an integer): '))
        return item_name, item_count, item_sku

    def read_item(self, name, count, sku):
         """
         Method that reports the name and count of the item
         """
    
    def update_item(self, name, count, sku):
        """
        method that updates either the name or count of the item
        """
        return f""

    def delete_item(self, name, count, sku):
        """
        removes an item from the database
        """