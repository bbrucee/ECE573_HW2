import sys
import os


# input_array should be sorted
# I used https://web.stanford.edu/class/cs9/sample_probs/TwoSum.pdf page 4 to debug the if, elif, else
def linear_pairs(input_array, target):
    count = 0
    left = 0
    right = len(input_array) - 1

    while left < right:
        if (input_array[left] + input_array[right]) == target and \
                input_array[left] < input_array[right] < -target:
            count += 1
            # If we find a matched pair we have to move one of the pointers to not get stuck
            left += 1
        elif input_array[left] + input_array[right] < target:
            # If the sum is currently less than the target then we want to make it larger
            left += 1
        else:
            # Otherwise if the sum is greater than the target than we want to make it smaller
            right -= 1
    return count


def fastest_3sum(input_array):
    count = 0
    sorted_array = sorted(input_array)
    for i in range(0, len(sorted_array), 1):
        target_value = sorted_array[i]
        count += linear_pairs(sorted_array, -target_value)
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
        print("Fastest 3 Sum algorithm finds {} triples".format(fastest_3sum(data_array)))

    except IndexError:
        print("No input data file")


if __name__ == '__main__':
    main()
