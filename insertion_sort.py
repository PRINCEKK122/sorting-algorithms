from typing import List


def insert_sort(numbers: List[int]) -> List[int]:
    for i in range(1, len(numbers)):
        current = numbers[i]

        j = i - 1
        while (j >= 0) and (numbers[j] > current):
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = current

    return numbers
