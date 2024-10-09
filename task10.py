import csv
import matplotlib.pyplot as plt
from datetime import datetime


dates = []
META = []
AAPL = []
AMZN = []
NFLX = []
NVDA = []
GOOGL = []

with open('/home/pi/ee347/lab-4-advanced-python-group-10/task9.csv', 'r') as file:
        reader = csv.reader(file)


        next(reader)

        for row in reader:
                
                dates.append(datetime.strptime(row[0], '%d/%m/%Y'))
                META.append(float(row[1]))
                AAPL.append(float(row[2]))
                AMZN.append(float(row[3]))
                NFLX.append(float(row[4]))
                NVDA.append(float(row[5]))
                GOOGL.append(float(row[6]))


colors = {
        'META': 'blue',
        'AAPL': 'grey',
        'AMZN': 'black',
        'NFLX': 'red',
        'NVDA': 'green',
        'GOOGL': 'orange'
}

plt.figure(figsize=(12,6))


plt.plot(dates, META, label = 'META: +184.22%', color = colors['META'])
plt.plot(dates, AAPL, label = 'AAPL: +126.56%', color = colors['AAPL'])
plt.plot(dates, AMZN, label = 'AMZN: +141.56%', color = colors['AMZN'])
plt.plot(dates, NFLX, label = 'NFLX: +139.34%', color = colors['NFLX'])
plt.plot(dates, NVDA, label = 'NVDA: +290.15%', color = colors['NVDA'])
plt.plot(dates, GOOGL, label = 'GOOGL: +119.09%', color = colors['GOOGL'])

plt.legend(loc = 'upper left')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('FAANG Performance')

plt.show()
        