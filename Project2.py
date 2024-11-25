from itertools import permutations

# A small example list of valid words (you can expand this)
valid_words = {
    "cat", "dog", "god", "act", "taco", "coat", "at", "to", "a", "c", 
    "bat", "tab", "cab", "bad", "dad", "add", "cot", "dot", "od", "cat", 
    "coat", "taco", "toad", "coat", "cart", "dart", "rat", "tar", "art"
}

def can_form_word(letters):
    # Check for all permutations of the letters
    for i in range(1, len(letters) + 1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if word in valid_words:
                return word  # Return the first valid word found
    return None

def main():
    user_input = input("Enter 6 letters: ")
    
    if len(user_input) != 6:
        print("Please enter exactly 6 letters.")
        return
    
    word = can_form_word(user_input)
    
    if word:
        print(f"Yes, the word '{word}' can be formed.")
    else:
        print("No, a word cannot be formed with these letters.")

if __name__ == "__main__":
    main()