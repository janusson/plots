# plot all .csv HPLC chromatogram data found in a folder
import pandas as pd
from glob import glob
import os
from matplotlib import pyplot as plt
import seaborn as sns

chromatograms_dir = os.path.abspath(r'.\out\HPLC Chromatograms')
csv_list = glob(chromatograms_dir + '\*.csv')
OUTPUT_DIRECTORY = os.path.abspath(r'.\out\HPLC chromatogram plots')
if not os.path.exists(OUTPUT_DIRECTORY):
    os.mkdir(OUTPUT_DIRECTORY)
else:
    pass

def save_chromatogram(csv_file):
    sample_name = csv_file.split('\\')[-1].split('.')[0]
    chromatogram = pd.read_csv(csv_file, header=0, usecols=['Time (mins)', 'Intensity (mAU)'])
    plot1 = sns.lineplot(x='Time (mins)', y='Intensity (mAU)', data=chromatogram, label=sample_name)
    plot1.set_title(sample_name)
    plot1.set_xlabel('Time (mins)')
    plot1.set_ylabel('Intensity (mAU)')
    save_dir = OUTPUT_DIRECTORY + '\\' + sample_name + '.png'
    plt.savefig(save_dir, dpi = 300)
    print(f'Chromatogram for {sample_name} saved to {save_dir}')
    return plt.close()

for chromatogram in csv_list:
    save_chromatogram(chromatogram)