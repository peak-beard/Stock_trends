import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import datedelta as dd
import time


style.use('ggplot')
df = pd.read_csv('tesla.csv')
y_true = df['Adj Close']
x_true = df['Date']
m = len(x_true)



def console_input() :

    i = input('$ ')
    if i == 'exit':
        exit()

    elif i == 'update':
        update()
        print('Sucessfully updated tesla.csv')
        console_input()
    elif i == 'plot' :
        plot()

    else:
        print('Command not found.')
        console_input()

def update() :
    stop = dt.date.today()
    start = stop - dd.datedelta(days=365)
    print(stop)
    print(start)
    df = web.DataReader('TSLA', 'yahoo', start, stop)
    df.to_csv('tesla.csv')
    print(start + dd.datedelta(days=365))

def plot() :
    df['Adj Close'].plot()
    plt.show()
    time.sleep(5)
    console_input()


def h(x, d0, d1) :
    y_pred = x * d1

    return y_pred

#print(h(x_true[1], 0, 1))
console_input()
