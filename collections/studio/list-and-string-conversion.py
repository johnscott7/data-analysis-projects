proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
for s in strings:
    print(f"Original: {s}")

    if "," in s:
        print("There are commas in this.")
    if ";" in s:
        print("There are semicolons in this.")
    if " " in s:
        print("There are spaces in this.")
    if not("," in s or ";" in s or " " in s):
        print("There are no commas, semicolons, or spaces.")


# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.
for s in strings:
    print(f"Original: {s}")
    
    if "," in s:
        words = s.split(",")
        words.reverse()
        new_string = ",".join(words)
        print("flip it and reverse it:", new_string)


# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
for s in strings:
    print(f"Original: {s}")
    
    if ";" in s:
        words = s.split(";")
        words.sort()
        new_string = ",".join(words)
        print("easy as abc:", new_string)


# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.
for s in strings:
    print(f"Original: {s}")
    
    if " " in s:
        words = s.split(" ")
        words.sort(reverse=True)
        new_string = " ".join(words)
        print("easy as zyx:", new_string)


# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
for s in strings:
    print(f"Original: {s}")
    
    if ", " in s:
        words = s.split(", ")
        words.reverse()
        new_string = ",".join(words)
        print("part b with no spaces:", new_string)