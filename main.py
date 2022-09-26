import tkinter as tk
from tkinter import ttk
from shedules_plt import mers_tab
def cars_stats_frame():
    root = tk.Tk()
    root.geometry('400x500')
    tk.Button(text='QUIT', command=root.destroy, fg='red').pack(side=tk.BOTTOM, fill=tk.X)
    bar1 = ttk.LabelFrame(text='Average prices by the regions')
    bar1.pack(fill=tk.BOTH)
    tk.Button(bar1, text='Mercedes <10y', command=mers_tab).pack(fill=tk.X)
    tk.Button(bar1, text='VAZ <15y').pack(fill=tk.X)
    tk.Button(bar1, text='Toyota <10y').pack(fill=tk.X)
    root.mainloop()


if __name__=='__main__':
    cars_stats_frame()
