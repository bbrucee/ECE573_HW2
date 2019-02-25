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


# https://www.geeksforgeeks.org/merge-sort/
def merge(input_array, left, middle, right):
    comps = 0
    N1 = middle - left + 1
    N2 = right - middle

    left_sub = []
    right_sub = []
    for i in range(0, N1):
        left_sub.append(input_array[left + i])
    for j in range(0, N2):
        right_sub.append(input_array[middle + 1 + j])

    i = j = 0
    k = left

    while i < N1 and j < N2:
        if left_sub[i] <= right_sub[j]:
            input_array[k] = left_sub[i]
            i += 1
            comps += 1
        else:
            input_array[k] = right_sub[j]
            j += 1
            comps += 1
        k += 1

    while i < N1:
        input_array[k] = left_sub[i]
        i += 1
        k += 1

    while j < N2:
        input_array[k] = right_sub[j]
        j += 1
        k += 1

    return comps


def recursive_mergesort(input_array, left, right):
    comps = 0
    if right > left:
        mid_point = (left + right) // 2
        comps += recursive_mergesort(input_array, left, mid_point)
        comps += recursive_mergesort(input_array, mid_point + 1, right)
        comps += merge(input_array, left, mid_point, right)
    return comps


# https://www.geeksforgeeks.org/iterative-merge-sort/
def iterative_mergesort(input_array):
    sz = 1
    comps = 0
    while sz < len(input_array) - 1:
        left = 0
        while left < len(input_array) - 1:
            mid = left + sz - 1

            if 2 * sz + left - 1 > len(input_array) - 1:
                right = len(input_array) - 1
            else:
                right = 2 * sz + left - 1

            comps += merge(input_array, left, mid, right)
            left = left + sz * 2
        sz = 2 * sz
    return comps


def mergesort_insertion_cutoff(input_array, left, right, cutoff=7):
    if right > left:
        if right - left < cutoff:
            insertion_sort(input_array)
            return
        mid_point = (left + right) // 2
        mergesort_insertion_cutoff(input_array, left, mid_point)
        mergesort_insertion_cutoff(input_array, mid_point+1, right)
        merge(input_array, left, mid_point, right)


def main():
    try:
        # https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
        rel_path = sys.argv[1]  # "/data/data1.1024"
        cwd = os.getcwd()
        abs_file_path = cwd + rel_path
        input_file = open(abs_file_path)
        data_array = []
        for line in input_file.readlines():
            data_array.append(int(line))
        input_file.close()
        print("Input data: {}".format(data_array))
        print("Iterative mergesort called on a copy of data_array, used {} comparisons".format(iterative_mergesort(data_array[:])))
        print("Recursive mergesort called on a copy of data_array, used {} comparisons".format(recursive_mergesort(data_array[:], 0, len(data_array)-1)))

    except IndexError:
        print("No input data file")


if __name__ == '__main__':
    main()
