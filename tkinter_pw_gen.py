
#--------------------------------------------------------------------------------------------------------------------------------------------

#   ╭∩╮    ╭∩╮
#    \(͡⚈ᴗ͡⚈)/

#--------------------------------------------------------------------------------------------------------------------------------------------

# Modules


from tkinter import *  
import random
import pyperclip

#---------------------------------------------------------------------------------------------------------------------------------------

# Global Variables

window = Tk()
window.title('calV s Password Generator')
window.geometry("900x500")
window.configure(bg='#303135')
passwrd = StringVar()
passlen = IntVar()
passlen.set(0)

#----------------------------------------------------------------------------------------------------------------------------------------

def generate():  # Generate Password Function
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']
    password = ""
    for x in range(passlen.get()):
        password = password + random.choice(pass1)
    passwrd.set(password)

#-------------------------------------------------------------------------------------------------------------------------------

# Copy Password Function

def copytoclipboard():
    random_password = passwrd.get()
    pyperclip.copy(random_password)


#---------------------------------------------------------------------------------------------------------------------------------

# Text
 
Label(window, text="Password Generator", font="Courier 30 italic").pack()
Label(window, text="made by calV", font="Courier 15 bold").pack()
Label(window, text="Enter the number of places for your Password").pack(pady=3)
Entry(window, textvariable=passlen).pack(pady=3)
Button(window, text="Generate", command=generate).pack(pady=7)
Entry(window, textvariable=passwrd).pack(pady=3)
Button(window, text="Copy to clipboard", command=copytoclipboard).pack()
window.mainloop()

