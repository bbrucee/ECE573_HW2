import sys
import os


def insertion_sort(input_array):
    comparisons = 0
    for i in range(1, len(input_array)):
        key = input_array[i]
        j = i-1
        while j >= 0 and key < input_array[j]:
            comparisons += 1
            input_array[j+1] = input_array[j]
            j -= 1
        comparisons += 1
        input_array[j+1] = key
    return comparisons

# https://www.geeksforgeeks.org/quick-sort/
# https://stackoverflow.com/questions/50912873/python-quicksort-with-median-of-three


def median_of_three(input_array, left, right):
    middle = (left + right - 1) // 2
    a = input_array[left]
    b = input_array[middle]
    c = input_array[right - 1]
    if a <= b <= c:
        return b, middle
    if c <= b <= a:
        return b, middle
    if a <= c <= b:
        return c, right - 1
    if b <= c <= a:
        return c, right - 1
    return a, left


def partition(input_array, left, right):
    pivot, pivot_index = median_of_three(input_array, left, right)
    input_array[left], input_array[pivot_index] = input_array[pivot_index], input_array[left]
    i = left + 1
    for j in range(left + 1, right):
        if input_array[j] < pivot:
            input_array[i], input_array[j] = input_array[j], input_array[i]
            i += 1
    input_array[left], input_array[i - 1] = input_array[i - 1], input_array[left]
    return i - 1


def quicksort(input_array, left, right):
    if left < right:
        partition_index = partition(input_array, left, right)
        quicksort(input_array, left, partition_index)
        quicksort(input_array, partition_index + 1, right)


def quicksort_insertion_cutoff(input_array, left, right, cutoff=7):
    if left < right:
        if right - left < cutoff:
            insertion_sort(input_array)
            return
        partition_index = partition(input_array, left, right)
        quicksort_insertion_cutoff(input_array, left, partition_index)
        quicksort_insertion_cutoff(input_array, partition_index + 1, right)


def main():
    pass
    # try:
    #     # https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
    #     rel_path = sys.argv[1]
    #     cwd = os.getcwd()
    #     abs_file_path = cwd + rel_path
    #     print("Input data file: {}".format(abs_file_path))
    #     file = open(abs_file_path)
    #     data_array = []
    #     for line in file.readlines():
    #         data_array.append(int(line))
    #     print("Input data: {}".format(data_array))
    #     file.close()
    #     print("Fastest 3 Sum algorithm finds {} triples".format(fastest_3sum(data_array)))
    #
    # except IndexError:
    #     print("No input data file")


if __name__ == '__main__':
    main()
