# Determine whether the two lists have any item in common or not:

# Method1:
# But this method takes O(n2) time complexity as it has nested for loop.


def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


list1 = [1, 2, 5]
list2 = [3, 4, 5]
print(item_in_common(list1, list2))


# Method2:
# This method is more efficient than the above one, as it has only O(n) time complexity


def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True
    return False


list1 = [1, 2, 5]
list2 = [3, 4, 5]
print(item_in_common(list1, list2))
