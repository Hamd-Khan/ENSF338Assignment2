import timeit
import time
import matplotlib.pyplot as plt
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

def func_memo(n, memoized={}):
    if n == 0 or n == 1:
        return n
    if n not in memoized:
        memoized[n] = func_memo(n-1, memoized) + func_memo(n-2, memoized)
    return memoized[n]

def time_function(func, n):
    return timeit.timeit(f"{func}({n})", globals=globals(), number=1)




if __name__ == '__main__':

    original_times = []
    optimized_times = []
    for n in range(36):
        original_times.append(time_function("func", n))
        optimized_times.append(time_function("func_memo", n))

    plt.plot(original_times, label="original")
    plt.plot(optimized_times, label="optimized")
    plt.legend()
    plt.xlabel("Input size (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Comparison of original and optimized code")
    plt.show()

