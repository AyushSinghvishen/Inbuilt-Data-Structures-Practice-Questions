def reverse_list(lst):
    """
    Reverse a list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with elements in reverse order.
    """
    return lst[::-1]

# Example usage
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)
print("Reversed list:", reverse_list(numbers))
