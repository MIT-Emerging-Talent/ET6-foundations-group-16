from math import sqrt

# Write a function that takes a sentence and returns the longest word in that sentence
s = "I am learning Python programming language"

# Split the sentence into words
words = s.split()

# Initialize an empty string to store the longest word
res = ""

# Iterate through each word
for word in words:
  
    # Update 'res' if the current word is longer than 'res'
    if len(word) > len(res):
        res = word

print(res)

# Longest word

# Reading sentence from user

sentence = input("Enter sentence: ")

# Finding longest word
longest = max(sentence.split(), key=len)

# Displaying longest word
print("Longest word is: ", longest)
print("And its length is: ", len(longest))

# Function to check the Vowel 
def isVowel(ch): 
    return ch.upper() in ['A', 'E', 'I', 'O', 'U'] 
  
# to count total number of 
# vowel from 0 to n 
def countVovels(str, n): 
    if (n == 1): 
        return isVowel(str[n - 1]); 
  
    return (countVovels(str, n - 1) +
                isVowel(str[n - 1])); 
  
# Driver Code 
  
# string object 
str = "abc de"; 
  
# Total numbers of Vowel 
print(countVovels(str, len(str)))

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

# Different Sizes using Sorting

def medianOf2(a, b):
    # Merge both the arrays
    c = a + b

    # Sort the concatenated array
    c.sort()

    len_c = len(c)

    # If length of array is even
    if len_c % 2 == 0:
        return (c[len_c // 2] + c[len_c // 2 - 1]) / 2.0

    # If length of array is odd
    else:
        return c[len_c // 2]

if __name__ == "__main__":
    a = [-5, 3, 6, 12, 15,44]
    b = [-12, -10, -6, -3, 21, 10]

    print(medianOf2(a, b))

#write a code that return a list of the elements that are common to both lists, without duplicates.
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

# Find common elements using nested loops
common = []
for x in a:
    if x in b:
        common.append(x)

print(common)

#Given a positive integer, determine if it is a prime number
#  (a number greater than 1 that has no divisors other than 1 
# and itself).
# prime function to check given number prime or not
def Prime(number, itr):  
    # base condition
    if itr == 1 or itr == 2:  
        return True
      # if given number divided by itr or not
    if number % itr == 0:  
        return False
      # Recursive function Call
    if Prime(number, itr - 1) == False:  
        return False

    return True

num = 14

itr = int(sqrt(num) + 1)

print(Prime(num, itr))

# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 6

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

   # Python program to find the factorial of a number provided by the user
# using recursion

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1 or x == 0:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


# change the value for a different result
num = 8

# to take input from the user
# num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)

# Python program to illustrate the intersection
# of two lists in most simple way
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

# Driver Code
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(lst1, lst2))