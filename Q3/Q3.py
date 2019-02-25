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
    total_comps, total_swaps = 0, 0
    for i in range(len(input_array)):
        swaps = 0
        for j in range(len(input_array)-i-1):
            if input_array[j] > input_array[j+1]:
                temp = input_array[j]
                input_array[j] = input_array[j+1]
                input_array[j+1] = temp
                swaps = swaps + 1
                total_swaps += 1
            total_comps = total_comps + 1
        if swaps == 0:
            break
    return total_comps, total_swaps


def main():
    num_comps, num_swaps = bubblesort(q3_dataset_creation())
    print("Bubblesort makes {} comparisons, {} swaps to sort the specified dataset".format(num_comps, num_swaps))


if __name__ == '__main__':
    main()