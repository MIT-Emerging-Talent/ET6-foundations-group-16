
def common_elements(list1, list2):
    # Convert both lists to sets to remove duplicates and find intersection
    set1 = set(list1)
    set2 = set(list2)
    # Find the common elements
    common = set1.intersection(set2)
    # Convert the result back to a list
    return list(common)

# Example usage
list1 = [1, 2, 3, 4, 5, 6,7]
list2 = [4, 5, 6, 7, 8, 9]
result = common_elements(list1, list2)
print(result)  # Output: [4, 5, 6]

