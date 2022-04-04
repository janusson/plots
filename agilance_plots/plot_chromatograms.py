# plot all .csv HPLC chromatogram data found in a folder
import pandas as pd
from glob import glob
import os
from matplotlib import pyplot as plt
import seaborn as sns

#* Import all .csv files in directory.
chromatograms_dir = r'C:\Users\Eric\Complex Biotech Discovery Ventures Ltd\Analytical Methods - Documents\Projects\GFYPSY\HPLC Chromatograms'
csv_list = glob(chromatograms_dir + '\*.csv')
OUTPUT_DIRECTORY = r'C:\Users\Eric\Complex Biotech Discovery Ventures Ltd\Analytical Methods - Documents\Projects\GFYPSY\HPLC Chromatograms\out'
if not os.path.exists(OUTPUT_DIRECTORY):
    os.mkdir(OUTPUT_DIRECTORY)
else:
    pass

def save_chromatogram(csv_file):
    sample_name = csv_file.split('\\')[-1].split('.')[0]
    chromatogram = pd.read_csv(csv_file, header=0, usecols=['Time (mins)', 'Intensity (mAU)'])
    x = sns.lineplot(x='Time (mins)', y='Intensity (mAU)', data=chromatogram, label=sample_name)
    # x.set_title(sample_name)
    save_dir = OUTPUT_DIRECTORY + '\\' + sample_name + '.png'
    plt.savefig(save_dir, dpi = 300)
    print(f'Chromatogram for {sample_name} saved to {save_dir}')
    return plt.close()

#? arbitrary testing file and name for plotting, loop in main
# hplc_signal_file = csv_list[8]
# chromatogram = pd.read_csv(hplc_signal_file, header=0, usecols=['Time (mins)', 'Intensity (mAU)'])
# sample_name = hplc_signal_file.split('\\')[-1].split('.')[0]
# plot1 = sns.lineplot(x='Time (mins)', y='Intensity (mAU)', data=chromatogram, label=sample_name)
# plt.savefig('test.png', dpi=300)

for chromatogram in csv_list:
    save_chromatogram(chromatogram)