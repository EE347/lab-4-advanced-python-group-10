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


plt.figure(figsize=(10,6))


plt.plot(dates, META, label = 'META')
plt.plot(dates, AAPL, label = 'AAPL')
plt.plot(dates, AMZN, label = 'AMZN')
plt.plot(dates, NFLX, label = 'NFLX')
plt.plot(dates, NVDA, label = 'NVDA')
plt.plot(dates, GOOGL, label = 'GOOGL')

plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('FAANG Performance')

plt.show()
        