%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
indicator2 = pd.read_csv('indicator2.csv')
plt.figure(figsize=(10,8))
colors = ("red", "green", "blue", "yellow", "orange", "black", "gray")
def attribute_color(region):
    colors = {
        'East Asia & Pacific (all income levels)':'red',
        'Europe & Central Asia (all income levels)':'green',
        'Latin America & Caribbean (all income levels)':'blue',
        'Middle East & North Africa (all income levels)':'yellow',
        'North America':'orange', 
        'South Asia':'black', 
        'Sub-Saharan Africa (all income levels)':'gray'
    }
    return colors.get(region, 'white')
color_region = list()
qty_states = len(indicator2['region'])
 
for state in range(qty_states):
    color_region.append(attribute_color(indicator2['region'][state]))
plt.scatter(x = indicator2['GDP_per_capita'],
            y = indicator2['life_expectancy'],
            s = indicator2['population_total']/1000000,
            c = color_region,
            alpha = 0.6)
plt.title('GDP per Capita vs. Life Expectancy 2015', fontsize=20)
plt.xlabel('GDP per Capita(USD)')
plt.ylabel('Life Expectancy(years)')
plt.ylim(0, 100)
regions = ['East Asia & Pacific (all income levels)', 'Europe & Central Asia (all income levels)', 'Latin America & Caribbean (all income levels)', 
           'Middle East & North Africa (all income levels)', 'North America', 'South Asia', 'Sub-Saharan Africa (all income levels)']
legend1_line2d = list()
for step in range(len(colors)):
    legend1_line2d.append(mlines.Line2D([0], [0],
                                        linestyle='none',
                                        marker='o',
                                        alpha=0.6,
                                        markersize=6,
                                        markerfacecolor=colors[step]))
legend1 = plt.legend(legend1_line2d,
                     regions,
                     numpoints=1,
                     fontsize=10,
                     loc='lower right',
                     shadow=True)
legend2_line2d = list()
legend2_line2d.append(mlines.Line2D([0], [0],
                                    linestyle='none',
                                    marker='o',
                                    alpha=0.6,
                                    markersize=np.sqrt(10),
                                    markerfacecolor='#D3D3D3'))
legend2_line2d.append(mlines.Line2D([0], [0],
                                    linestyle='none',
                                    marker='o',
                                    alpha=0.6,
                                    markersize=np.sqrt(100),
                                    markerfacecolor='#D3D3D3'))
legend2_line2d.append(mlines.Line2D([0], [0],
                                    linestyle='none',
                                    marker='o',
                                    alpha=0.6,
                                    markersize=np.sqrt(1000),
                                    markerfacecolor='#D3D3D3'))
 
legend2 = plt.legend(legend2_line2d,
                     ['1', '10', '100'],
                     title='Population (in million)',
                     numpoints=1,
                     fontsize=10,
                     loc='lower left',
                     frameon=False, 
                     labelspacing=3,
                     handlelength=5,
                     borderpad=4  
                    )
plt.gca().add_artist(legend1)
 
plt.setp(legend2.get_title(),fontsize=10)
plt.savefig('matplotlib.png')