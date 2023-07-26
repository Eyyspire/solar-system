import math
import pytest

from src.Util.Vector import Vector

class TestVector:

    def setup_method(self):
        self.zero = Vector(0,0,0)
        self.zerosWith1 = Vector(0,0,1)
        self.v1 = Vector(1,2,3)
        self.v2 = Vector(2,2,5)
        
    def test_eqWorksFine(self):
        assert self.zero != self.v1
        assert self.zero != self.zerosWith1
        assert self.v1 == Vector(1,2,3)

    def test_addWorksFine(self):
        assert self.v1 + self.v2 == Vector(3,4,8)

    def test_subWorksFine(self):
        assert self.v1 - self.v2 == Vector(-1, 0, -2)

    def test_scalarProduct(self):
        assert self.v1 * self.zero == 0
        assert self.v1 * self.v2 == 21

    def test_numberProduct(self):
        assert self.v1 * 3 == Vector(3,6,9)

    def test_div(self):
        assert self.v2 / 2 == Vector(1.0, 1.0, 5/2)

    def test_neg(self):
        assert -self.v2 == Vector(-2, -2, -5)

    def test_magnitudeWorksFine(self):
        assert self.v2.magnitude(), math.sqrt(33)

    def test_normalize(self):
        assert self.v2.normalize() == Vector(self.v2[0]/math.sqrt(33), self.v2[1]/math.sqrt(33), self.v2[2]/math.sqrt(33))

    def test_orthogonal_2d(self):
        assert self.v1.orthogonal_2d() == Vector(-2, 1, 3)
        assert self.v2.orthogonal_2d(clockwise=True) == Vector(2,-2,5)


