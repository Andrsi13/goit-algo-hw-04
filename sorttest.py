import timeit
import random
from copy import deepcopy


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key 
    return arr

def timesort(arr):
    sorted_arr = sorted(arr)
    return sorted_arr


def measure_sort_time(sort_func, arr):
    time_taken = timeit.timeit(lambda: sort_func(arr.copy()), number=100)
    return time_taken




def main():
    #різні масиви даних
    sizes = [10, 100, 1000]
    for size in sizes:

        arr = [random.randint(0, 10000) for i in range(size)]
        print(f"\nРозмір масиву: {size}")
        a = deepcopy(arr)


        
        time_taken_merge_sort = measure_sort_time(merge_sort, a)
        time_taken_insertion_sort = measure_sort_time(insertion_sort, a)
        time_taken_timesort = measure_sort_time(timesort, a)


        print(f"Час виконання методом злиття: {time_taken_merge_sort}")
        print(f"Час виконання методом вставок: {time_taken_insertion_sort}")
        print(f"Час виконання методом Timesort: {time_taken_timesort}")





if __name__ == "__main__":
    main()
