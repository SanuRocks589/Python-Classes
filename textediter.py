from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("My text editor")
window.geometry("400x300")
window.rowconfigure(0,minsize=800, weight=2)
window.columnconfigure(1, minsize=800, weight=2)

def opnfile():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"),("All Files", "*.*")]
    )
    if not filepath:
        return 
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text=input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
    window.title(f"My text editor-{filepath}")

def savefile():
    filepath = asksaveasfilename(
        filetypes=[("Text Files", "*.txt"),("All Files", "*.*")]
    )
    if not filepath:
        return 
    txt_edit.delete(1.0, END)
    with open(filepath, "w") as output_file:
        text=output_file.read()
        txt_edit.insert(END, text)
        output_file.close()
    window.title(f"My text editor-{filepath}")

txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=opnfile)
btn_save = Button(fr_buttons, text="Save As...", command=savefile)