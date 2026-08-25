# This file demonstrates Step 5 of your assignment

from vec import Vec


# Create two vectors
v1 = Vec([1, 2, 3])
v2 = Vec([4, 5, 6])


# Display vectors
print("v1 =", v1)
print("v2 =", v2)


# Vector addition
print("v1 + v2 =", v1 + v2)


# Vector subtraction
print("v1 - v2 =", v1 - v2)


# Scalar multiplication
print("2 * v1 =", 2 * v1)


# Negative vector
print("-v1 =", -v1)


# Vector dimension
print("Dimension of v1 =", len(v1))


# Vector norm
print("Norm of v1 =", v1.norm())


# Zero vector
print("Zero vector =", Vec.zeros(5))


# Ones vector
print("Ones vector =", Vec.ones(5))


# Random vector
print("Random vector =", Vec.uniform(5))

