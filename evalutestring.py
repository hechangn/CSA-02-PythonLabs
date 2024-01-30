#make a letter variable in range of alphabet
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#ask user to input the letters range
user_range = input("enter a range of letters (ex: a-z or a-g): \n")
#split the letters range by hyphen "-"
split = user_range.split("-")
#make the variable name start and end by their position in range_of_letters
start = alphabet.index(split[0])
end = alphabet.index(split[1])
#use [] to make the range of letters by the user's order
result_string = alphabet[start:end + 1]
#print the result
result_display = print(result_string)

