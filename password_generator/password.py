import random
import string
import tkinter as tk
from tkinter import messagebox

char = '@#$&*_'
password=""
pw_visible = False

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + char
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def password_visible():
    global pw_visible
    pw_visible = not pw_visible
    if pw_visible:
        password.entry.comfig(show="")
        show_butn.config(text="Hide Password")
        password_entry.delete(0,tk.END)
        password_entry.insert(0,password)
    else:
        password_entry.config(show="")
        show_butn.config(text="Show Password")
        password_entry.delete(0,tk.END)
        password_entry.insert(0,'*'*len(password))

def generate_pw_butn():
    global password,password_visible
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error","Password length should be greater than 0.")
        else:
            password= generate_password(length)
            password_entry.delete(0,tk.END)
            password_entry.insert(0,'*' * len(password))
            show_button.config(state='normal')
            password_visible = False
    except ValueError:
        messagebox.showerror("Error","Invalid Input.Plz enter a valid number for password length`   q")

root = tk.Tk()
root.title = "Password Generator"

length_label = tk.Label(root,text = "Enter Password Length")
length_label.grid(row=0 , column=0,sticky="w")

length_entry = tk.Entry(root)
length_entry .grid(row =0,column=1,sticky="e")

generate_butn = tk.Button(root,text="Generate password",command=generate_pw_butn,fg="red",bg="cyan")
generate_butn.grid(row=1,column=0,sticky="w")

password_entry = tk.Entry(root,show ="")
password_entry.grid(row=1,column=1,columnspan=2,sticky="w")

show_butn = tk.Button(root,text='Show Password',command= password_visible ,state = "disabled",fg ='brown',
              font = ("Arial",12,bold))
pw_visible = False
        