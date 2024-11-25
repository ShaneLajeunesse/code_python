def is_palindrome(word):
    # Normalize the word by converting it to lowercase
    normalized_word = word.lower()
    # Check if the word is the same forwards and backwards
    return normalized_word == normalized_word[::-1]

# Get input from the user
user_input = input("Please enter a word: ")

# Check if the input is a palindrome and print the result
if is_palindrome(user_input):
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")