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
        self.total_value = 0
        self.total_weight = 0

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items: list):
        for item in new_items:
            if self.is_item_valid(item) and item.weight <= self.__capacity:
                self._items.append(item)
                self.total_value += item.value
                self.total_weight += item.weight

    @items.deleter
    def items(self):
        self._items = []
        self.total_value = 0
        self.total_weight = 0

    @classmethod
    def set_capacity(cls, capacity: int) -> None:
        cls.__capacity = capacity

    def add_item(self, item: Item) -> str:
        if not self.is_item_valid(item):
            return "Item is not valid"
        if self.__capacity >= self.total_weight + item.weight:
            self._items.append(item)
            self.total_weight += item.weight
            self.total_value += item.value
            return "Object added!"
        return f"Item '{item.name}' is too heavy for the backpack."

    def remove_item(self, item: Item) -> str:
        self._items.remove(item)
        self.total_value -= item.value
        self.total_weight -= item.weight
        return "Object successfully removed."

    @staticmethod
    def is_item_valid(item: Item) -> bool:
        return isinstance(item, Item) and item.weight >= 0 and item.value >= 0

    def __str__(self) -> str:
        item_word = "item" if len(self._items) in (0, 1) else "items"
        return f"Backpack contains {len(self._items)} {item_word} with total weight {self.total_weight} kg and total value ${self.total_value}"
