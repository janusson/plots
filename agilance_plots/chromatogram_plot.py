#!/usr/bin/python
# -*- coding: utf-8 -*-
''' ⌬ Description:
Plotting functions for HPLC chromatogram data.
'''

import pandas as pd
import numpy as np
import os
from os import path

#* Constants for testing
TEST_DIR = r'D:\moreslaw\agilance\out\HPLC Chromatogram Output Data'
TEST_FILENAME = r'EJ042-4OHMET(CRM)-6 (1) 2021-06-04 12-13-05.csv'
TEST_SOURCEFILE = os.path.join(TEST_DIR, TEST_FILENAME)

#* Data import
def import_chromatogram(
        filepath):
    '''
    Imports Agilent HPLC chromatogram (.csv) file and returns a dataframe of .
    
    Args:
        filepath (pathlike): path to .csv file
        select_cols (list): columns to import
    
    Returns:
        data (pandas.data_1): Selected data as data_1 object.
    '''
    data = pd.DataFrame()
    if path.exists(filepath):
        data = pd.read_csv(
            filepath,
            sep=',',
            header=0,
            usecols=['Time (min)', 'Intensity (mAU)'],
            # dtype=float, # depends on data type
            engine='c')
    else:
        raise FileNotFoundError('File {filepath} could not be read properly.')
    return data

import_chromatogram(TEST_SOURCEFILE)