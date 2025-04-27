from tkinter import *
from datetime import date 

root = Tk()
root.title('Login App')
root.geometry('500x500')
root.configure(bg="#E8F0F2")

Ibl = Label(root, text="Hey There!", fg="white", bg="#072F5F", width=30)
name_lbl = Label(root, text="Full Name", bg="#3895D3", width=30)
name_entry = Entry(root, width=30)
email_lbl = Label(root, text="Email ID", bg="#3895D3", width=30)
email_entry = Entry(root, width=30)
class_lbl = Label(root, text="Class:", bg="#3895D3", width=30)
class_entry = Entry(root, width=30)
fav_lbl = Label(root, text="Favorite Subjects:", bg="#3895D3", width=30)
fav_entry = Entry(root, width=30)
password_lbl = Label(root, text="Enter password", bg="#3895D3", width=30)
password_entry = Entry(root, show="*", width=30)

def display():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    fav = fav_entry.get()
    class1 = class_entry.get()

    greet = f"Hello {name}!\n"
    message = "Congratulations on your new account!"
    
    text_box.delete('1.0', END)  
    text_box.insert(END, greet + message)

text_box = Text(root, height=5, width=40, bg="#D3E3FC")
btn = Button(root, text="Create Account", command=display, bg="#1261A0", fg='white', width=15)

Ibl.pack(pady=10)
name_lbl.pack()
name_entry.pack(pady=5)
email_lbl.pack()
email_entry.pack(pady=5)
password_lbl.pack()
password_entry.pack(pady=5)
fav_lbl.pack()
fav_entry.pack(pady=5)
class_lbl.pack()
class_entry.pack(pady=5)
btn.pack(pady=10)
text_box.pack(pady=10)

root.mainloop()
