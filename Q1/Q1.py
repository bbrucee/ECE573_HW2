import sys
import os


# https://www.geeksforgeeks.org/insertion-sort/
# Input is any length array
# After function call array is sorted
# Returns number of comparisons
def insertion_sort(input_array):
    comparisons = 0
    for i in range(1, len(input_array)):
        key = input_array[i]
        j = i - 1
        while j >= 0 and key < input_array[j]:
            comparisons += 1
            input_array[j + 1] = input_array[j]
            j -= 1
        comparisons += 1
        input_array[j + 1] = key
    return comparisons


# https://www.geeksforgeeks.org/python-program-for-shellsort/
# Input is any length array
# After function call array is 7-sorted
# Returns number of comparisons
def shell7(input_array):
    comparisons = 0
    for i in range(7, len(input_array)):
        key = input_array[i]
        j = i
        while j >= 7 and input_array[j - 7] > key:
            comparisons += 1
            input_array[j] = input_array[j - 7]
            j -= 7
        comparisons += 1
        input_array[j] = key
    return comparisons


# Input is any length array
# After function call array is 3-sorted
# Returns number of comparisons
def shell3(input_array):
    comparisons = 0
    for i in range(3, len(input_array)):
        key = input_array[i]
        j = i
        while j >= 3 and input_array[j - 3] > key:
            comparisons += 1
            input_array[j] = input_array[j - 3]
            j -= 3
        comparisons += 1
        input_array[j] = key
    return comparisons


# Input is any length array
# After function call array is sorted
# Returns number of comparisons
def shell_sort(input_array):
    comparisons = 0
    comparisons += shell7(input_array)
    comparisons += shell3(input_array)
    comparisons += insertion_sort(input_array)
    return comparisons


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
    #     print("Brute Force algorithm finds {} triples".format(brute_force_3sum(data_array)))
    #     print("Binary Search algorithm finds {} triples".format(binary_search_3sum(data_array)))
    #
    # except IndexError:
    #     print("No input data file")


if __name__ == '__main__':
    main()
