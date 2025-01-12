import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Taxonomy and Frames")

tree = ttk.Treeview(root)
tree.heading("#0", text="Taxonomy", anchor="w")

tree.pack(fill="both", expand=True)

root.geometry("400x300")
root.mainloop()