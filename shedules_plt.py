import pandas as pd
import matplotlib.pyplot as plt
import sqlite3


def pandas_bar(button):
    town_price = pd.read_sql(f'SELECT * FROM {button}', con=sqlite3.connect('cars_prices.db'))
    plt.title('Average price by the region')
    plt.bar(town_price['town'], height=town_price['price'])
    plt.show()
