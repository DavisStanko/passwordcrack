from itertools import product

# Max password length for memory saving
MAX_LENGTH = 4

# Types of characters to use in cracking password
NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
CAPITAL_LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
SPECIAL_CHARS = [" ", "!", "”", "#", "$", "%", "&", "’", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]


def crack_Password(password, verbose, master_List):
    # Set max length of password as a for loop to save memory
    for i in range(MAX_LENGTH):
        # Get all possible combinations of characters
        combinations = list(product(master_List, repeat=i))
        # Format the combinations
        combinations = [''.join(i) for i in combinations]
        # Reset the number of attempts for verbose mode
        attempt_Number = 1
        # Crack the password
        for i in combinations:
            attempt = i
            # Calculate and print verbose mode information
            if verbose == True:
                attempt_Number += 1
                print(f"Attempt {attempt_Number}: {attempt}")
            # Check if password is correct
            if attempt == password:
                end(attempt)


def password_Input():
    password = input("Please enter a password to be tested: ")
    # Check if password is correct length
    if len(password) > MAX_LENGTH:
        print(f"Password is too long. Please try a password of less than {MAX_LENGTH} characters.")
        password_Input()
    else:
        return password


def intro():
    # default settings
    verbose = False
    master_List = NUMBERS + LETTERS + CAPITAL_LETTERS + SPECIAL_CHARS

    # Get password from user
    print("Welcome to the password cracker!")
    print("This program will attempt to crack a password.")
    password = password_Input()
    print(f"The password you entered is: {password}")

    # Skip settings?
    advanced_Mode = input("Would you like to edit the settings? (y/n)")

    # Advanced settings
    if advanced_Mode.lower() == "y":
        # Edit verbose mode
        verbose = input("Verbose mode? (y/n)")
        if verbose.lower() == "y":
            verbose = True

        # Edit list of characters use to crack password
        charset = input("Would you like to edit the character list? (y/n)")
        if charset.lower() == "y":
            # Reset master list
            master_List = []
            lowercase = input("Would you like to include lowercase letters? (y/n)")
            # Add lowercase letters to master list
            if lowercase.lower() == "y":
                master_List = master_List + LETTERS
            # Add uppercase letters to master list
            uppercase = input("Would you like to include uppercase letters? (y/n)")
            if uppercase.lower() == "y":
                master_List = master_List + CAPITAL_LETTERS
            # Add numbers to master list
            numbers = input("Would you like to include numbers? (y/n)")
            if numbers.lower() == "y":
                master_List = master_List + NUMBERS
            # Add special characters to master list
            special_Chars = input("Would you like to include special characters? (y/n)")
            if special_Chars.lower() == "y":
                master_List = master_List + SPECIAL_CHARS

    print(f"The master list is: {master_List}")
    input("Press enter to continue...")
    crack_Password(password, verbose, master_List)


def end(attempt):
    print("Password cracked!")
    print("The password was:")
    print(attempt)
    print("Thank you for using the password cracker.")
    restart = input("Would you like to crack another password? (y/n)")
    if restart.lower() == "y":
        intro()
    else:
        print("Thank you for using the password cracker.")
        exit()


intro()
