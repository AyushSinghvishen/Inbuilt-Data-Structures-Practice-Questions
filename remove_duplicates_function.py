# remove_duplicates_function.py

def remove_duplicates(lst):
    """
    Remove duplicates from a list while preserving order.

    Parameters:
    lst (list): The input list with possible duplicates.

    Returns:
    list: A new list with duplicates removed.
    """
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
print("Original list:", numbers)
print("Unique list:", remove_duplicates(numbers))
