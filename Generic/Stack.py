class EmptyStackError(Exception):
    pass


class Stack:
    def __init__(self):
        self.stack = []
        self.__size = 0

    def top(self):
        if self.__size == 0:
            raise EmptyStackError
        return self.stack[0]

    def pop(self):
        if self.__size == 0:
            raise EmptyStackError
        self.__size -= 1
        return self.stack.pop(0)

    def push(self, obj):
        self.stack.insert(0, obj)
        self.__size += 1

    def is_empty(self) -> bool:
        return self.__size == 0

    def size(self) -> int:
        return self.__size
