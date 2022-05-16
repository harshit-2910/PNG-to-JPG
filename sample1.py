from glob import glob
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image #istalled Pillow Using pip3

root = tk.Tk() #root_func_initialzed
canvas= tk.Canvas(root, width=400, height=400, bg='gray', relief='raised')
canvas.pack()

label= tk.Label(root, text='PNG TO JPG', bg='gray')
label.config(font=('helvetica',22))
canvas.create_window(150,180, window=label)

#creating function to obtain the File
def getPNG():
    global img
    import_file_path= filedialog.askopenfilename() #variable created to the file name
    img = Image.open(import_file_path).convert('RGB')

browseButton_PNG = tk.Button(text='Import PNG File', command=getPNG)
canvas.create_window(350,350, window=browseButton_PNG)


def convertToJPG():
    global img
    export_file_path= filedialog.asksaveasfilename(defaultextension='.jpg')
    img.save(export_file_path)

saveAsButton_JPG=tk.Button(text='Convert To JPG', command=convertToJPG)
canvas.create_window(300,300, window=saveAsButton_JPG)

root.mainloop()