import sys
import os
import csv


# Dataset is already sorted so we can use a modified bubble sort to exit after a single pass through
# The idea here is that bubble sort is completed when it makes a pass with no swaps
# https://www.quora.com/What-is-modified-bubble-sorting

def q3_dataset_creation(write_to_csv=False):

    dataset = 1024 * [1] + 2048 * [11] + 4096 * [111] + 1024 * [1111]
    # https://stackoverflow.com/questions/2084069/create-a-csv-file-with-values-from-a-python-list
    if write_to_csv:
        with open('Q3_dataset.csv', 'w') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(dataset)
    return dataset


def bubblesort(input_array):
    total_swaps = 0
    for i in range(len(input_array)):
        swaps = 0
        for j in range(len(input_array)-i-1):
            if input_array[j] > input_array[j+1]:
                temp = input_array[j]
                input_array[j] = input_array[j+1]
                input_array[j+1] = temp
                swaps = swaps + 1
                total_swaps = total_swaps + 1
        if swaps == 0:
            break
    return total_swaps


def main():
    pass
#     try:
#         # https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
#         rel_path = sys.argv[1]
#         cwd = os.getcwd()
#         abs_file_path = cwd + rel_path
#         print("Input data file: {}".format(abs_file_path))
#         file = open(abs_file_path)
#         data_array = []
#         for line in file.readlines():
#             data_array.append(tuple(map(int, line.split())))
#         print("Input data: {}".format(data_array))
#         file.close()
#
#         A = UFQuickfind(8192)
#         B = UFQuickunion(8192)
#         C = UFQuickunionbalanced(8192)
#
#         for (left, right) in data_array:
#             if not A.find(left, right):
#                 A.union(left, right)
#             if not B.find(left, right):
#                 B.union(left, right)
#             if not C.find(left, right):
#                 C.union(left, right)
#
#         print("Not sure what the output should be...")
#
#     except IndexError:
#         print("No input data file")


if __name__ == '__main__':
    main()