# cliffordPanel.py
# https://examples.pyviz.org/attractors/clifford_panel.html#attractors-gallery-clifford-panel
import numpy as np, pandas as pd
from numba import jit

@jit(nopython=True)
def clifford_trajectory(a, b, c, d, x0, y0, n):
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n-1):
        xs[i+1] = np.sin(a * ys[i]) + c * np.cos(a * xs[i])
        ys[i+1] = np.sin(b * xs[i]) + d * np.cos(b * ys[i])
    return xs, ys

import datashader as ds
from datashader import transfer_functions as tf

from colorcet import palette_n
ps ={k:p[::-1] for k,p in palette_n.items()}

import panel as pn
pn.extension()

def clifford_plot(a=1.9, b=1.9, c=1.9, d=0.8, n=100000000, colormap=ps['kbc']):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = clifford_trajectory(a, b, c, d, 0, 0, n)
    agg = cvs.points(pd.DataFrame({'x':xs, 'y':ys}), 'x', 'y')
    return tf.shade(agg, cmap=colormap)

img = clifford_plot(a=1.7, b=1.7, c=0.6, d=1.2, n=20000000, colormap=ps['dimgray'])
pn.interact(clifford_plot, n=(1,20000000), colormap=ps)
