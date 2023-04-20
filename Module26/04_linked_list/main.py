from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.link = None

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self) -> None:
        self.__head = None
        self.__cur_el = None
        self.__len = 0

    def __str__(self) -> str:
        return str([item.data for item in self.__iter__()])

    def __iter__(self) -> 'LinkedList':
        self.__cur_el = self.__head
        return self

    def __next__(self) -> Any:
        if self.__cur_el is None:
            raise StopIteration
        this = self.__cur_el
        self.__cur_el = self.__cur_el.link
        return this

    def append(self, item: Any) -> None:
        new_node = Node(item)
        if self.__head is None:
            self.__head = new_node
            self.__len += 1
            return
        last_node = self.__head
        while last_node.link:
            last_node = last_node.link
        last_node.link = new_node
        self.__len += 1

    def get(self, index: int) -> Any | None:
        if self.__len == 0 or self.__len <= index or index < 0:
            raise IndexError
        count = 0
        start_node = self.__head
        while count < index:
            if start_node.link is None:
                return None
            count += 1
            start_node = start_node.link
        return start_node

    def remove(self, index: int) -> None | Exception:
        if self.__len == 0 or self.__len <= index or index < 0:
            raise IndexError
        count = 0
        if index == 0:
            self.__head = self.__head.link
            self.__len -= 1
            return
        start_node = self.__head
        while start_node is not None and start_node.link is not None:
            if count == index - 1:
                start_node.link = start_node.link.link
                self.__len -= 1
                return
            else:
                start_node = start_node.link
            count += 1


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)

for el in my_list:
    print(el)

print('Получение третьего элемента:', my_list.get(2))

print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
