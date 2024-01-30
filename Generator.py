import random
import tkinter as tk

# The Character Pools to use
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

# Create a all character pool to use as default
all_character_pool = lowercase_letters + uppercase_letters + numbers + symbols

# Getting required information from the user
def getPasswordLength():
    password_length = int(length_entry.get())
    return password_length
            
            
def getThePools():
    characterPool = ""
    if lowercase_var.get():
        characterPool += lowercase_letters
    if uppercase_var.get():
        characterPool += uppercase_letters
    if number_var.get():
        characterPool += numbers
    if symbol_var.get():
        characterPool += symbols
    
    return characterPool


# Update the button state
def update_button_state():
    length = length_entry.get()
    is_valid = validate_length(length)
    generate_button.config(state="normal" if is_valid else "disabled")

# Generating the password
def generatePassword(length, characterpool):
    password = ""
    if characterpool == "":
        characterpool = all_character_pool
    for _ in range(length):
        password += random.choice(characterpool)
    return password

# Checking the value and make sure it stand for the standards
def validate_length(text, current_value):
    """Validates password length input and updates button state."""

    if text.isdigit() and int(text) >= 8:
        is_valid = True
    else:
        invalid_message = tk.messagebox.showerror(
            "Invalid Length", "Password length must be at least 8 characters"
        )
        length_entry.delete(0, tk.END)
        is_valid = False

    # Update button state based on validation
    generate_button.config(state="normal" if is_valid else "disabled")

    return True  # Always return True to allow further input



# Creating the GUI Application
def GUI():
    window = tk.Tk()
    window.title("Password Generator")
    
    # Getthing the length
    length_label = tk.Label(window, text="Password length: ")
    length_label.pack()
    # Making the variable global so we can use it inside other functions   
    global length_entry, lowercase_checkbox, uppercase_checkbox, Number_checkbox, Symbol_checkbox, generate_button
    length_entry = tk.Entry(window)
    length_entry.pack()
    length_entry.config(validate="key", validatecommand=(validate_length, "%s", "%P"))
    
    # Adding checkbox to get the character types
    global lowercase_var, uppercase_var, number_var, symbol_var
    lowercase_var = tk.BooleanVar()
    lowercase_checkbox = tk.Checkbutton(window, text="Lowercase Letter", variable=lowercase_var)
    lowercase_checkbox.pack()
    uppercase_var = tk.BooleanVar()
    uppercase_checkbox = tk.Checkbutton(window, text="Uppercase Letter", variable=uppercase_var)
    uppercase_checkbox.pack()
    number_var = tk.BooleanVar()
    Number_checkbox = tk.Checkbutton(window, text="Numbers", variable=number_var)
    Number_checkbox.pack()
    symbol_var = tk.BooleanVar()
    Symbol_checkbox = tk.Checkbutton(window, text="Symbols", variable=symbol_var)
    Symbol_checkbox.pack()
    
    # Generate button
    generate_button = tk.Button(window, text="Generate Password")
    generate_button.pack()
    generate_button.config(command=run)
    
    
    # Place to show the generated password 
    global password_label
    password_label = tk.Label(window, text="")
    password_label.pack()
    
    # Run the GUI
    window.mainloop()

# Run the application
def run():
    passwordLength = getPasswordLength()
    CharacterPool = getThePools()
    
    password = generatePassword(passwordLength, CharacterPool)
    password_label.config(text=password)


# Main funtion to run the application
def main():
    GUI()


# Running the application
if __name__ == "__main__":
    main()