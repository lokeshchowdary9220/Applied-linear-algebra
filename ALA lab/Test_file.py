# This file includes step 4 (Steps.txt)

from vec import Vec


# -------------------------
# Test vector creation
# -------------------------

v = Vec([1, 2, 3])
assert v.elements == [1, 2, 3]


# -------------------------
# Test vector addition
# -------------------------

v1 = Vec([1, 2, 3])
v2 = Vec([4, 5, 6])

result = v1 + v2
assert result.elements == [5, 7, 9]


# -------------------------
# Test vector subtraction
# -------------------------

result = v2 - v1
assert result.elements == [3, 3, 3]


# -------------------------
# Test scalar multiplication
# -------------------------

result = 2 * v1
assert result.elements == [2, 4, 6]


# -------------------------
# Test in-place multiplication
# -------------------------

v3 = Vec([1, 2, 3])
v3 *= 3

assert v3.elements == [3, 6, 9]


# -------------------------
# Test negation
# -------------------------

result = -v1
assert result.elements == [-1, -2, -3]


# -------------------------
# Test in-place addition
# -------------------------

v4 = Vec([1, 2, 3])
v4 += Vec([4, 5, 6])

assert v4.elements == [5, 7, 9]


# -------------------------
# Test zeros()
# -------------------------

result = Vec.zeros(5)

assert result.elements == [0, 0, 0, 0, 0]


# -------------------------
# Test ones()
# -------------------------

result = Vec.ones(4)

assert result.elements == [1, 1, 1, 1]


# -------------------------
# Test norm()
# -------------------------

v5 = Vec([3, 4])

assert v5.norm() == 5


# -------------------------
# Test dimension
# -------------------------

v6 = Vec([10, 20, 30, 40])

assert len(v6) == 4


print("All tests passed successfully!")