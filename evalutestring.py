#make a letter variable in range of alphabet
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#ask user to input the letters range
range_of_letters = input("enter a range of letters (ex: a-z or a-g): \n")
#split the letters range by hyphen "-"
split = range_of_letters.split("-")
#make the variable name start and end by their position in range_of_letters
start = letters.index(split[0])
end = letters.index(split[1])
#use [] to make the range of letters by the user's order
result_letters_range = letters[start:end + 1]
#print the result
result_display = print(result_letters_range)