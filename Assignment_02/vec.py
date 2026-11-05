
import math
import random
from gensim.models import KeyedVectors


class Vec:
    """A simple class for representing mathematical vectors."""

    def __init__(self, elements):
        """Create a vector from a list or tuple of numbers."""

        self.elements = tuple(float(x) for x in elements)

        for x in self.elements:
            if not isinstance(x, (int, float)):
                raise TypeError("Vector elements must be numbers.")

    def __add__(self, other):
        """Add two vectors element by element."""

        if not isinstance(other, Vec):
            raise TypeError("Can only add another Vec.")

        if len(self) != len(other):
            raise TypeError("Vectors must have the same dimensions.")

        result = []

        for x, y in zip(self.elements, other.elements):
            result.append(x + y)

        return Vec(result)

    def __sub__(self, other):
        """Subtract two vectors element by element."""

        if not isinstance(other, Vec):
            raise TypeError("Can only subtract another Vec.")

        if len(self) != len(other):
            raise TypeError("Vectors must have the same dimensions.")

        result = []

        for x, y in zip(self.elements, other.elements):
            result.append(x - y)

        return Vec(result)

    def __mul__(self, scalar):
        """Multiply vector by a scalar."""

        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number.")

        result = []

        for x in self.elements:
            result.append(x * scalar)

        return Vec(result)

    def __rmul__(self, scalar):
        """Allow scalar multiplication from the left."""

        return self * scalar

    def __imul__(self, scalar):
        """Multiply vector by a scalar in place."""

        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number.")

        self.elements = tuple(x * scalar for x in self.elements)

        return self

    def __neg__(self):
        """Return the negative of the vector."""

        return Vec([-x for x in self.elements])

    def __radd__(self, other):
        """Add a scalar to every element of the vector."""

        if isinstance(other, (int, float)):
            result = []
            for x in self.elements:
                result.append(x + other)
            return Vec(result)

        if isinstance(other, Vec):
            return other + self

        raise TypeError("Unsupported operand for addition.")
    
    def __iadd__(self, other):
        """Add another vector in place."""

        return self + other

    def __len__(self):
        """Return the number of elements."""

        return len(self.elements)

    def __repr__(self):
        """Return a readable representation."""

        return repr(self.elements)

    @staticmethod
    def zeros(n):
        """Create a vector containing n zeros."""

        return Vec([0] * n)

    @staticmethod
    def ones(n):
        """Create a vector containing n ones."""

        return Vec([1] * n)

    @staticmethod
    def uniform(n):
        """Create a vector with random values between 0 and 1."""

        return Vec([random.random() for _ in range(n)])

    def norm(self):
        """Calculate Euclidean norm."""

        total = 0

        for x in self.elements:
            total += x * x

        return math.sqrt(total)

    def __norm__(self):
        """Calculate vector norm."""

        return self.norm()

    def __mean__(self):
        """Calculate mean of vector elements."""

        if len(self) == 0:
            raise ValueError("Cannot calculate mean of empty vector.")

        return sum(self.elements) / len(self)

    def __demean__(self):
        """Subtract mean from every element."""

        mean = self.__mean__()

        result = []

        for x in self.elements:
            result.append(x - mean)

        return Vec(result)

    def __std__(self):
        """Calculate population standard deviation."""

        demeaned = self.__demean__()

        variance = sum(x * x for x in demeaned.elements) / len(self)

        return math.sqrt(variance)

    @staticmethod
    def load_model(path):
        """Load a GloVe word vector model."""

        return KeyedVectors.load(path)

    @staticmethod
    def __glove_vector__(word, model):
        """Retrieve a word embedding from the GloVe model."""

        if word not in model:
            raise KeyError("Word not found: " + word)

        return Vec([float(x) for x in model[word]])
