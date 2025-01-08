# Write Python 3 code in this online


def common_elements(list1, list2):
    # Convert both lists to sets to remove duplicates and find intersection
    set1 = set(list1)
    set2 = set(list2)
    # Find the common elements
    common = set1.intersection(set2)
    # Convert the result back to a list
    return list(common)


# Example usage
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
result = common_elements(list1, list2)
print(result)  # Output: [4, 5, 6]

# Example usage
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
result = common_elements(list1, list2)  # type: ignore
print(result)  # Output: [4, 5, 6]


def test_common_elements():
    # Test case 1: Common elements exist
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    assert sorted(common_elements(list1, list2)) == [4, 5], "Test case 1 failed"  # type: ignore

    # Test case 2: No common elements
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    assert common_elements(list1, list2) == [], "Test case 2 failed"  # type: ignore

    # Test case 3: Identical lists
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 5]
    assert sorted(common_elements(list1, list2)) == [
        1,
        2,
        3,
        4,
        5,
    ], "Test case 3 failed"  # type: ignore

    # Test case 4: One list is empty
    list1 = []
    list2 = [1, 2, 3]
    assert common_elements(list1, list2) == [], "Test case 4 failed"  # type: ignore

    # Test case 5: Both lists are empty
    list1 = []
    list2 = []
    assert common_elements(list1, list2) == [], "Test case 5 failed"  # type: ignore

    # Test case 6: Lists with duplicate elements
    list1 = [1, 2, 2, 3, 4]
    list2 = [3, 3, 4, 5, 6]
    assert sorted(common_elements(list1, list2)) == [3, 4], "Test case 6 failed"  # type: ignore

    print("All test cases passed!")


# Run the tests
test_common_elements()
