import unittest
# Function that count the vowel in sentence 
def count_vowels_recursively(string): 
 
    if not string: 
 
        return 0 
    else: 
        if string[0].lower() in 'aeiou': 
            return 1 + count_vowels_recursively(string[1:]) 
        else: 
            return count_vowels_recursively(string[1:]) 
 
input_string = "Palestinian culture is beautiful." 
a = count_vowels_recursively(input_string) 
print(f"Number of vowels in '{input_string}' is: {a}") 
 
# Function that count the vowel in sentence 
def count_vowels_recursively(string): 
 
    if not string: 
 
        return 0 
    else: 
        if string[0].lower() in 'aeiou': 
            return 1 + count_vowels_recursively(string[1:]) 
        else: 
            return count_vowels_recursively(string[1:])
         
input_string = "Palestinian culture is beautiful." 
a = count_vowels_recursively(input_string) 
print(f"Number of vowels in '{input_string}' is: {a}") 


def count_vowels_recursively(string): 
    if not string: 
        return 0 
    else: 
        if string[0].lower() in 'aeiou': 
            return 1 + count_vowels_recursively(string[1:]) 
        else: 
            return count_vowels_recursively(string[1:])
#Here is the test 

class TestCountVowelsRecursively(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_vowels_recursively(""), 0)

    def test_no_vowels(self):
        self.assertEqual(count_vowels_recursively("bcdfghjklmnpqrstvwxyz"), 0)

    def test_only_vowels(self):
        self.assertEqual(count_vowels_recursively("aeiouAEIOU"), 10)

    def test_mixed_string(self):
        self.assertEqual(count_vowels_recursively("hello world"), 3)

    def test_complex_sentence(self):
        self.assertEqual(count_vowels_recursively("The quick brown fox jumps over the lazy dog"), 11)

    def test_special_characters(self):
        self.assertEqual(count_vowels_recursively("!@#$%^&*()_+ 1234567890-="), 0)

    def test_single_vowel(self):
        self.assertEqual(count_vowels_recursively("a"), 1)

    def test_single_non_vowel(self):
        self.assertEqual(count_vowels_recursively("b"), 0)

if __name__ == '__main__':
    unittest.main()
