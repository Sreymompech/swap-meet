# Wave 1
from curses import beep
from nis import cat
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
class Vendor:
    """Parent class of Clothing, Decor, and Electronics"""

    # Wave 1
    def __init__(self, inventory = None):
        """Inventory is keyword argument that optionally pass in."""
        # assign empty list to inventory when the if statement is falsy. 
        # Otherwise, assign inventory as value of object's inventory.
        if not inventory:
            inventory = []
        self.inventory = inventory
        
        
    def add(self, item):
        """Adding new item into inventory and returns the added item."""
        self.inventory.append(item)
        return item


    def remove(self, item):
        """Removing item from inventory if it is matching the paramenter pass in and returns that removed item."""
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False


    # Wave 2
    def get_by_category(self, category):
        """Returnning list of items if matching the conditions, otherwise, return []"""
        items_list = []
        # adding item into the new list if the inventory is not empty and category was the input
        if len(self.inventory) > 0:
            for item in self.inventory:
                if item.category == category:
                    items_list.append(item)
            return items_list
        return []


    # Wave 3
    def swap_items(self, vendor, my_item, their_item):
        """Returning True if item been swapped between both inventories, otherwise, return False"""
        
        # make sure the both items that want to swap are in both inventories
        if my_item in self.inventory and their_item in vendor.inventory:
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            vendor.inventory.append(my_item)
            vendor.inventory.remove(their_item)
            return True
        return False
            

    # Wave 4
    def swap_first_item(self, vendor):
        """Returnning True if the first item of both inventories been swapped, otherwise, return False."""
        
        # make sure both inventories are not empty before swapping
        if len(self.inventory) > 0 and len(vendor.inventory) > 0:
            self.inventory[0], vendor.inventory[0] = vendor.inventory[0], self.inventory[0]
            return True
        return False


    # Wave 6
    def get_best_by_category(self, category):
        """Returning best item if matching conditions, otherwise, return False"""
        
        # if inventory is not empty then find the highest condition that is matching category for best item
        if len(self.inventory) > 0:
            for item in self.inventory:
                if item.category == category:
                    max_condi = max([item.condition for item in self.inventory if item.category == category])
                    if item.condition == max_condi: 
                        return item
        return None

    
    def swap_best_by_category(self, other, my_priority, their_priority ):
        """Swapping item by best item and returning invoked function swap_items() at the end."""
        
        # invoking method get_best_by_category() to find my best item and other best item.
        my_best_item = self.get_best_by_category(their_priority)
        other_best_item = other.get_best_by_category(my_priority)
        # invoking method swap_item() to swap item then return it
        return self.swap_items(other, my_best_item, other_best_item)


  





        