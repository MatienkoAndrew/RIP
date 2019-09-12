from abc import ABC, abstractmethod
import math
#import sys
# sys.path.insert(1, '/lab_python_oop/Rectangle.py')
# import lab_python_oop

# Абстрактный класс "Геометрическая фигура"
class Geometric_figure(ABC):
    def __init__(self, name):
        self.name = name
        pass

    @abstractmethod
    def area(self):
        pass
    pass


# Класс «Цвет фигуры» содержит свойство для описания цвета геометрической фигуры
class ColorFigure:
    def __init__(self, color):
        self._color = color
        pass

    def getx(self):
        return self._color
        pass

    def setx(self, color):
        self._color = color
        pass
    
    def delx(self):
        del self._color
        pass

    _color = property(getx, setx, delx, "New Color")
    pass

# Класс «Прямоугольник» наследуется от класса «Геометрическая фигура»
class Rectangle(Geometric_figure):
    def __init__(self, width, high, color):
        super().__init__("Rectangle")
        self._width = width
        self._high = high
        # self._color = ColorFigure(color)
        pass
    
    def area(self):
        return self._width * self._high
        pass
    
    def repr(self):
        print("Area of {0} : {1}".format(self.name, self.area()))
        pass
    pass

# Класс Круг
class Circle(Geometric_figure):
    def __init__(self, radius, color):
        super().__init__("Circle")
        self.radius = radius
        # self.color = ColorFigure(color)
        pass

    def area(self):
        return math.pi * self.radius
        pass
    
    def repr(self):
        print("Area of {0} : {1}".format(self.name, self.area()))
        pass
    pass


# Класс Квадрат
class Square(Rectangle):
    def __init__(self, x, name):
        self.x = x
        self.name = name
        pass
    
    def setName(self):
        return self.name
        pass
    
    def area(self):
        return self.x * self.x
        pass

    def repr(self):
        print("Area of {0} : {1}".format(self.setName(), self.area()))
        pass
    pass


a = Rectangle(3, 2, "Dark blue")
a.repr()

b = Circle(5, "Green")
b.repr()

c = Square(5, "Square")
c.repr()

