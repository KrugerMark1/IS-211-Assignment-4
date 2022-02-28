import argparse
# other imports go here
import time
import random


def current_time():
    """Get the current time in seconds

    :returns: The current time in seconds
    """
    return time.time()


def get_me_random_list(n):
    """Generate list of n elements in random order

    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    pos = 0
    found = False

    st = current_time()

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    et = current_time()
    total_time = et - st

    return found, total_time


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False

    st = current_time()

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    et = current_time()
    total_time = et - st

    return found, total_time


def binary_search_iterative(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    st = current_time()

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    et = current_time()
    total_time = et - st

    return found, total_time


def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)


def time_binary_search_recursive(a_list, item):
    """Run the function for binary search recursive and time it

    :returns: (Tuple) Binary Search Result, Time of Execution in Seconds
    """
    st = current_time()
    bs_return = binary_search_recursive(a_list, item)
    et = current_time()
    total_time = et - st

    return bs_return, total_time


def get_algorithm_results_for_n_size(n):
    """Generate Algorithm Test Results for Lists of Size N

    :params: A number, N, corresponding to the size of the random lists to be generated
    :returns: (Tuple) Sequential Sort Average, Ordered Sequential Sort Average, Binary Search (Iterative) Average,
    Binary Search (Recursive) Average
    """

    """ Counters to keep track of the total execution time to calculate the average at the end """
    ss_total = 0
    oss_total = 0
    bsi_total = 0
    bsr_total = 0

    """ Calculate 100 execution times per algorithm, adding to the counters """
    for i in range(0, 100):
        new_list = get_me_random_list(n)
        """ Run the first Algorithm, worst case, with a list """
        ss_total += sequential_search(new_list, -1)[1]

        """ Sort the list to pass to the appropriate algorithms """
        new_list.sort()

        """ Run the rest of Algorithms, worst case, with the sorted list """
        oss_total += ordered_sequential_search(new_list, -1)[1]
        bsi_total += binary_search_iterative(new_list, -1)[1]
        bsr_total += time_binary_search_recursive(new_list, -1)[1]

    """ Calculate the averages of each execution time using the totals """
    ss_average = ss_total / 100
    oss_average = oss_total / 100
    bsi_average = bsi_total / 100
    bsr_average = bsr_total / 100

    return ss_average, oss_average, bsi_average, bsr_average


if __name__ == "__main__":
    """Main entry point"""

    averages_500 = get_algorithm_results_for_n_size(500)
    averages_1000 = get_algorithm_results_for_n_size(1000)
    averages_10000 = get_algorithm_results_for_n_size(10000)

    """ Display our average results from 100 executions of each algorithm """
    print(f"Sequential Search took {averages_500[0]:10.7f} seconds to run, on average. (500)")
    print(f"Ordered Sequential Search took {averages_500[1]:10.7f} seconds to run, on average. (500)")
    print(f"Binary Search (Iterative) took {averages_500[2]:10.7f} seconds to run, on average. (500)")
    print(f"Binary Search (Recursive) took {averages_500[3]:10.7f} seconds to run, on average. (500)")

    print(f"Sequential Search took {averages_1000[0]:10.7f} seconds to run, on average. (1000)")
    print(f"Ordered Sequential Search took {averages_1000[1]:10.7f} seconds to run, on average. (1000)")
    print(f"Binary Search (Iterative) took {averages_1000[2]:10.7f} seconds to run, on average. (1000)")
    print(f"Binary Search (Recursive) took {averages_1000[3]:10.7f} seconds to run, on average. (1000)")

    print(f"Sequential Search took {averages_10000[0]:10.7f} seconds to run, on average. (10000)")
    print(f"Ordered Sequential Search took {averages_10000[1]:10.7f} seconds to run, on average. (10000)")
    print(f"Binary Search (Iterative) took {averages_10000[2]:10.7f} seconds to run, on average. (10000)")
    print(f"Binary Search (Recursive) took {averages_10000[3]:10.7f} seconds to run, on average. (10000)")
