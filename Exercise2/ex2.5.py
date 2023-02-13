import random
import json
import sys
import json
import time
import matplotlib.pyplot as plt

with open('data.json', 'r') as file:
    data = json.load(file)

for piece in data:
    random.shuffle(piece)

with open("ex2.5.json", "w") as file:
    json.dump(data, file)



sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]
    return high







with open('ex2.5.json', 'r') as file:
    data = json.load(file)


timing_results = []
for array in data:
    start = time.time()
    func1(array, 0, len(array)-1)
    end = time.time()
    timing_results.append(end - start)

print("Quick Sort Timing Results: ",timing_results," Secconds.")
plt.plot(timing_results)
plt.xlabel('Input number')
plt.ylabel('Time taken (s)')
plt.title('QuickSort Timing Results')
plt.show()


