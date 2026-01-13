from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Elipse(Shape):
    def draw(self):
        print("This is an elipse.")

    def __str__(self):
        return "Elipse's STR"
    
    def __repr__(self):
        return "ECLIPse"

class Rectangle(Shape):
    def __init__(self, r, c, char="X"):
        self.r = r 
        self.c = c
        self.char = char


    def draw(self):
        i = 0
        while i<self.r:
            for j in range(self.c):
                print(self.char, end="")
            print("")
            i+=1
    def __str__():
        return "STR: This is a rectangle"
    
    def __repr__(self):
        return "RECTangle"

# ob1 = Elipse()
# ob1.draw()
# ob2 = Rectangle(5, 7)
# ob2.draw()

class Square(Rectangle):
    def __init__(self, r, c, char="%"):
        if not(r==c):
            raise ValueError("Enter valid sides for a square")
        super().__init__(r,c,char)

    def __str__(self):
        return "STR: This is a square"
    
    def __repr__(self):
        return "SQuare"

sq = Square(5, 5)
sq.draw()
print(sq.__repr__())
print(Rectangle.__str__())
    
