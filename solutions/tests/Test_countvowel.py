# Test cases for the function count_vowels_recursively 
def test_count_vowels_recursively(): 
    # Test case 1: Empty string 
    assert count_vowels_recursivelycount_vowels_recursively("") == 0, "Test case 1 failed"  # type: ignore
    
    # Test case 2: String with no vowels 
    assert count_vowels_recursivelycount_vowels_recursively("bcdfghjklmnpqrstvwxyz") == 0, "Test case 2 failed"  # type: ignore
     
    # Test case 3: String with only vowels 
    assert count_vowels_recursivelycount_vowels_recursively("aeiouAEIOU") == 10, "Test case 3 failed"  # type: ignore
     
    # Test case 4: Mixed string 
    assert count_vowels_recursivelycount_vowels_recursively("hello world,") == 3, "Test case 4 failed"  # type: ignore
     
    # Test case 5: Complex sentence 
    assert count_vowels_recursivelycount_vowels_recursively("The quick brown fox jumps over the lazy dog") == 11, "Test case 5 failed"  # type: ignore
     
    # Test case 6: String with special characters and spaces 
    assert count_vowels_recursivelycount_vowels_recursively("!@#$%^&*()_+ 1234567890-=") == 0, "Test case 6 failed"  # type: ignore
     
    # Test case 7: Single character (vowel) 
    assert count_vowels_recursivelycount_vowels_recursively("a") == 1, "Test case 7 failed"  # type: ignore
     
    # Test case 8: Single character (non-vowel) 
    assert count_vowels_recursivelycount_vowels_recursively("b") == 0, "Test case 8 failed"  # type: ignore
 
    print("All test cases passed!") 
 
# Run the tests 
test_count_vowels_recursively()
