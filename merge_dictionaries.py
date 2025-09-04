def merge_dictionaries(dict1, dict2):
    """
    Merge two dictionaries, summing values for common keys.
    
    Parameters:
    dict1 (dict): First dictionary
    dict2 (dict): Second dictionary
    
    Returns:
    dict: Merged dictionary with summed values for common keys
    """
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

# Example usage
dict1 = {'a': 2, 'b': 3, 'c': 5}
dict2 = {'b': 4, 'c': 6, 'd': 1}
print("Merged dictionary:", merge_dictionaries(dict1, dict2))
