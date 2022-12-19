from typing import List


def sort(arr: List[int]) -> List[int]:
    arr_size = len(arr)
    is_sorted = False

    for i in range(arr_size):
        count = 0
        for j in range(1, arr_size - i):
            if arr[j] < arr[j - 1]:
                swap(arr, j, j - 1)
                is_sorted = True

        count += 1

        if not is_sorted:
            print(count)
            return arr

    return arr


def swap(arr: List[int], index_1: int, index_2: int) -> List[int]:
    arr[index_1], arr[index_2] = arr[index_2], arr[index_1]
