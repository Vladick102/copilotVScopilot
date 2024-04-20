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

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items: list):
        for item in new_items:
            if self.is_item_valid(item) and item.weight <= self.__capacity:
                self._items.append(item)

    @items.deleter
    def items(self):
        self._items = []

    @property
    def total_value(self):
        return sum(i.value for i in self._items)

    @property
    def total_weight(self):
        return sum(i.weight for i in self._items)

    @classmethod
    def set_capacity(cls, capacity: int) -> None:
        cls.__capacity = capacity

    def add_item(self, item: Item) -> str:
        if not self.is_item_valid(item):
            return "Item is not valid"
        if self.__capacity >= self.total_weight + item.weight:
            self.items.append(item)
            return "Object added!"
        return f"Item '{item.name}' is too heavy for the backpack."

    def remove_item(self, item: Item) -> str:
        self.items.remove(item)
        return "Object succesfully removed."

    @staticmethod
    def is_item_valid(item: Item) -> bool:
        return isinstance(item, Item) and item.weight >= 0 and item.value >= 0

    def __str__(self) -> str:
        item_word = "item" if len(self.items) <= 1 else "items"
        return f"Backpack contains {len(self.items)} {item_word} with total weight {self.total_weight} kg and total value ${self.total_value}"
