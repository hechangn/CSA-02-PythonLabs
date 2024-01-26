# Prompt the user for input
letter_range = input("Enter a range of letters: ")

# Separate the input string into start and end
start = letter_range[0]
end = letter_range[2]

# Initialize an empty string to store the result
result = ""

# Repeat over the ASCII values from start to end
for i in range(ord(start), ord(end) + 1):
# Convert each ASCII value back to a character and add it to the result
    result += chr(i)

# Print the result
print(result)

