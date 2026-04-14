
#Quicksort [Lomuto Algorithm with partition]
def partition(arr, low, high):

    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
 if low < high:
    pi = partition(arr, low, high)

    quicksort(arr, pi + 1, high)
    quicksort(arr, low, pi - 1)

arr = [10, 392, 930, 20,77, 8,9,39,47,72,92]

quicksort(arr, 0, len(arr) - 1)

print(f"sorted array is: {arr}")




# The Quicksort which decreases the possiblity of worst case of the time complexity
import random
def random_index(arr, low, high):
   r = random.randint(low, high)

   arr[r], arr[high] = arr[high], arr[r]


def partition2(arr, low, high):
    

    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort2(arr, low, high):
 if low < high:
    random_index(arr,low, high)
    pi = partition2(arr, low, high)

    quicksort2(arr, pi + 1, high)
    quicksort2(arr, low, pi - 1)

arr = [10, 392, 930, 20,77, 8,9,39,47,72,92]

quicksort2(arr, 0, len(arr) - 1)

print(f"sorted array is: {arr}")
