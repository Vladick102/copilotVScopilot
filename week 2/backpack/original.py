class Item:
    def __init__(self, name: str, weight: int, value: int) -> None:
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self) -> str:
        return f"{self.name} ({self.weight} kg, ${self.value})"

    def __repr__(self) -> str:
        return self.name


class Backpack:
    __capacity = 10

    def __init__(self) -> None:
        self._items = []
        self.total_value = sum(n.value for n in self._items)
        self.total_weight = 0

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items: list):
        for item in new_items:
            try:
                if self.is_item_valid(item) and item.weight <= self.__capacity:
                    self._items.append(item)
            except ValueError:
                continue
        self.total_value = sum(i.value for i in self._items)

    @items.deleter
    def items(self):
        self._items = []

    @classmethod
    def set_capacity(cls, capacity: int) -> None:
        cls.__capacity = capacity

    def add_item(self, item: Item) -> str:
        if not isinstance(item, Item):
            return "Item is not valid"
        if self.__capacity >= self.total_weight + item.weight:
            self.items.append(item)
            self.total_weight += item.weight
            self.total_value += item.value
            return "Object added!"
        return f"Item '{item.name}' is too heavy for the backpack."

    def remove_item(self, item: Item) -> str:
        self.items.remove(item)
        self.total_value -= item.value
        self.total_weight -= item.weight
        return "Object succesfully removed."

    @staticmethod
    def is_item_valid(item: Item) -> bool:
        if not isinstance(item, Item) or item.weight < 0 or item.value < 0:
            return False
        return True

    def __str__(self) -> str:
        if len(self.items) in (0, 1):
            return f"Backpack contains {len(self.items)} item with total weight \
{sum(w.weight for w in self.items)} kg and total value ${sum(v.value for v in self.items)}"
        return f"Backpack contains {len(self.items)} items with total weight \
{sum(w.weight for w in self.items)} kg and total value ${sum(v.value for v in self.items)}"
