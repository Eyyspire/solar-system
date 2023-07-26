import math

class Vector:

    @classmethod   
    def type_error(cls):
        raise TypeError("Type error")

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, vector):
        """Two vectors are equal if all elements are equal

        :param vector: The other vector
        :return: True if the vectors are equal, false otherwise or if the parameter is not a vector.
        """
        return isinstance(vector, Vector) and self.x == vector.x and self.y == vector.y and self.z == vector.z

    def __add__(self, vector):
        """Add this vector with another one

        :param vector: The other vector
        :return: The new vector
        """
        return Vector(self.x + vector.x, self.y + vector.y, self.z + vector.z)
    
    def __iadd__(self, vector): 
        """Add this vector with another one

        :param vector: The other vector
        :return: The new vector
        """
        return Vector(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def __sub__(self, vector):
        """Substacte the vector by another one

        :param vector: The other vector
        :return: The new vector
        """
        return Vector(self.x - vector.x, self.y - vector.y, self.z - vector.z)

    def __mul__(self, other):
        """Does a scalar product if the parameter is a number, or a dot product if it is another vector

        :param other: A number (int, float, complex) or a Vector
        :return: The new vector
        """
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        if isinstance(other, (int, float, complex)):
            return Vector(other * self.x, other * self.y, other * self.z)

    def __imul__(self, other):
        """Does a scalar product if the parameter is a number, or a dot product if it is another vector

        :param other: A number (int, float, complex) or a Vector
        :return: The new vector
        """
        if isinstance(other, Vector):
            return Vector(self.x * other.x + self.y * other.y + self.z * other.z)
        if isinstance(other, (int, float, complex)):
            return Vector(other * self.x, other * self.y, other * self.z)

    def __truediv__(self, number):
        """Divide all elements of the vector by a number

        :param number: A number
        :return: The new vector
        """ 
        return Vector(self.x / number, self.y / number, self.z / number) 

    def __neg__(self):
        """Returns the vector with opposite values on each axis

        :return: the vector with opposite values on each axis
        """
        return Vector(-self.x, -self.y, -self.z)

    def __abs__(self):
        """Get the absolute value for each element of the vector

        :return: The new vector
        """
        return Vector(abs(self.x), abs(self.y), abs(self.z))

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __getitem__(self, key):
        """Get the axis corresponding to the given key

        :param key: a number
        :return:the corresponding axis
        """
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        elif key == 2:
            return self.z

    def __setitem__(self, key, value):
        """Set the axis corresponding to the given key

        :param key: the key corresponding to the axis
        :param value: the number to set
        """
        if type(key) != self.type : 
            Vector.type_error()
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        elif key == 2:
            self.z = value

    def magnitude(self):
        """Get the magnitude of the vector (its length)

        :return: The magnitude of the vector
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        """Gets the unary vector correponding to this one

        :return: The unary vector correponding to this one
        """
        magnitude = self.magnitude()
        if magnitude == 0:
            return self
        else:
            return self / self.magnitude()

    def orthogonal_2d(self, clockwise=False):
        if clockwise:
            x, y = self.y, -self.x
        else:
            x, y = -self.y, self.x
        return Vector(x, y, self.z)

    def multiplyComponents(self, vector):
        for i in range(3):
            self[i] *= vector[i]

    def round(self, decimals):
        for i in range(3):
            self[i] == round(self[i], decimals) 

    def to_float(self):
        return Vector(float(self.x), float(self.y), float(self.z))

    def to_int(self):
        return Vector(int(self.x), int(self.y), int(self.z))

    def tuple(self):
        return (self.x, self.y, self.z)
    
    def modulo(self, number):
        return (self.x % number, self.y % number, self.z % number)

