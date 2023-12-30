# merge function is a helper function in merge_sort.
def merge(list1, list2):
    combined_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined_list.append(list1[i])
            i += 1
        else:
            combined_list.append(list2[j])
            j += 1
    while i < len(list1):
        combined_list.append(list1[i])
        i += 1
    while j < len(list2):
        combined_list.append(list2[j])
        j += 1
    return combined_list


def merge_sort(my_list):
    if len(my_list) == 1:  # Base case
        return my_list
    mid_index = len(my_list) // 2
    left_half = merge_sort(my_list[:mid_index])  # Recursion
    right_half = merge_sort(my_list[mid_index:])  # Recursion

    return merge(left_half, right_half)


original_list = [3, 1, 6, 5, 4, 2, 7]
sorted_list = merge_sort(original_list)

print("Original list :", original_list)
print("Sorted list:", sorted_list)


# Space complexity of merge sort is O(n).
# Time complexity of merge sort is O(n log n).
