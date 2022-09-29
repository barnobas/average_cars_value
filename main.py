import tkinter as tk
from tkinter import ttk
from shedules_plt import pandas_bar
from sql_db import *


def cars_stats_frame():
    root = tk.Tk()
    root.geometry('400x500')

    tk.Button(text='QUIT', command=root.destroy, fg='red').pack(side=tk.BOTTOM, fill=tk.X)

    tk.Label(text='Average price by the region').pack()

    bar1 = ttk.LabelFrame()
    bar1.pack(fill=tk.BOTH)
    tk.Button(bar1, text='Update', command=lambda button='button1', dp_car='mercedes-benz',
                                                  dp_year='2012': db_update(button, dp_car, dp_year), fg='green').pack(
        side=tk.RIGHT)
    tk.Button(bar1, text='Mercedes <10y', command=lambda button='button1': pandas_bar(button)).pack(fill=tk.X)

    bar2 = ttk.LabelFrame()
    bar2.pack(fill=tk.BOTH)
    tk.Button(bar2, text='Update', command=lambda button='button2', dp_car='lada',
                                                  dp_year='2012': db_update(button, dp_car, dp_year), fg='green').pack(
        side=tk.RIGHT)
    tk.Button(bar2, text='Lada', command=lambda button='button2': pandas_bar(button)).pack(fill=tk.X)

    bar3 = ttk.LabelFrame()
    bar3.pack(fill=tk.BOTH)
    tk.Button(bar3, text='Update', command=lambda button='button3', dp_car='toyota',
                                                  dp_year='2012': db_update(button, dp_car, dp_year), fg='green').pack(
        side=tk.RIGHT)
    tk.Button(bar3, text='Toyota', command=lambda button='button3': pandas_bar(button)).pack(fill=tk.X)

    root.mainloop()


if __name__ == '__main__':
    sql_start()
    cars_stats_frame()
