# This file includes steps 6 and 8 (Steps.txt)

import timeit

from vec import Vec


# Vector sizes required by the assignment
sizes = [2000, 4000, 8000, 16000, 32000, 64000]


for n in sizes:

    print("\n------------------------------")
    print(f"Vector dimension: {n}")
    print("------------------------------")

    # Create two random vectors
    v1 = Vec.uniform(n)
    v2 = Vec.uniform(n)

    # Addition
    addition_time = timeit.timeit(
        lambda: v1 + v2,
        number=10
    )

    # Subtraction
    subtraction_time = timeit.timeit(
        lambda: v1 - v2,
        number=10
    )

    # Scalar multiplication
    multiplication_time = timeit.timeit(
        lambda: 2 * v1,
        number=10
    )

    # Norm
    norm_time = timeit.timeit(
        lambda: v1.norm(),
        number=10
    )

    print(f"Addition:       {addition_time:.8f} seconds")
    print(f"Subtraction:    {subtraction_time:.8f} seconds")
    print(f"Multiplication: {multiplication_time:.8f} seconds")
    print(f"Norm:            {norm_time:.8f} seconds")