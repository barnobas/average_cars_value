import sqlite3 as sql
from Car_parse import car_parse


def sql_start():
    global base, cur
    base = sql.connect('cars_prices.db')
    cur = base.cursor()
    base.commit()


def db_update(button, dp_car, dp_year):
    car = dp_car
    year = dp_year

    base.execute(f'DROP TABLE IF EXISTS {button}')
    base.commit()

    base.execute(f'CREATE TABLE IF NOT EXISTS {button}(town TEXT, price BLOB)')
    base.commit()

    cur.executemany(f'INSERT INTO {button} VALUES(?, ?)', list(car_parse(car, year).items()))
    base.commit()
