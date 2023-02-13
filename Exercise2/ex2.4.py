import json
import timeit
import matplotlib.pyplot as plt

def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
    return array

with open('Exercise2/data.json') as f:
    data = json.load(f)
    times = []
    sizes = []
    for size in range(1, len(data)+1):
        array = data[:size]
        sizes.append(size)
        t = timeit.timeit(lambda: merge_sort(array), number=1)
        times.append(t)

    plt.plot(sizes, times)
    plt.xlabel('Array size')
    plt.ylabel('Time (seconds) e^-5')
    plt.title('Merge Sort Performance on Large Array')
    plt.show()
