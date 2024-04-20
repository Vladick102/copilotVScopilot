"""Backpack"""
class Item:
    """
    Create an item for your backpack.
    """
    def __init__(self, name: str, weight: int, value: int) -> None:
        """
        Get name, weight and value for an item.
        """
        self.name = name
        self.weight = weight
        self.value = value
    def __str__(self) -> str:
        """
        Returns the information about item in readable
        for user way.
        """
        return f'{self.name} ({self.weight} kg, ${self.value})'
    def __repr__(self) -> str:
        """
        Return normal representation for an item.
        """
        return self.name

class Backpack:
    """
    Create a backpack with items.
    """
    __capacity = 10
    # items = []
    def __init__(self) -> None:
        """
        Get items to a backpack and count their total
        value and weight.
        """
        # self.__capacity = 0
        self._items = []
        self.total_value = sum(n.value for n in self._items)
        self.total_weight = 0
    @property
    def items(self):
        """
        Get protected list of items.
        """
        return self._items
    @items.setter
    def items(self, new_items: list):
        """
        Create a list of items with already done list
        and check all the items in it.
        """
        for item in new_items:
            try:
                if self.is_item_valid(item) and item.weight <= self.__capacity:
                    self._items.append(item)
            except ValueError:
                continue
        self.total_value = sum(i.value for i in self._items)
    @items.deleter
    def items(self):
        """
        Delete all the items in backpack.
        """
        self._items = []
    @classmethod
    def set_capacity(cls, capacity: int) -> None:
        """
        Set a particular capacity of weight to backpack.
        """
        cls.__capacity = capacity
    def add_item(self, item: Item) -> str:
        """
        Check whether item is valid. If so, add it to
        backpack.
        """
        if not isinstance(item, Item):
            return 'Item is not valid'
        if self.__capacity >= self.total_weight + item.weight:
            self.items.append(item)
            self.total_weight += item.weight
            self.total_value += item.value
            return "Object added!"
        return f"Item '{item.name}' is too heavy for the backpack."
    def remove_item(self, item: Item) -> str:
        """
        Remove an item from backpack.
        """
        self.items.remove(item)
        self.total_value -= item.value
        self.total_weight -= item.weight
        return "Object succesfully removed."
    @staticmethod
    def is_item_valid(item: Item) -> bool:
        """
        Check whether item has specific class and whether
        its weight and value are real.
        """
        if not isinstance(item, Item) or item.weight < 0 or item.value < 0:
            return False
        return True
    def __str__(self) -> str:
        """
        Return the information about backpack in readable
        for user way.
        """
        if len(self.items) in (0, 1):
            return f'Backpack contains {len(self.items)} item with total weight \
{sum(w.weight for w in self.items)} kg and total value ${sum(v.value for v in self.items)}'
        return f'Backpack contains {len(self.items)} items with total weight \
{sum(w.weight for w in self.items)} kg and total value ${sum(v.value for v in self.items)}'
