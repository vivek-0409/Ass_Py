print("*****Sum of first n positive integers*****")


#1.Sum of first n positive integers
n = int(input("Enter a number: "))
total = sum(range(1, n+1))
print("Sum:", total)

print("*****Count occurrences of a substring in a string*****")
#2. Count occurrences of a substring in a string
string = "hello hello world"
print(string.count("hello"))    # Output: 2

print("*****Count each word in a sentence*****")

#3. Count each word in a sentence
sentence = "hello world hello"
words = sentence.split()
count = {word: words.count(word) for word in words}
print(count)

print("*****Combine two strings and swap first 2 characters*****")

#4. Combine two strings and swap first 2 characters
s1 = "hello"
s2 = "world"
s1_new = s2[:2] + s1[2:]
s2_new = s1[:2] + s2[2:]
print(s1_new + " " + s2_new)

print("*******Add 'ing' or 'ly' (But ---  String is less than 3)******")

# 5. Add 'ing' or 'ly' to a string
s = input("Enter a string: ")

if len(s)<3:
    print(s)
elif s.endswith("ing"):
    print(s + "ly")
else:
    print(s + "ing")

print("*******Replace 'not...poor' with 'good'******")
#6. Replace 'not...poor' with 'good'
def replace_not_poor(text):
    not_index = text.find('not')
    poor_index = text.find('poor')

    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        result = text[:not_index] + 'good' + text[poor_index + 4:]
        return result
    else:
        return text

sentence = input("Enter a sentence: ")
print("Updated sentence:", replace_not_poor(sentence))    


# Ex :-   
# (input)  :-  Enter a sentence: This movie is not that poor!
# (Output) :-  Updated sentence: This movie is good!

print("******Store user details in tuple using class*******")


#7.  Store user details in tuple using class
import math

# Take input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate GCD
gcd = math.gcd(num1, num2)

# Print result
print(f"The GCD of {num1} and {num2} is: {gcd}")

# Ex :-  Enter first number: 20
#        Enter second number: 28
#        The GCD of 20 and 28 is: 4


# =>  without ( math )

# Function to find GCD manually
def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Output
print(f"The GCD of {a} and {b} is: {find_gcd(a, b)}")


print("*****check whether a list contains a sublist.******")


# 8. check whether a list contains a sublist.

def contains_sublist(main_list, sub_list):
    sub_len = len(sub_list)
    for i in range(len(main_list) - sub_len + 1):
        if main_list[i:i+sub_len] == sub_list:
            return True
    return False


main = [1, 2, 3, 4, 5, 6]
sub = [3, 4, 5]


if contains_sublist(main, sub):
    print("Sublist found in the main list.")
else:
    print("Sublist not found.")

print("******second smallest number in a list.******")

#9. second smallest number in a list.
 
n=[11,99,55,33,00]

n.sort()

print(n[1])           # Output :- 11


print("********get unique values from a list. ******")

# 10. get unique values from a list. 
nums = list(map(int, input("Enter list elements: ").split()))

# Remove duplicates but keep original order
unique = []
for num in nums:
    if num not in unique:
        unique.append(num)

print("Unique values (ordered):", unique)


# EX:-        Enter list elements:  1 2 2 3 4 4 5                                         
#             Unique values (ordered): [1, 2, 3, 4, 5]


print("******unzip a list of tuples into individual lists.*******")

# 11. unzip a list of tuples into individual lists.

# List of tuples
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

# Unzipping using zip and *
list1, list2 = zip(*pairs)

# Convert to list (optional)
list1 = list(list1)
list2 = list(list2)

# Output
print("First list:", list1)
print("Second list:", list2)



# Ex :-   First list: [1, 2, 3]
#         Second list: ['a', 'b', 'c']


print("*****convert a list of tuples into a dictionary ******")

# 12. convert a list of tuples into a dictionary 

# List of tuples
tuple_list = [('a', 1), ('b', 2), ('c', 3)]

# Convert to dictionary using dict()
dictionary = dict(tuple_list)

# Output the result
print("Converted dictionary:", dictionary)       # Output :- Converted dictionary: {'a': 1, 'b': 2, 'c': 3}


print("******sort a dictionary (ascending /descending) by value.*****")

# 13.sort a dictionary (ascending /descending) by value. 

# Original dictionary
my_dict = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 3}

# Sort in ascending order by value
asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sort in descending order by value
desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

# Output
print("Ascending order :", asc_sorted)
print("Descending order :", desc_sorted)    

# Output :-   Ascending order : {'banana': 2, 'date': 3, 'apple': 5, 'cherry': 8}
            # Descending order : {'cherry': 8, 'apple': 5, 'date': 3, 'banana': 2}

print("*****find the highest 3 values in a dictionary.*****")

# 14. find the highest 3 values in a dictionary.

# Sample dictionary
my_dict = {'a': 30, 'b': 10, 'c': 60, 'd': 50, 'e': 90}

# Step 1: Get all values and sort in descending order
top_values = sorted(my_dict.values(), reverse=True)[:3]

