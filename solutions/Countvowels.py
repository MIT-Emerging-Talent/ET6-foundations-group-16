def count_vowels_recursively(string):
    if not string:
        return 0
    else:
        if string[0].lower() in "aeiou":
            return 1 + count_vowels_recursively(string[1:])
        else:
            return count_vowels_recursively(string[1:])


input_string = "Palestinian culture is beautiful."
a = count_vowels_recursively(input_string)
print(f"Number of vowels in '{input_string}' is: {a}")