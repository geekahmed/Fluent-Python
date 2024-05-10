import math

class Vector:
    def __init__(self, x=0, y=0) -> None:
        self.__x = x
        self.__y = y
    
    def __repr__(self) -> str:
        return f'Vector({self.__x!r}, {self.__y!r})'
    
    def __abs__(self):
        return math.hypot(self.__x, self.__y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.__x + other.__x
        y = self.__y + other.__y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.__x * scalar, self.__y * scalar)
    
    def __rmul__(self, scalar):
        return Vector(self.__x * scalar, self.__y * scalar)
    
v1 = Vector(1,2)
v2 = Vector(1,2)
print(5*v1*5)


class X:
    def __init__(self, x) -> None:
        self.__x = x
    
    def __repr__(self) -> str:
        return f'X value is {self.__x!r}'
    

print(X(25))