# Output
print("Top 3 highest values are:", top_values)          # Output :- Top 3 highest values are: [90, 60, 50]



print("*****Fibonacci series*******")

# 15. Fibonacci series

n=int(input("Enter The Number In Which You Want Range{N=}:"))
n1=0
n2=1
print(n1 , end=" ")
print(n2 , end=" ")
for i in range(2,n):
    n3=n1+n2
    print(n3 , end=" ")
    n1=n2
    n2=n3         

# Enter The Number In Which You Want Range:8
# Ans :- 0 1 1 2 3 5 8 13 

print("*****Count Frequencies Using Dictionary******")

# 16. Count Frequencies Using Dictionary

numbers = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2,2]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1   
    else:
        frequency[num] = 1    

for key in sorted(frequency):  
    print(f"{key} : {frequency[key]}", end=" , ")  

# Output :-  1 : 5 , 2 : 4 , 3 : 3 , 4 : 3 , 5 : 2 ,     

print("******using function to find  the sum of odd series and even series *******")

# 17. using function to find  the sum of odd series and even series 

import math  # factorial function ke liye

# Function to calculate odd series sum
def odd_series(n):
    sum_odd = 0
    num = 1  # odd numbers start from 1
    for i in range(n):
        term = (num ** 2) / math.factorial(num)
        sum_odd += term
        num += 2  # next odd number
    return sum_odd

# Function to calculate even series sum
def even_series(n):
    sum_even = 0
    num = 2  # even numbers start from 2
    for i in range(n):
        term = (num ** 2) / math.factorial(num)
        sum_even += term
        num += 2  # next even number
    return sum_even

try:
    n = int(input("Enter number of terms (n): "))
    if n <= 0:
        print("Please enter a positive number.")
    else:
        print("Sum of Odd Series:", round(odd_series(n), 4))
        print("Sum of Even Series:", round(even_series(n), 4))
except ValueError:
    print("Invalid input! Please enter an integer.")


# Output :-   Enter number of terms (n): 5
#             Sum of Odd Series: 2.7183
#             Sum of Even Series: 2.7183

print("******Find Factorial of Number Using Recursion******")

# 18. Find Factorial of Number Using Recursion


def factorial(n):
    if n == 0 or n == 1:
        return 1  # Base case: factorial of 0 or 1 is 1
    else:
        return n * factorial(n - 1)  # Recursive call


try:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print(f"Factorial of {num} is: {result}")
except ValueError:
    print("Please enter a valid integer.")

# Output :-   Enter a number: 5
#             Factorial of 5 is: 120

print("******# 19. function that takes a list and returns a new list with unique elements of the first list*****")

# 19. function that takes a list and returns a new list with unique elements of the first list

def get_unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage
original_list = [1, 2, 2, 3, 4, 4, 5, 1]
print("Original List:", original_list)
print("Unique List:", get_unique_elements(original_list))

# Output :- Original List: [1, 2, 2, 3, 4, 4, 5, 1]
#           Unique List: [1, 2, 3, 4, 5]  

print("*****Mini project :  Problem Statement : Password Generator******")

# 20. Mini project :  Problem Statement : Password Generator

import random
import string

# User class to store user details
class User:
    def __init__(self, user_id, name, password):
        self.details = (user_id, name, password)

    def display(self):
        print("\nUser Details:")
        print("User ID   :", self.details[0])
        print("Name      :", self.details[1])
        print("Password  :", self.details[2])

# Function to generate strong password
def generate_password(user_input):
    try:
        # Break input into words
        words = user_input.split()
        if len(words) < 2:
            raise ValueError("Please enter at least two words for better password generation.")

        # Randomly select one or two words
        chosen = random.sample(words, 2)
        base = ''.join(chosen)

        # Add random digits, special characters, uppercase letters
        symbols = random.choices("!@#$%^&*()_+", k=2)
        digits = random.choices(string.digits, k=2)
        upper_letters = random.choices(string.ascii_uppercase, k=2)

        # Combine all parts and shuffle
        raw_password = list(base + ''.join(symbols + digits + upper_letters))
        random.shuffle(raw_password)
        password = ''.join(raw_password)

        # Ensure password length > 8
        if len(password) < 8:
            # Add extra characters if needed
            password += ''.join(random.choices(string.ascii_letters + string.digits, k=8 - len(password)))

        return password
    except Exception as e:
        print("Error generating password:", e)
        return None

# Main program
try:
    user_id = input("Enter User ID: ")
    name = input("Enter your name: ")
    input_text = input("Enter a few words related to yourself (e.g. hobbies, favorites, etc.): ")

    password = generate_password(input_text)

    if password:
        user = User(user_id, name, password)
        user.display()
    else:
        print("Failed to generate password.")

except Exception as err:
    print("Something went wrong:", err)


# Output :- Enter User ID: u001
            # Enter your name: Vivek
            # Enter a few words related to yourself (e.g. hobbies, favorites, etc.): music python cricket

            # User Details:
            # User ID   : u001
            # Name      : Vivek
            # Password  : !3Pycr*)6



print("**********************Finish*************************")




