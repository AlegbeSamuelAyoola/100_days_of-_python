def is_palindrome_recursive(word):
    # Base case: if the word is empty or has one character, it's a palindrome
    if len(word) <= 1:
        return True
    # Recursive case: check the first and last characters, then the rest of the word
    if word[0] == word[-1]:
        return is_palindrome_recursive(word[1:-1])
    return False

# Main program to take input from the user and check if it's a palindrome
word = input("Enter a word: ").lower()  # Convert to lowercase for case-insensitive check

if is_palindrome_recursive(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
