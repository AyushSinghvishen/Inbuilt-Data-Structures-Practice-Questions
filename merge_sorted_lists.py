def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists into a single sorted list.

    Parameters:
    list1 (list): First sorted list
    list2 (list): Second sorted list

    Returns:
    list: Merged sorted list
    """
    return sorted(list1 + list2)

# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print("Merged sorted list:", merge_sorted_lists(list1, list2))
