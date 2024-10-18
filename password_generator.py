import random
import string
import pyperclip

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    # Character sets
    char_set = ''
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_lowercase:
        char_set += string.ascii_lowercase
    if use_digits:
        char_set += string.digits
    if use_special_chars:
        char_set += string.punctuation

    # Check if the character set is empty
    if not char_set:
        print("Error: No character set selected. Please choose at least one option.")
        return None

    # Generate the password
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def main():
    print("Password Generator Tool")
    print("=======================")

    # User input for password criteria
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Invalid input. Please enter a number for the length.")
        return

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate password based on user criteria
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)

    if password:
        print(f"Generated Password: {password}")
        # Copy to clipboard
        copy_to_clipboard = input("Would you like to copy the password to the clipboard? (y/n): ").lower()
        if copy_to_clipboard == 'y':
            pyperclip.copy(password)
            print("Password copied to clipboard!")

if __name__ == "__main__":
    main()
