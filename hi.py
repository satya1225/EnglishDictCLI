import os
import time
import pandas

while True:
    if os.path.exists('temps_today.csv'):
        df = pandas.read_csv('temps_today.csv')
        print(df.mean())
    else:
        print('Path does not exist')
    time.sleep(3)
