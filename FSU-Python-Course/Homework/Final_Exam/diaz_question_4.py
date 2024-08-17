'''
Write a GUI program that displays your name and address when a button “Show Info” is clicked. The
application should close when a “Quit” button is clicked (See below for a design).
'''

import tkinter as tk

# gives button functionality upon clicking
def info_button_action():
    info_label.config(text='Devin Diaz\n21 Jump Street\nBoston, MA 02135')

# creates window frame
root = tk.Tk()
root.title("Devin's Info")
root.geometry('300x300')

# main label to display info
info_label = tk.Label(root, text='')
info_label.pack(pady=20)
info_label.place(x=100,y=100)

# show info button and styling
show_info_button = tk.Button(root, text='Show Info', command=info_button_action)
show_info_button.pack(pady=10)

# quit button and styling, has functionality to quit
quit_button = tk.Button(root, text='Quit', command=root.quit)
quit_button.pack(pady=10)

# positioning for buttons
show_info_button.place(x=50, y=200)
quit_button.place(x=200, y=200)

# begins program
root.mainloop()
