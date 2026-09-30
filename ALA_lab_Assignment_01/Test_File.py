import math

from Vector_operations import Vec


# Constructor, length and representation
v1 = Vec([1, 2, 3])
assert v1.elements == [1, 2, 3]
assert len(v1) == 3
assert repr(v1) == "[1, 2, 3]"

# Vector addition
v2 = Vec([4, 5, 6])
assert (v1 + v2).elements == [5, 7, 9]

# Scalar multiplication
assert (2 * v1).elements == [2, 4, 6]

# In-place scalar multiplication
v3 = Vec([1, 2, 3])
v3 *= 2
assert v3.elements == [2, 4, 6]

# Vector subtraction
assert (v2 - v1).elements == [3, 3, 3]

# Vector negation
assert (-v1).elements == [-1, -2, -3]

# Scalar addition
assert (5 + v1).elements == [6, 7, 8]

# In-place vector addition
v4 = Vec([1, 2, 3])
v4 += Vec([4, 5, 6])
assert v4.elements == [5, 7, 9]

# In-place scalar addition
v4 += 1
assert v4.elements == [6, 8, 10]

# Factory methods
assert Vec.zeros(3).elements == [0, 0, 0]
assert Vec.ones(3).elements == [1, 1, 1]

random_vector = Vec.uniform(5)
assert len(random_vector) == 5
assert all(0 <= x <= 1 for x in random_vector.elements)

# Euclidean norm
assert Vec([3, 4]).norm() == 5

# Mean
assert Vec([1, 2, 3, 4, 5]).mean() == 3

# De-meaned vector
original_vector = Vec([1, 2, 3, 4, 5])
demeaned_vector = original_vector.demean()
assert demeaned_vector.elements == [-2, -1, 0, 1, 2]
assert math.isclose(demeaned_vector.mean(), 0)
assert original_vector.elements == [1, 2, 3, 4, 5]

# Standard deviation
std_vector = Vec([2, 4, 4, 4, 5, 5, 7, 9])
assert math.isclose(std_vector.std(), 2)
assert Vec([5, 5, 5]).std() == 0

print("All vector tests passed.")