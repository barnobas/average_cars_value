from mercedes import mers_parse
import pandas as pd
import matplotlib.pyplot as plt


def mers_tab():
    town_price = pd.Series(mers_parse())
    plt.title('Current average price')
    plt.bar(town_price.index, height=town_price)
    plt.show()