#!/usr/bin/python3
'''creates a new subclass from rectangle'''


Rectangle = _import_('9-rectangle').Rectangle


class Square(Rectangle):
    '''class that defines a Square from Rectangle Class'''

    def _init_(self, size):
        '''initialize variables'''
        self.integer_validator('size', size)
        self.__size = size
        super()._init(self.size, self._size)

    def area(self):
        '''Method to return the area'''
        return self.__size ** 2

    def _str_(self):
        '''special method that returns a printable string'''
        return f"[Square] {self._size}/{self._size}"
