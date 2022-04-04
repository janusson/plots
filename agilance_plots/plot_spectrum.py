#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Python 3.9
'''
⌬ Dirty, old example of 2D spectra plotting
'''

from os import path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler
from matplotlib.pyplot import figure
from datetime import datetime

#* Constants and settings
filename = ''

X_RANGE = [0, 5]
Y_RANGE = [0, 100]

START_TIME = datetime.now()
DATA_FILEPATH = path.abspath(f'{filename}.csv')
MSPEC_OUTPUT = './out/{filename}_plot.png'

#* Data import

def csv_to_df(filepath):
    '''
    Import {filepath}.csv file data to plot.

    Args:
        filepath (pathlike): path to .csv file.

    Returns:
        data (pandas.DataFrame): The .csv data as a dataframe
    '''
    data = pd.DataFrame()
    if path.exists(filepath):
        data = pd.read_csv(filepath,
                           sep=',',
                           header=0,
                        #    usecols=['RT', 'mAU', ''], #TODO: add columns
                           dtype=float,
                           engine='c')
    return data


#* Data processing

def peakdata_processing(input_data, MS_RANGE, DT_RANGE, AREA_MIN):
    '''
    Process input data for plot boundaries. 
    Includes scaling, removal of null values, dt conversion from bins to ms, etc.
    This uses the selection rule in DriftScope. 
    See: 'database\Figure 2\SiMo12O40(--)-SelectionRule.rul'

    Args:
        apex_data (pandas.DataFrame): Apex3D output data containing m/z, DT, and area.

    Returns:
        data (pandas.DataFrame): processed m/z, mobility (bins), and peak area data
        formatted for plotting Figure 2.
    '''
    # drop null values, reset index
    proc_data = input_data.dropna()

    # Filter data within plotting range
    proc_data = proc_data[(proc_data['3D_m_z'] > MS_RANGE[0])
                          & (proc_data['3D_m_z'] < MS_RANGE[1]) &
                          (proc_data['3D_Mobility'] > DT_RANGE[0]) &
                          (proc_data['3D_Mobility'] < DT_RANGE[1]) &
                          (proc_data['3D_Intensity'] >
                           AREA_MIN)]  # NOTE: no-negative values
    # add log scale
    proc_data['log(area)'] = proc_data['3D_Intensity'].apply(
        lambda x: np.log(x))
    # convert mobility to millliseconds
    proc_data['mobility (ms)'] = proc_data['3D_Mobility'].apply(lambda x:
                                                                (x * 0.1105))
    # sort all data by m/z for plotting
    proc_data.sort_values('3D_m_z', inplace=True, ascending=True)
    proc_data.reset_index()
    # export workedup csv:
    proc_data.to_csv('./out/figure2_ms_data_processed.csv')
    return proc_data


#* Plotting
def plot_mass_spectrum(apex_data, filename=f'plot_spectrum{START_TIME}'):
    # Style settings
    # plt.style.use('tableau-colorblind10')

    # Custom colours:
    colour_theme = ['#003f5c']
    # colour_theme = ['#003f5c', '#444e86', '#955196', '#dd5182', '#ff6e54', '#ffa600']
    colours = cycler('color', colour_theme)

    # Matplotlib runtime configuration settings (rc params):

    # Background
    plt.rc('axes',
           edgecolor='black',
           axisbelow=False,
           grid=False,
           prop_cycle=colours)
    plt.rc('figure', edgecolor='white')

    # Ticks
    plt.rc('xtick', direction='out', color='black')
    plt.rc('ytick', direction='out', color='black')
    # plt.rc('patch', edgecolor='#003f5c') #?

    # Point size, line size, etc.
    plt.rc('lines', linewidth=1, aa=True)

    # Labels
    font = {
        'family': 'Source Code Pro',  # defaults to Deja Vu Sans
        'weight': 'regular',
        'size': 9
    }
    plt.rc('font', **font)

    # Figure size
    plt.figure(figsize=(10, 5))

    # Labels
    plt.xlabel('$\it{m/z}$')
    plt.ylabel('Signal Area')

    # Gridlines
    plt.grid(True, alpha=0.2)

    # Fill
    # plt.fill_between(apex_data['m_z'], apex_data['area'], y2=0, interpolate=True)

    # Plot
    x_data = apex_data['3D_m_z']
    y_data = apex_data['3D_Intensity']
    plt.stem(x_data, y_data, markerfmt=' ', linefmt='C0-')

    # Axes
    plt.axis([X_RANGE[0], X_RANGE[1], 0, apex_data['3D_Intensity'].max()])

    # Layout
    plt.tight_layout(True)

    # Save figure
    plt.savefig(MSPEC_OUTPUT, dpi=600)
    return None


#* Main sequence
def main(*args):
    fig2_data = csv_to_df(DATA_FILEPATH)  # import csv file
    fig2_processed = peakdata_processing(fig2_data, X_RANGE, Y_RANGE,
                                              AREA_MIN)
    # print('Processed data summary: \n') # check data for debugging
    # print(fig2_processed.info())
    plot_mass_spectrum(fig2_processed)
    print(f'Mass spectrum plot exported to {MSPEC_OUTPUT}')


#* Run program
if __name__ == '__main__':
    main()
