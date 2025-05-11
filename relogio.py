import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, update_time)

root = tk.Tk()
root.title('Relógio')

label = tk.Label(root, font=('calibri', 40, 'bold'), background='blue', foreground='white')
label.pack(anchor='center')

update_time()

root.mainloop()
