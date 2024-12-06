# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()


# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    letters = input("Enter a letter: ").lower()
    print(f"The user entered the letter {letters}")

    for letter in letters:
        if letter == 'a' and 'e' and 'i' and 'o' and 'u':
            print(f"The letter '{letters} is a vowel.'")
        elif type(letter) == int or float:
            print(f"{letter} is a number. Please enter a letter.")
            # prints out consonants & words...need to fix
            # How to print floating num 1 time/no repeats?  Circle back....  
        elif  len(letters) > len(letter):
            print(f"{letters} is invalid. Please enter a letter.")
        else:
            print(f"The letter '{letters}' is a consonant.")

# Call the function
check_letter()
