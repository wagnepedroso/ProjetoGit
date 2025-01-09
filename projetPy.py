import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Janela Principal")
root.geometry("300x200+300+300")
btn = tk.Button(text="Clique-me", command=lambda: messagebox.showinfo("Message", "Bem vindo ao GitHub e Python!"))
btn.pack()

btn2 = tk.Button(text="Sair",fg="blue", command=lambda: root.quit()).pack()

root.mainloop()