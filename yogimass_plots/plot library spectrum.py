#
#! under construction - choose a spectrum template
from matplotlib import pyplot as plt

spec_metadata['name']

def plot_library_spectrum(plot_data, spectrum_output='./out/plots/{spectrum_name}', MS_RANGE = [0, 1000]):
    # plot mass spectrum, save to file
    fig = plt.figure(figsize=(4, 3))
    ax = fig.add_subplot(111)
    ax.plot(plot_data['m/z'], plot_data['Normalized Abundance'])
    ax.set_title('Mass Spectrum')

    # Axes labels
    plt.xlabel('$\it{m/z}$')
    plt.ylabel('Normalized Abundance')

    # RC Params: Point size, line size, etc.
    plt.rc('lines', linewidth=1)
    plt.rc('axes', linewidth=1)
    plt.rc('xtick', direction='out', color='black')
    plt.rc('ytick', direction='out', color='black')
    plt.rc('xtick.major', size=4)
    plt.rc('ytick.major', size=4)
    plt.rc('xtick.minor', size=2)
    plt.rc('ytick.minor', size=2)
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.rc('axes', labelsize=8)
    plt.rc('axes', titlesize=8)

    # Gridlines
    plt.grid(True, alpha=0.2)

    # Fill
    # plt.fill_between(apex_data['m_z'], apex_data['area'], y2=0, interpolate=True)

    # Stem Plot
    x_data = plot_data['m/z']
    y_data = plot_data['Normalized Abundance']
    plt.stem(x_data, y_data, markerfmt=' ', linefmt='C0-')

    # Axes
    # plt.axis([MS_RANGE[0], MS_RANGE[1], 0, plot_data[1].max()]) # FIXME 

    # Layout
    plt.tight_layout(True)

    # Save figure
    plt.savefig(spectrum_output, dpi=300)

def main():
    #! under construction - choose a spectrum template
    
#* Run program
if __name__ == '__main__':
    main()
