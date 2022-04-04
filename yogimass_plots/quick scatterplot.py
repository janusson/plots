import seaborn as sns
import pandas as pd

plot_data = pd.read_csv('./database/mz_data.csv')

def quick_scatterplot(plot_data):
    # Plot XY scatter spectrum
    sns.set(style="whitegrid")
    sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
    sns.set_palette("husl")
    sns.set_color_codes("dark")
    sns.scatterplot(x = plot_data[0],
                    y = plot_data[1],
                    # x='m/z',
                    # y='Percent Abundance',
                    data=plot_data,
                    xlabel='m/z')
    return print('Plotting scatter spectrum...')
