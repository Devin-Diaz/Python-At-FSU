'''
Joe's Automotive performs the following routine maintenance services: (20)
    Oil change—$30.00
    Lube job—$20.00
    Radiator flush—$40.00
    Transmission flush—$100.00
    Inspection—$35.00
    Muffler replacement—$200.00
    Tire rotation—$20.00
Write a GUI program with check buttons that allow the user to select any or all of these services.
When the user clicks a button, the total charges should be displayed
'''

import tkinter as tk
from tkinter import messagebox

# functionality for the checkboxes by appending their value to total, displays the value via message box
def show_status():
    total = 0
    if var1.get():
        total += 30
    if var2.get():
        total += 20
    if var3.get():
        total += 40
    if var4.get():
        total += 100
    if var5.get():
        total += 35
    if var6.get():
        total += 200
    if var7.get():
        total += 20
    
    messagebox.showinfo("Total Charges", f"Total charges: ${total:.2f}")

# creates window frame
root = tk.Tk()
root.title('Joe\'s Automotive')
root.geometry('300x300')

# variables to recognize whether checkbox is clicked or not
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()
var4 = tk.BooleanVar()
var5 = tk.BooleanVar()
var6 = tk.BooleanVar()
var7 = tk.BooleanVar()

# all checkboxes with text and value in string format
checkbox1 = tk.Checkbutton(root, text="Oil Change - $30.00", variable=var1)
checkbox1.pack(pady=5)

checkbox2 = tk.Checkbutton(root, text="Lube Job - $20.00", variable=var2)
checkbox2.pack(pady=5)

checkbox3 = tk.Checkbutton(root, text="Radiator Flush - $40.00", variable=var3)
checkbox3.pack(pady=5)

checkbox4 = tk.Checkbutton(root, text="Transmission Flush - $100.00", variable=var4)
checkbox4.pack(pady=5)

checkbox5 = tk.Checkbutton(root, text="Inspection - $35.00", variable=var5)
checkbox5.pack(pady=5)

checkbox6 = tk.Checkbutton(root, text="Muffler Replacement - $200.00", variable=var6)
checkbox6.pack(pady=5)

checkbox7 = tk.Checkbutton(root, text="Tire Rotation - $20.00", variable=var7)
checkbox7.pack(pady=5)

# main button to display information
display_button = tk.Button(root, text='Show Total', command=show_status)
display_button.place(x=50, y=260)

# quit button with functionality
quit_button = tk.Button(root, text='Quit', command=root.quit)
quit_button.place(x=200, y=260)

# begins program
root.mainloop()
