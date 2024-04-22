import turtle as t

class Molecule:
    def __init__(self, x: int, y: int, mass: float, velocx: int, velocy: int):
        self.__mass = mass
        self.__velocx = velocx
        self.__velocy = velocy
        self.__x = x
        self.__y = y

    @property
    def mass(self):
        return self.__mass
    
    @property
    def velocx(self):
        return self.__velocx
    
    @property
    def velocy(self):
        return self.__velocy
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def velocx(self, value: int):
        self.__velocx = value
    
    @velocy.setter
    def velocy(self, value: int):
        self.__velocy = value
    
    @x.setter
    def x(self, x: int):
        self.__x = x
    
    @y.setter
    def y(self, y: int):
        self.__y = y
    
    def idraw(self):
        t.teleport(self.x, self.y)
        t.dot(1, "black")

    def move(self):
        self.__x += self.__velocx
        self.__y += self.__velocy

    def collis(self, other):
        return
