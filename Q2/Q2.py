import sys
import os


def kd_merge(input_array, left, middle, right):
    swaps = 0

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
        else:
            input_array[k] = right_sub[j]
            swaps = swaps + middle - (left + i) + 1
            j += 1
        k += 1

    while i < N1:
        input_array[k] = left_sub[i]
        i += 1
        k += 1

    while j < N2:
        input_array[k] = right_sub[j]
        j += 1
        k += 1

    return swaps


def kd_mergesort(input_array, left, right):
    swaps = 0
    if right > left:
        mid_point = (left + right) // 2
        swaps = swaps + kd_mergesort(input_array, left, mid_point)
        swaps = swaps + kd_mergesort(input_array, mid_point + 1, right)
        swaps = swaps + kd_merge(input_array, left, mid_point, right)
    return swaps


def kendalltau(input_array):
    temp_array = input_array[:]
    return kd_mergesort(temp_array, 0, len(temp_array) - 1)


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
    #         data_array.append(tuple(map(int, line.split())))
    #     print("Input data: {}".format(data_array))
    #     file.close()
    #
    #     A = UFQuickfind(8192)
    #     B = UFQuickunion(8192)
    #     C = UFQuickunionbalanced(8192)
    #
    #     for (left, right) in data_array:
    #         if not A.find(left, right):
    #             A.union(left, right)
    #         if not B.find(left, right):
    #             B.union(left, right)
    #         if not C.find(left, right):
    #             C.union(left, right)
    #
    #     print("Not sure what the output should be...")
    #
    # except IndexError:
    #     print("No input data file")


if __name__ == '__main__':
    main()