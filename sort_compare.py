import argparse
# other imports go here
import random
import time


def get_me_random_list(n):
    """Generate list of n elements in random order

    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value


def shell_sort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


def python_sort(a_list):
    """
    Use Python built-in sorted function
    :param a_list:
    :return: the sorted list
    """
    return sorted(a_list)


def get_algorithm_results_for_n_size(n):
    """Generate Algorithm Test Results for Lists of Size N

    :params: A number, N, corresponding to the size of the random lists to be generated
    :returns: (Tuple) Insertion Sort Average, Shell Sort Average, Python Sort Average
    """

    is_total = 0
    ss_total = 0
    ps_total = 0

    for i in range(100):
        new_list = get_me_random_list(n)

        is_st = time.time()
        is_sorted_list = insertion_sort(new_list)
        is_et = time.time()
        is_total_time = is_et - is_st
        is_total += is_total_time

        ss_st = time.time()
        ss_sorted_list = shell_sort(new_list)
        ss_et = time.time()
        ss_total_time = ss_et - ss_st
        ss_total += ss_total_time

        ps_st = time.time()
        ps_sorted_list = python_sort(new_list)
        ps_et = time.time()
        ps_total_time = ps_et - ps_st
        ps_total += ps_total_time

    is_average = is_total / 100
    ss_average = ss_total / 100
    ps_average = ps_total / 100

    return is_average, ss_average, ps_average


if __name__ == "__main__":
    """Main entry point"""

    print("Processing n size equals 500...")
    averages_500 = get_algorithm_results_for_n_size(500)

    print(f"Insertion Sort took {averages_500[0]:10.7f} seconds to run, on average. (500)")
    print(f"Shell Sort took {averages_500[1]:10.7f} seconds to run, on average. (500)")
    print(f"Python Sort took {averages_500[2]:10.7f} seconds to run, on average. (500)")

    print("Processing n size equals 1000...")
    averages_1000 = get_algorithm_results_for_n_size(1000)

    print(f"Insertion Sort took {averages_1000[0]:10.7f} seconds to run, on average. (1000)")
    print(f"Shell Sort took {averages_1000[1]:10.7f} seconds to run, on average. (1000)")
    print(f"Python Sort took {averages_1000[2]:10.7f} seconds to run, on average. (1000)")

    print("Processing n size equals 10000...")
    averages_5000 = get_algorithm_results_for_n_size(10000)

    print(f"Insertion Sort took {averages_10000[0]:10.7f} seconds to run, on average. (10000)")
    print(f"Shell Sort took {averages_10000[1]:10.7f} seconds to run, on average. (10000)")
    print(f"Python Sort took {averages_10000[2]:10.7f} seconds to run, on average. (10000)")