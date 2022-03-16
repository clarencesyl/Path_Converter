import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Path Converter")
window.geometry('400x200')  # Window size, Width * Height.
window.configure(bg="#D3D3D3")


def convert():
    """ Converts path \ to /. Converted path is copied to clipboard automatically. """

    window.clipboard_clear()
    newPath_list = []  # Contains converted path.

    # Convert user input path str to list.
    getPath = path_txt.get("1.0", "end")
    getPath_list = list(getPath)

    # Iterate through list to do conversion.
    # Converted path is appended to a new list.
    for char in getPath_list:
        if char == "\\":
            char = "/"
            newPath_list.append(char)

        else:
            newPath_list.append(char)

    # Convert list containing new path to str.
    newPath_list.remove("\n")
    newPath_str = "".join(map(str, newPath_list))

    # Display new path str in lbl.
    newPath_lbl.config(text="Converted Path: {}".format(newPath_str))

    window.clipboard_append(newPath_str)
    path_txt.delete("1.0", "end")

    # Toggle on/off displaying of msgbox. 
    if var1.get() == 1:
        messagebox.showinfo("Info", "Converted path copied to clipboard.")

    else:
        pass


def faq():
    """ Display info on how to use program. """

    messagebox.showinfo("How To Use", "Changes path \ to / e.g. C:\\Users\\User\\Desktop -> C:/Users/User/Desktop\n\n 1. Enter a path.\n 2. Click convert button.\n 3. Converted path will be displayed and copied to your clipboard automatically.\n 4. Check/Uncheck box to toggle displaying of alert after every successful conversion.")


# User input path to be converted.
path_txt = tk.Text(window, height=5, width=20, bg="#D3D3D3")
path_txt.pack()

# Execute path conversion.
convert_btn = tk.Button(window, text="Convert", bg="#D3D3D3", command=convert)
convert_btn.pack()

# Toggle on/off displaying of msgbox.
var1 = tk.IntVar(value=1)  # Set chkbox to be checked by default.
msgbox_chkbox = tk.Checkbutton(window, text="On/Off Alert", bg="#D3D3D3", variable=var1, onvalue=1, offvalue=0)
msgbox_chkbox.pack()

# Display converted path.
newPath_lbl = tk.Label(window, text="Converted Path: ", bg="#D3D3D3")
newPath_lbl.pack()

# Display info on how to use program.
faq_btn = tk.Button(window, text="How To Use", bg="#D3D3D3", command=faq)
faq_btn.pack()

# Run the script.
window.mainloop()


# Written by: Clarence Seah.
