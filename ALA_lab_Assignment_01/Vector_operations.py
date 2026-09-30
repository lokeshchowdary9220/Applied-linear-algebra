import random
import math
import sys
from typing import Self


"""
A custom vector class implementation for educational purposes.
"""

class Vec:
    # takes input elements which are int or float type only
    def __init__(self, src=None) -> None:
        if src is None:
            self.elements = []
        else:
            elements = list(src)
            for x in elements:
                if not isinstance(x, (int, float)):
                    raise TypeError(f"Scalar must be a number: {type(x)}")
            self.elements = elements

    def __add__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")
        if len(self.elements) != len(t):
            raise TypeError("Type error - vectors must be of same dimensions")
        return Vec([round(x + y, 5) for x, y in zip(self.elements, t.elements)])

    def __rmul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")
        return Vec([round(x * scalar, 5) for x in self.elements])

    def __imul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")
        for i, val in enumerate(self.elements):
            self.elements[i] = round(val * scalar, 5)
        return self

    def __repr__(self) -> str:
        return repr(self.elements)

    def __len__(self) -> int:
        return len(self.elements)

    def __sub__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")
        if len(self.elements) != len(t.elements):
            raise TypeError("Vectors must be of same dimensions")
        return Vec([x - y for x, y in zip(self.elements, t.elements)])

    def __neg__(self) -> Self:
        return Vec([-x for x in self.elements])

    def __radd__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError(f"Expected scalar: {type(other)}")
        return Vec([x + other for x in self.elements])

    def __iadd__(self, other: Self | int | float) -> Self:
        if isinstance(other, Vec):
            if len(self.elements) != len(other.elements):
                raise TypeError("Vectors must be of same dimensions")
            for i in range(len(self.elements)):
                self.elements[i] = round(self.elements[i] + other.elements[i], 5)
            return self
        elif isinstance(other, (int, float)):
            for i in range(len(self.elements)):
                self.elements[i] = round(self.elements[i] + other, 5)
            return self
        else:
            raise TypeError(f"Unsupported operand type for +=: {type(other)}")

    @classmethod
    def zeros(cls, n: int) -> Self:
        v = [0] * n
        return cls(v)

    @classmethod
    def ones(cls, n: int) -> Self:
        v = [1] * n
        return cls(v)

    @classmethod
    def uniform(cls, n: int) -> Self:
        return cls([random.uniform(0, 1) for _ in range(n)])

    def norm(self) -> float:
        return math.sqrt(sum(x * x for x in self.elements))

    def mean(self) -> float:
        return sum(self.elements) / len(self.elements)

    def demean(self) -> Self:
        vector_mean = self.mean()
        return Vec([x - vector_mean for x in self.elements])

    def std(self) -> float:
        demeaned_vector = self.demean()
        return math.sqrt(
            sum(x * x for x in demeaned_vector.elements) / len(demeaned_vector)
        )


if sys.version_info < (3, 8):
    sys.exit("Error: This script requires Python 3.8 or higher.")

if __name__ == "__main__":
    z1 = Vec.zeros(5)
    print("\n zero vector: ", z1)
    z2 = Vec.ones(3)
    print("\n unit vector: ", z2)
    v1 = Vec([0, 1, 1.03])
    print("\n Creating a new vector: ",v1)
    v3 = 5 * v1
    print("\nsclar and vector mulplication: ", v3)
    v5 = 1 + v3
    print("\nscalar and vector addition: ", v3)
    v2 = v1 + v3
    print("\n addition of 2 vectors: ", v2)
    v4 = v1 - v3
    print ("\n subtraction on two vectors: ", v4)
    print("\n Negation of a vector ", -(v2))
    uniform_vector = Vec.uniform(5)
    print("\n Uniform random vector:", uniform_vector)
    norm_result = v1.norm()
    print("\n Norm of Vector v1:", norm_result)