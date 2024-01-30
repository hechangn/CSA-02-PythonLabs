# Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter.
# Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes a hyphen will separate the two letters in the string.

#alphabet = "abcdefghijklmnopqrstuvwxyz"

#user_range = input("Enter a range of letters (e.g., a-z): ")

#print(result_string)


#make a letter variable in range of alphabet
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#ask user to input the letters range
user_range = input("enter a range of letters (e.g., a-z): \n")
#split the letters range by hyphen "-"
split = user_range.split("-")
#make the variable name start and end by their position in range_of_letters
start = alphabet.index(split[0])
end = alphabet.index(split[1])
#use [] to make the range of letters by the user's order
result_string = alphabet[start:end + 1]
#print the result
result_display = print(result_string)

