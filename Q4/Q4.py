import sys
import os


def farthest_pair(a, print_output=False):
    min_value = float('-inf') # min(a)
    max_value = float('inf') # max(a)
    for index in range(0, len(a), 1):
        if a[index] > min_value:
            min_value = a[index]
        if a[index] < max_value:
            max_value = a[index]
    if print_output:
        print("Farthest pair is {} and {} with a distance of {}".format(min_value, max_value, abs(max_value-min_value)))


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
        farthest_pair(data_array, True)

    except IndexError:
        print("No input data file")


if __name__ == '__main__':
    main()
