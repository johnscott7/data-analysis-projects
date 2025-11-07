my_string = "LaunchCode"

# a) Use string methods to remove the first three characters from the string and add them to the end.
new_string = my_string[3:] + my_string[:3]
print(new_string)

# Use a template literal to print the original and modified string in a descriptive phrase.
print(f"The first word is {my_string} and the re-formmated word is {new_string}")

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
number = int(input("Input the number of letters that you would like to be relocated from the original word: "))
new_word = my_string[number:] + my_string[:number]
print(f"The user modified word is now {new_word}")

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
number = int(input("Input the number of letters that you would like to be relocated from the original word: "))
if number > len(my_string):
    print(f"That number is too big. '{my_string}' only contains {len(my_string)} letters. 3 letters will be relocated.")
    number = 3
new_word_2 = my_string[number:] + my_string[:number]
print(f"The user modified word is now {new_word_2}")
