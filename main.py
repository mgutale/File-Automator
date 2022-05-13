# This is file automating script that takes in an input file and writes to specific location at an interval.

# Import libraries
import pandas as pd
import datetime as dt
import os

def automate():
    # read the file
    file = pd.read_csv(os.path.join(os.getcwd(),'data/vehicles.csv'))

    # create a loop
    schedule = dt.datetime(2022, 5, 13, 11, 35, 00)
    count = 1

    while count <= 2:
        if dt.datetime.now() == schedule:
            file.to_csv(f'data/vehicles{count}.csv')
            schedule += dt.timedelta(minutes=2)
            count += 1

        else:
            time_now = dt.datetime.now()
            time_left = schedule - time_now
            minutes_left = time_left.total_seconds() / 60
            print(f'The next file will be saved in {minutes_left}')


if __name__ == '__main__':
    automate()
