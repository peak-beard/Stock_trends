
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')

def console_input() :

    i = input('$ ')
    if i == 'exit':
        exit()

    elif i == 'update':
        update()
        print('Sucessfully updated tesla.csv')
        console_input()

    else:
        print('Command not found.')
        console_input()



def update() :
    stop = dt.date.today()
    start = stop - dt.timedelta(days=365)
    print(start)
    df = web.DataReader('TSLA', 'yahoo', start, stop)
    df.to_csv('tesla.csv')


df = pd.read_csv('tesla.csv', parse_dates=True)
#df['Adj Close'].plot()
#plt.show()
axis_y = df['Adj Close']
axis_x = df['Date']
#print(axis_x)
m = len(axis_y)

print(m)