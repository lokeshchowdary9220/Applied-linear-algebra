from Vector_operations import Vec
import timeit


sizes = [2000, 4000, 8000, 16000, 32000, 64000]

print("Performance Benchmark")
print("-" * 70)

for n in sizes:
    v1 = Vec([1.0] * n)
    v2 = Vec([2.0] * n)

    print(f"\nVector size: {n}")

    time_add = timeit.timeit(lambda: v1 + v2, number=100)
    time_sub = timeit.timeit(lambda: v1 - v2, number=100)
    time_neg = timeit.timeit(lambda: -v1, number=100)
    time_mul = timeit.timeit(lambda: 5 * v1, number=100)
    time_radd = timeit.timeit(lambda: 5 + v1, number=100)
    time_norm = timeit.timeit(lambda: v1.norm(), number=100)
    time_mean = timeit.timeit(lambda: v1.mean(), number=100)
    time_demean = timeit.timeit(lambda: v1.demean(), number=100)
    time_std = timeit.timeit(lambda: v1.std(), number=100)

    print(f"Addition:              {time_add / 100:.8f} seconds")
    print(f"Subtraction:           {time_sub / 100:.8f} seconds")
    print(f"Negation:              {time_neg / 100:.8f} seconds")
    print(f"Scalar multiplication: {time_mul / 100:.8f} seconds")
    print(f"Scalar + vector:       {time_radd / 100:.8f} seconds")
    print(f"Norm:                  {time_norm / 100:.8f} seconds")
    print(f"Mean:                  {time_mean / 100:.8f} seconds")
    print(f"Demean:                {time_demean / 100:.8f} seconds")
    print(f"Standard deviation:    {time_std / 100:.8f} seconds")