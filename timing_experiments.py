from Q1.Q1 import insertion_sort, shell7, shell3, shell_sort
from Q2.Q2 import kd_merge, kd_mergesort, kendalltau
from Q3.Q3 import q3_dataset_creation, bubblesort
from Q4.Q4 import merge, mergesort_insertion_cutoff, iterative_mergesort, recursive_mergesort
from Q5.Q5 import median_of_three, partition, quicksort, quicksort_insertion_cutoff
from glob import glob
import os
import timeit
import functools


def shellsort_comps():
    shell_sort_comps = []
    partial_insertion_sort_comps = []
    insertion_sort_comps = []
    data_sizes = [1024, 2048, 4096, 8192, 16384, 32768]
    for data_size in data_sizes:
        rel_path = "/Q1/data/data1.{}".format(data_size)
        cwd = os.getcwd()
        abs_file_path = cwd + rel_path
        input_file = open(abs_file_path)
        data_array = []
        for line in input_file.readlines():
            data_array.append(int(line))
        input_file.close()
        ss_comp, p_insert = shell_sort(data_array[:])
        shell_sort_comps.append(ss_comp)
        partial_insertion_sort_comps.append(p_insert)
        insertion_sort_comps.append(insertion_sort(data_array[:]))
    print(shell_sort_comps)
    print(partial_insertion_sort_comps)
    print(insertion_sort_comps)

    # PLOT STUFF


def kendalltau_timing():
    kd_merge_timings = []
    bubble_timings = []
    data_sizes = [1024, 2048, 4096, 8192, 16384, 32768]
    for data_size in data_sizes:
        rel_path = "/Q1/data/data1.{}".format(data_size)
        cwd = os.getcwd()
        abs_file_path = cwd + rel_path
        input_file = open(abs_file_path)
        data_array = []
        for line in input_file.readlines():
            data_array.append(int(line))
        input_file.close()

        kd_timer = timeit.Timer(functools.partial(kendalltau, data_array))
        kd_merge_timings.append(kd_timer.timeit(1))
        bb_time = timeit.Timer(functools.partial(bubblesort, data_array))
        bubble_timings.append(bb_time.timeit(1))
    print(kd_merge_timings)
    print(bubble_timings)

    # PLOT STUFF


def mergesort_vs_mergesort():
    rec_comps = []
    ite_comps = []

    data_sizes = [1024, 2048, 4096, 8192, 16384, 32768]
    for data_size in data_sizes:
        rel_path = "/Q1/data/data1.{}".format(data_size)
        cwd = os.getcwd()
        abs_file_path = cwd + rel_path
        input_file = open(abs_file_path)
        data_array = []
        for line in input_file.readlines():
            data_array.append(int(line))
        input_file.close()
        rec_comps.append(recursive_mergesort(data_array[:], 0, len(data_array)-1))
        ite_comps.append(iterative_mergesort(data_array[:]))
    print(rec_comps)
    print(ite_comps)

    # PLOT STUFF


def quicksort_vs_mergesort():
    ite_ms_timings = []
    ms_timings = []
    qs_timings = []

    data_sizes = [1024, 2048, 4096, 8192, 16384, 32768]
    for data_size in data_sizes:
        rel_path = "/Q1/data/data1.{}".format(data_size)
        cwd = os.getcwd()
        abs_file_path = cwd + rel_path
        input_file = open(abs_file_path)
        data_array = []
        for line in input_file.readlines():
            data_array.append(int(line))
        input_file.close()
        ms_timer = timeit.Timer(functools.partial(recursive_mergesort, data_array[:], 0, len(data_array)-1))
        ms_timings.append(ms_timer.timeit(5))
        ite_ms_timer = timeit.Timer(functools.partial(iterative_mergesort, data_array[:]))
        ite_ms_timings.append(ite_ms_timer.timeit(5))
        qs_timer = timeit.Timer(functools.partial(quicksort, data_array[:], 0, len(data_array)))
        qs_timings.append(qs_timer.timeit(5))
    print(ms_timings)
    print(ite_ms_timings)
    print(qs_timings)

    # PLOT STUFF


def quicksort_vs_mergesort_cutoffs():
    ms_timings = []
    qs_timings = []

    data_sizes = [1024, 2048, 4096, 8192, 16384, 32768]
    for data_size in data_sizes:
        rel_path = "/Q1/data/data1.{}".format(data_size)
        cwd = os.getcwd()
        abs_file_path = cwd + rel_path
        input_file = open(abs_file_path)
        data_array = []
        for line in input_file.readlines():
            data_array.append(int(line))
        input_file.close()
        ms_timer = timeit.Timer(functools.partial(mergesort_insertion_cutoff, data_array[:], 0, len(data_array) - 1))
        ms_timings.append(ms_timer.timeit(1))
        qs_timer = timeit.Timer(functools.partial(quicksort_insertion_cutoff, data_array[:], 0, len(data_array)))
        qs_timings.append(qs_timer.timeit(1))

    print(ms_timings)
    print(qs_timings)

    # PLOT STUFF


def quicksort_varying_cutoffs():
    qs_timings_list = []

    data_sizes = [1024, 2048, 4096, 8192, 16384, 32768]
    cutoffs = range(7, 700, 7)
    for cutoff in cutoffs:
        qs_timings = []
        for data_size in data_sizes:
            rel_path = "/Q1/data/data1.{}".format(data_size)
            cwd = os.getcwd()
            abs_file_path = cwd + rel_path
            input_file = open(abs_file_path)
            data_array = []
            for line in input_file.readlines():
                data_array.append(int(line))
            input_file.close()
            qs_timer = timeit.Timer(functools.partial(quicksort_insertion_cutoff, data_array[:], 0, len(data_array), cutoff))
            qs_timings.append(qs_timer.timeit(1))
        qs_timings_list.append(qs_timings)

    print(qs_timings_list)


def main():
    # shellsort_comps()
    # kendalltau_timing()
    # mergesort_vs_mergesort()
    # quicksort_vs_mergesort()
    # quicksort_vs_mergesort_cutoffs()
    quicksort_varying_cutoffs()

if __name__ == '__main__':
    main()