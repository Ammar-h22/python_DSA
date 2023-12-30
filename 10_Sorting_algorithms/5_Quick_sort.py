def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


# pivot function is a helper function in the quick_sort
def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort(my_list, left, pivot_index - 1)
        quick_sort(my_list, pivot_index + 1, right)
    return my_list


print(quick_sort([4, 1, 6, 7, 3, 2, 5], 0, 6))


# Quick sort:
# Time complexity of Best and Average case is O(n log n) when the data is not sorted.
# The worst case is O(n2) when the data is already sorted.
