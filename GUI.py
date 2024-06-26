import customtkinter as ctk


# Create the main window
def GUI():
    window = ctk.CTk()
    window.title("Password Generator")
    window.geometry("800x600")
    ctk.set_appearance_mode('dark')


    # Adding the components
    # Title frame
    Titleframe = ctk.CTkFrame(window, width=600, height=100, fg_color="transparent")
    TitleLable = ctk.CTkLabel(Titleframe, text="Password Generator", font=("Arial", 24), justify="center", pady=20)
    TitleLable.pack()
    Titleframe.pack()
    
    # input frame
    Inputframe = ctk.CTkFrame(window, width=600, height=300)
    LengthLabel = ctk.CTkLabel(Inputframe, text="Password length: ", font=("Arial", 14), justify="left", pady=10, padx=20)
    LengthInput = ctk.CTkEntry(Inputframe, width=200, font=("Arial", 14))
    LengthLabel.pack(side="left")
    LengthInput.pack(side="right")
    Inputframe.pack()
    # checkbox frame
    
    

    
    window.mainloop()
    

    # Creating a main class to run the application indivdualy
def main():
    GUI()
    

if __name__ =="__main__":
    main()

