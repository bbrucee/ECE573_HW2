import sys
import os


def brute_force_3sum(input_array):
    count = 0
    for i in range(0, len(input_array), 1):
        for j in range(i + 1, len(input_array), 1):
            for k in range(j + 1, len(input_array), 1):
                if input_array[i] + input_array[j] + input_array[k] == 0:
                    count += 1
    return count


# Input array must be sorted
# Modified from http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
def binary_search(input_array, target):
    low = 0
    high = len(input_array)
    while low < high:
        mid_point = (low + high) // 2
        if input_array[mid_point] < target:
            low = mid_point + 1
        elif input_array[mid_point] > target:
            high = mid_point
        else:
            return input_array[mid_point]
    return None


def binary_search_3sum(input_array):
    count = 0
    sorted_array = sorted(input_array)
    for i in range(0, len(sorted_array), 1):
        for j in range(i + 1, len(sorted_array), 1):
            target_value = sorted_array[i] + sorted_array[j]
            if binary_search(sorted_array, -target_value) and \
                    sorted_array[i] < sorted_array[j] < -target_value:
                count += 1
    return count


def main():
    try:
        # https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
        rel_path = sys.argv[1]
        cwd = os.getcwd()
        abs_file_path = cwd + rel_path
        print("Input data file: {}".format(abs_file_path))
        file = open(abs_file_path)
        data_array = []
        for line in file.readlines():
            data_array.append(int(line))
        print("Input data: {}".format(data_array))
        file.close()
        print("Brute Force algorithm finds {} triples".format(brute_force_3sum(data_array)))
        print("Binary Search algorithm finds {} triples".format(binary_search_3sum(data_array)))

    except IndexError:
        print("No input data file")


if __name__ == '__main__':
    main()
