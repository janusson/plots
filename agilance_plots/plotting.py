import pandas as pd
from scipy.stats import linregress
import matplotlib.pyplot as plt
import numpy as np
from os import path

#* data import
data = pd.read_csv(path.abspath(input('Enter .csv data path: ')))
type(data)
x,y = data.loc[0], data.loc[1]


#* plotting
data.plot(x='x', y='y', kind='scatter')
plt.xlabel('x')
plt.ylabel('y')
# plt.legend(loc='upper left')
plt.show()

# Fitting
params, cov = curve_fit(f, x, y)
