# We want to COMPLETELY reverse a list by flipping the order of the entries AND flipping the order of characters in each element.

# a) Define a 'reverse_characters' function. Give it one parameter, which will be the string to reverse.
#def reverse_characters(word):
  
# b) Within the function, use the 'list' function to split a string into a list of individual characters
#def reverse_characters(word):
#   word_list = list(word)

# c) 'reverse' your new list.
#def reverse_characters(word):
#    word_list = list(word)
#    rev_word_list = word_list.reverse()

# d) Use 'join' to create the reversed string and return that string from the function.
#def reverse_characters(word):
#    word_list = list(word)
#    rev_word_list = word_list.reverse()
#    return ''.join(rev_word_list)

# e) Create a variable of type string to test your new function. 
#word = 'bumblebee'

# f) Use 'print(reverse_characters(my_variable_name))'; to call the function and verify that it correctly reverses the characters in the string.

#def reverse_characters(word):
#    word_list = list(word)
#    word_list.reverse()
#    return ''.join(word_list)
# g) Use method chaining to reduce the lines of code within the function.

def reverse_characters(word):
    return ''.join(reversed(list(word)))

print(reverse_characters('bumblebee'))

# 2) The 'split' method does not work on numbers, but we want the function to return a number with all the digits reversed (e.g. 1234 converts to 4321 and NOT the string "4321")

# a) Add an if statement to your reverse_characters function to check the typeof the parameter.
#if type(word) == str:

#else:

# b - d) If type is ‘string’, return the reversed string as before. If type is ‘number’, convert the parameter to a string, reverse the characters, then convert it back into a number. Return the reversed number.
def reverse_part_2(word_2):
    if type(word_2) == str:
        word_list_2 = list(word_2)
        word_list_2.reverse()
        return ''.join(word_list_2)
    else:
        num_string = str(word_2)
        rev_string = ''.join(reversed(num_string))
        return int(rev_string)

# e) Be sure to print the result returned by the function to verify that your code works for both strings and numbers. Do this before moving on to the next steps.

print(reverse_part_2('bumblebee'))
print(reverse_part_2(5678))

# 3) Create a new function with one parameter, which is the list we want to change. The function should:

# a) Define and initialize an empty list.
#def reverse_lists(list):
#    new_list = []

# b) Loop through the old list.
#def reverse_lists(list):
#    new_list = []
#    for i in list:   

# c) For each element in the old list, call reverse_characters to flip the characters or digits.

#def reverse_lists(list):
#   new_list = []
#    for i in list:
#        flip_chars_digs = reverse_part_2(i)

# d) Add the reversed string (or number) to the list defined in part ‘a’.

#def reverse_lists(list):
#    new_list = []
#    for i in list:
#        flip_chars_digs = reverse_part_2(i)
#        new_list.append(flip_chars_digs)


# e) Return the final, reversed list.

def reverse_lists(list):
    new_list = []
    for i in list:
        flip_chars_digs = reverse_part_2(i)
        new_list.append(flip_chars_digs)
    return new_list

# f) Be sure to print the results from each test case in order to verify your code.

list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']

print(reverse_lists(list_test1))
print(reverse_lists(list_test2))
print(reverse_lists(list_test3))
