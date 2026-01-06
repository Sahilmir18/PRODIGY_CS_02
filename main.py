from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

filepath=""


window = tk.Tk()
window.title("Simple Image Encryption Tool made by Sahilmir18")
window.geometry("1000x600")

tk.Label(window, text= "About Image Encryption Tool", font=("Roboto", 14)).pack(anchor="w",pady=10 ,padx=10)
tk.Label(window, text= "It uses pixel manipulation. You can perform operations XOR operation to encrypt/decrypt Images.",font = ("Roboto",12)).pack(anchor="w",padx=10)

tk.Label(window, text="Choose an option (Encrypt/Decrypt):", font=("Roboto", 14)).pack(anchor="w",pady=10, padx=10)
opt = IntVar(value=1)
tk.Radiobutton(window, text = "Encrypt", variable = opt, value = 1, font=("Roboto",12)).pack(anchor="w",padx=10)
tk.Radiobutton(window, text = "Decrypt", variable = opt, value = 2, font=("Roboto",12)).pack(anchor="w",padx=10)

def Image_opening():
    global filepath # Declare the intent to modify the global variable
    filepath = filedialog.askopenfilename(title="Select a image",defaultextension= "PNG, *.png",filetypes=[("PNG","*.png"),("JPEG/JPG",".jpg")])
    if filepath:
        status_label.config(text="Image Inserted")
        messagebox.showinfo(message="Success",detail="Image Inserted Successfully!")
    
    
    
    
    

def pixel_manipulation():
    # print(filepath)
    img = Image.open(filepath)
    pixels = img.load()
    width, height = img.size

    key = int(Key.get())
    if key < 1 or key > 255:
        messagebox.showerror("Error", "Key must be between 1 and 255")
        return
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixels[x,y] = (r^key, g^key, b^key)

    save_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("PNG","*.png"),("JPEG/JPG",".jpg")])
    if save_path:
        img.save(save_path)
        messagebox.showinfo("Success", f"Image processed and saved successfully! and saved at {save_path}")


tk.Label(window,text="Enter the Key (1 to 255): ",font=("Roboto",14)).pack(anchor="w",padx=10,pady=10)
Key = tk.Entry(window, width=40)
Key.pack(anchor="w", padx=10)


tk.Label(window,text="Choose the Image:",font=("Roboto",14)).pack(anchor="w",padx=10,pady=10)
tk.Button(window,text="Choose Image",command=Image_opening,fg="black",bg="white",font=("Roboto",13)).pack(anchor="w",padx=10)
status_label = tk.Label(window,text="status: Image not choosen",font=("Roboto",11))
status_label.pack(anchor="w",padx=10)




tk.Button(window,text="Encrypt/Decrypt",command=pixel_manipulation,fg="black",bg="white",font=("Roboto",13)).pack(anchor="w",pady=10,padx=10)
output_label = tk.Label(window,text="",font=("Roboto",11))
output_label.pack(anchor="w",padx=10)
                                                                                             

window.mainloop()