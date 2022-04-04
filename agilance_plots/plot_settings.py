#! /usr/bin/python

import matplotlib as mpl
from os import path
from matplotlib import pyplot as plt
import pandas as pd


#* MPL RC Params Settings
def mpl_plot_settings():
    '''
    Custom Delic Labs colour schemes and Matplotlib plot setup.
    '''
    # Delic Labs palette
    delic_labs_palette = ('#00008A', '#FBC700', '#08C1CD', '#60E970',
                          '#0062FF', '#0000CB')

    # MPL Plot Settings
    colors = mpl.cycler(
        'color', delic_labs_palette
    )  #? colors = cycler('color', delic_labs_palette) for rotating through colours
    plt.rc('axes',
           edgecolor='gray',
           axisbelow=False,
           grid=False,
           prop_cycle=colors)
    plt.rc('grid', c='0.5', ls='-', lw=0.1)
    plt.rc('xtick', direction='out', color='gray')
    plt.rc('ytick', direction='out', color='gray')
    plt.rc('patch', edgecolor='#003f5c')
    plt.rc('lines', linewidth=0.18, aa=True)
    font = {'family': 'arial', 'weight': 'bold', 'size': 16}
    plt.rc('font', **font)  # pass in the font dict as kwargs
    return (colors)


#* Define datasets and theme

user_data = path.abspath(
    input('Enter data directory (of Signal1.csv):') + '/Signal1.csv')
user_data = pd.read_csv(user_data)
file_name = str(user_data).split('/')[-1]
output_dir = path.abspath(input('Enter output directory:') + '/')
 

def plot_chromatogram_data(dataset, figure_name='chromatogram'):
    mpl_plot_settings()
    chromatogram_plot = plt.plot(dataset['Time (mins)'],
                                 dataset['Intensity (mAU)'],
                                 linewidth=2)
    plt.plot(dataset['Time (mins)'], dataset['Intensity (mAU)'], linewidth=2)
    plt.savefig('chromatogram - ' + output_dir + figure_name,
                dpi=300,
                orientation='landscape')


#* Plotting


#* Main sequence
def main():
    plot_chromatogram_data(user_data)


#* Run program
if __name__ == '__main__':
    main()
