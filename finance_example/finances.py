# finances.py
# 24 months employ simulation
# Python 3.7.4 

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
dataPath = r'D:\Programming\Plotting\Financial Example\dataCsv.csv'
data = pd.read_csv(dataPath)
data

data.drop(['Sort Code', 'Account Number'], axis=1)
data.reset_index()
keepRows, num = [], 0
for item in data['Transaction Description']:
    num+=1
    if item.upper().endswith('UNIV OF GLASGOW'):
        print(item)
        print(num)
        keepRows.append(num)
print(keepRows)

deposits, dates = ['Amount'], ['Date']
for row in keepRows:
    deposits.append(data['Debit Amount'][row])
    dates.append(data['Transaction Date'][row])

plt.plot(dates, deposits)
plt.show()