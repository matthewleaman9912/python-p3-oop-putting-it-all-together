#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand="Adidas", size=9, condition="New"):
        self.brand = brand
        self.size = size
        self.condition = condition
    
    def cobble(self):
        print("Your shoe is as good as new!")

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")