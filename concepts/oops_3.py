"""

    MRO - Method Resolution Order (From Left -> Right based) (C3 Algorithm)
    __bases__ ==> <baseclass1, baseclass2>
    __mro__ ==> <class, baseclass1, baseclass2, parent_to_baseclass1, parent_to_baseclass2,........... , object>
    super() ==> Next class In the __mro__ order ( after matching implementation class in __mro__ order)

"""


class SimpleList(object):
    def __init__(self, items) -> None:
        self.items = list(items)

    def add(self, item) -> None:
        self.items.append(item)

    def delete(self, item):
        if item in self.items:
            self.items.remove(item)

    def get(self, idx) -> int:
        if 0 < idx < len(self.items):
            return self.items[idx]
        return -1

    def size(self) -> int:
        return len(self.items)

    def is_exists(self, item) -> bool:
        return item in self.items

    def sort(self, is_descending=False):
        self.items.sort(reverse=is_descending)

    def __repr__(self):
        return f"{type(self).__name__}({self.items!r})"


class SortedList(SimpleList):

    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item) -> None:
        super(SortedList, self).add(item)
        self.sort()


class IntList(SimpleList):

    def __init__(self, items=()):
        for item in items:
            self._validate(item)
        super().__init__(items)

    @staticmethod
    def _validate(item):
        if not isinstance(item, int):
            raise TypeError("Supports only Integers")

    def add(self, item) -> None:
        self._validate(item)
        super().add(item)


class SortedIntList(IntList, SortedList):
    pass
