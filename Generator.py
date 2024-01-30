import random

# The Character Pools to use
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

# Create a all character pool to use as default
all_character_pool = lowercase_letters + uppercase_letters + numbers + symbols

# Getting required information from the user
def getPasswordLength():
    while (True):
        try:
            length = int(input("Enter the length of the password to be generated: \n"))
            if length >= 8:
                return length
            else:
                print("Password should be longer than 8 characters. ")
        except ValueError:
            print("Invalid data type enter a number.")
            
            
def getThePools():
    characterPool = ""
    while (True):
        if input("If you want to add lowercase Letter enter y: ").lower() == "y":
            characterPool += lowercase_letters
        if input("If you want to add uppercase Letters enter y: ").lower() == "y":
            characterPool += uppercase_letters
        if input("If you want to add numbers enter y:").lower() == "y":
            characterPool += numbers
        if input("If you want to add symbols enter y: ").lower() == "y":
            characterPool += symbols
        if characterPool != "":
            break
    
    return characterPool

# Generating the password
def generatePassword(length, characterpool):
    password = ""
    for _ in range(length):
        password += random.choice(characterpool)
    return password

# Main funtion to run the application
def main():
    passwordLength = getPasswordLength()
    CharacterPool = getThePools()
    
    password = generatePassword(passwordLength, CharacterPool)
    
    print(password)
    


# Running the application
if __name__ == "__main__":
    main()