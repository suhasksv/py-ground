import tkinter as tk

window = tk.Tk()
message = tk.Label(text="Enter your name")
entry = tk.Entry()
message.pack()
entry.pack()

window.mainloop()
