#!/usr/bin/python
# -*- coding: utf-8 -*-
#   ⌬ Eric Janusson
#   Python 3.9
'''
Description:
GCMS data extraction.
GCMS peak data are exported as csv files via MassHunter Qualitative Analysis 10.0.
Notes: See experiments EJ021, EJ022.
'''
from os import path
import pandas as pd

#* Constants and settings
filename = ''
DATA_FILEPATH = path.abspath('database\EJ022 - Terpene Calibration Data')
AREA_MIN = 0 # filter out negative values
OUTPUT = f'./out/GCMS Chromatogram {filename}.png'

#* Data import

""" for path in report_paths:
    split = path.split(' ')[0]
    txtfiles = glob(DATA_DIR + '*.TXT') """

def import_data(filepath):
    '''
    Import file for plotting.

    Args:
        filepath (pathlike): path to Apex3D peaks csv file.

    Returns:
        data (pandas.DataFrame): m/z, mobility (bins), and peak area data
    '''
    if path.exists(filepath):
        data = pd.read_csv(DATA_FILEPATH,
                     sep=',',
                     header=0,
                     usecols=['m_z', 'mobility', 'area'], # FIXME
                     dtype=float,
                     engine='c')

    return data
