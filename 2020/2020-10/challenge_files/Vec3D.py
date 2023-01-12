import math

class Vec3D:
    
    __slots__ = 'x', 'y', 'z'
    
    def __init__(self, x, y=None, z=None):
        if y is None:
            self.x, self.y, self.z = x
        else:
            self.x = x
            self.y = y
            self.z = z
    
    def __repr__(self):
        return f'Vec3D({repr(self.x)}, {repr(self.y)}, {repr(self.z)})'
    
    def __str__(self):
        return f'[{self.x}, {self.y}, {self.z}]'
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __add__(self, other):
        return Vec3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vec3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __neg__(self):
        return Vec3D(-self.x, -self.y, -self.z)
    
    def __mul__(self, other):
        if isinstance(other, Vec3D):
            return self.x * other.x + self.y * other.y + self.z * other.z
        return Vec3D(self.x * other, self.y * other, self.z * other)
    
    def __rmul__(self, other):
        return self * other
    
    def __matmul__(self, other):
        return Vec3D(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

    def __truediv__(self, other):
        return Vec3D(self.x / other, self.y / other, self.z / other)
    
    def __floordiv__(self, other):
        return Vec3D(self.x // other, self.y // other, self.z // other)
    
    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def norm(self):
        return self / abs(self)
    
    def __bool__(self):
        return bool(self.x or self.y or self.z)
    
    def __getitem__(self, index):
        if index == 0 or index == 'x':
            return self.x
        if index == 1 or index == 'y':
            return self.y
        if index == 2 or index == 'z':
            return self.z
        raise IndexError
