from tkinter import font
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
root.title('Image to PDF Converter')

canvas1 = tk.Canvas(root, width = 300, height = 300 ,bg='black' ,relief = 'flat')
canvas1.pack()

label1 = tk.Label(root, text='Image to PDF Converter' ,bg='black' ,fg='white')
label1.config(font=('helvetica', 18))
canvas1.create_window(150, 60, window=label1)

# Open File Function
def openFile():
    global im1

    import_file_path = filedialog.askopenfilename(initialdir = "/", title = "Select an Image", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    image1 = Image.open(import_file_path)
    im1 = image1.convert('RGB')

# Open File Button
browseButton = tk.Button(text="     Select File     ",bg='purple1', fg='white' ,command=openFile, font=('helvetica', 12, 'bold'), relief = 'flat')
canvas1.create_window(150, 130, window=browseButton)

# Convert to PDF Function
def convertFile():
    global im1

    export_file_path = filedialog.asksaveasfilename(defaultextension='.pdf')
    im1.save(export_file_path)

# Save File Button
saveAsButton = tk.Button(text="Convert to PDF", bg="purple1", fg="white",command=convertFile ,font=("helvetica", 12, "bold"), relief="flat")
canvas1.create_window(150, 180, window=saveAsButton)

def exitApplication():
    MsgBox = tk.messagebox.askquestion('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
        root.destroy()

exitButton = tk.Button(text="Exit Application", bg="black", fg="white", command=exitApplication, font=("helvetica", 12, "bold"), relief="flat")
canvas1.create_window(150, 230, window=exitButton)



root.mainloop()