# colormap.py
# File for choosing colormaps

## Choosing a colormap with colorcet (holoviz)
from colorcet.plotting import swatch, swatches, candy_buttons
import holoviews as hv
hv.extension('bokeh')

from colorcet import bmw, colorwheel, isolum, bkr, bgy, bgyw, kbc, bmw, bmy, kb, bkr, CET_CBL2
#https://colorcet.holoviz.org/user_guide/Continuous.html
candy_buttons('CET_CBL2', bgcolor='white') + candy_buttons('CET_CBL2', bgcolor='black')