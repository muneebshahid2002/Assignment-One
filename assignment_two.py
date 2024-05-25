# problem 1
"""
Problem Statement:

Prompt the user to enter a float number.
Use the round() function to round the number to 2 decimal places.
Print the original number and the rounded number.
Use the len() function to find the length of a string entered by the user and print the result.
"""


# number = float(input("Enter any floating number: "))
# rounder_value = round(number,2)
# print("User entered value: ",number)
# print("Rounded value: ",rounder_value)
# convert_to_str = str(number)
# print("Length of user entered value: ", len(convert_to_str))


# problem 2
"""
Problem Statement:

Prompt the user to enter a sentence.
Convert the entire sentence to uppercase.
Convert the entire sentence to lowercase.
Capitalize the first word of the sentence.
Print each of these modified sentences.
"""
# sentence = input("Write any sentence: ")
# sentence_in_upper_case = sentence.upper()
# sentence_in_lower_case = sentence.lower()
# sentence_in_capitalize = sentence.capitalize()

# print("Lower Case: ",sentence_in_lower_case)
# print("Upper Case: ",sentence_in_upper_case)
# print("Capitalize Case: ",sentence_in_capitalize)


# problem 3
"""
Problem Statement:

Prompt the user to enter a sentence.
Ask user to replace the word
ask user to replace the word with

Print the modified sentence
"""
# sentence = input("Write any sentence: ")
# replace_word = input("Write a word to replace: ")
# replace_with = input("Write a word to replace with: ")
# modified_sentence = sentence.replace(replace_word, replace_with)
# print(modified_sentence)


# problem 4
"""
Write a program that:
Asks the user to enter their age.
Adds 10 to their age.

Prints a message saying "In 10 years, you will be X years old." where X is the new age.
"""
# age = int(input("Write your age: "))
# new_age = age+10
# print('In 10 years, you will be', new_age ,'years old. where', new_age ,'is the new age')


# problem 5
"""
Write a program that:

Asks the user to enter their full name.
Converts the full name to uppercase and prints it.
Asks the user for their favorite number.
Multiplies the number by 2, converts it to a string, and concatenates it to a message.

Prints the message "Your favorite number multiplied by 2 is X.", where X is the new number.
"""

# name = input("Write your full name: ")
# print("Upper Case Name: ",name.upper())
# favourt = int(input("Write your favorite number: "))
# multiplication = favourt * 2
# convert_to_string = str(multiplication)
# print('Your favorite number multiplied by 2 is',str(multiplication) ,'. where', str(multiplication) ,'is the new number')
# print(type(convert_to_string))


# problem 6
"""
Problem: Create a small program that asks the user for their first name and last name, 
converts them to uppercase, 
replaces spaces with hyphens
and calculates the length of their full name.
print 3 variables i.e
print("Your full name in uppercase is: " + full_name_upper)
print("Modified sentence: " + modified_sentence)
print("The length of your full name is: " + str(full_name_length))
NOTE: Concepts Covered: input(), string methods (upper, replace), len(), print()
"""
# first_name = input("Write your fisrt name: ")
# last_name = input("Write your last name: ")
# print("First Name in Upper Case: ",first_name.upper())
# print("Last Name in Upper Case: ",last_name.upper())
# full_name = first_name +" "+ last_name
# modified_sentence = full_name.replace(" ","-")
# print("Your full name in uppercase is: " + full_name.upper())
# print("Modified sentence: " + modified_sentence)
# print("The length of your full name is: " + str(len(full_name)))


# problem 7
"""
Problem: Ask the user to input two numbers. 
Calculate their average 
and print the average rounded to 2 decimal places.

NOTE: Concepts Covered: round(), input(), print(), type casting
"""
# Ask the user to input two numbers
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# # Calculate their average
# average = (num1 + num2) / 2

# # Print the average rounded to 2 decimal places
# print('The average of the two numbers is:',round(average,2))



# problem 8
"""
Problem: Ask the user to input a sentence. 
Replace all spaces with underscores 
and split the sentence into words.

NOTE: Concepts Covered: replace(), split(), input(), print()
"""
sentence = input("Enter a Sentence: ")
replaced = sentence.replace(" ","_")
print(replaced)
split_sentence = sentence.split()
print(split_sentence)

# last_name = input("Write your last name: ")




