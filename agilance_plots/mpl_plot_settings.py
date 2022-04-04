
#* Plotting
def mpl_plot_settings():
    '''
    Custom Delic Labs colour schemes and Matplotlib plot setup.
    '''
    # Delic Labs palette
    delic_labs_palette = ('#00008A', '#FBC700', '#08C1CD', '#60E970',
                          '#0062FF', '#0000CB')

    # MPL Plot Settings
    colors = mpl.cycler(
        'color',
        delic_labs_palette)  #? colors = cycler('color', delic_labs_palette) for rotating through colours
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
