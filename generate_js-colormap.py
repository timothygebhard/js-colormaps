from matplotlib import cm
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np



# -----------------------------------------------------------------------------
# FUNCTION DEFINITIONS
# -----------------------------------------------------------------------------

def enforce_bounds(x):
    if x < 0:
        return 0
    elif x > 1:
        return 1
    else:
        return x


def cm_values_to_js(values, cm_name):
    """
    Take an array of values of the form (x, (r, g, b)), and return the
    corresponding JavaScript variable with the correct name.
    """

    dummy = ['[{x:.3f}, [{r:.3f}, {g:.3f}, {b:.3f}]]'.format(x=value[0],
                                                             r=value[1][0],
                                                             g=value[1][1],
                                                             b=value[1][2])
             for value in values]
    cm_values = ', '.join(dummy)

    return 'var {cm_name} = [{cm_values}];'.format(cm_name=cm_name, 
                                                   cm_values=cm_values)

def get_cm_values(colormap, n_shades=256):
    """
    Takes the name of an inbuilt colormap and the number of shades, and returns
    an array whose elements whave the form (x, (r, g, b)), for n_shades values
    of x between 0 and 1.
    """
    values = []
    for i in np.linspace(0, 1, n_shades):
        r, g, b, alpha = colormap(i)
        values.append((i, (r, g, b)))
    return values


def interpolate_linearly(x, values):
    """
    Takes a point x in [0, 1], and an array of color values, whose elements
    have the form (x', (r, g, b)), with x', r, g, b all in [0, 1].
    If there is an element in values so that x==x', it will return the
    corresponding RGB-value. Otherwise it will interpolate linearly between
    x' and x'', where x' < x < x''.
    """

    # Split values into four lists
    x_values = [_[0] for _ in values]
    r_values = [_[1][0] for _ in values]
    g_values = [_[1][1] for _ in values]
    b_values = [_[1][2] for _ in values]

    # If we are requesting the color for a value that happens to be in the
    # values list, we do not need to interpolate anything
    if x in x_values:
        i = x_values.index(x)
        return (r_values[i], r_values[i], r_values[i])

    # Otherwise things get more complicated:
    else:

        # Find the largest index i such that x_values[i] < x
        # We will interpolate between x_values[i] and x_values[i+1]
        i = 0
        while x_values[i] < x:
            i+= 1
        i -= 1

        # The scaling factor that we need for the interpolation
        width = np.abs(x_values[i] - x_values[i+1])
        scaling_factor = (x - x_values[i])/width

        # Get the new color values though interpolation
        r = r_values[i] + scaling_factor * (r_values[i+1] - r_values[i])
        g = g_values[i] + scaling_factor * (g_values[i+1] - g_values[i])
        b = b_values[i] + scaling_factor * (b_values[i+1] - b_values[i])
        
        return (enforce_bounds(r), enforce_bounds(g), enforce_bounds(b))


def plot_cm_comparison(colormap, values):
    """
    Takes the name of a colormap and an array of values for that colormap.
    It then plots the original colormap, and an interpolated one using the
    values-array. This can be used to check how long values needs to be for
    a reasonable approximation of the original colormap.
    """

    # Split the canvas in two subplots and set up plot options
    fig, axarr = plt.subplots(2, sharex=True)
    plt.subplots_adjust(hspace = .001)
    axarr[0].set_title('Linear Interpolation from {} given shades'
                       .format(len(values)))
    axarr[0].set_yticklabels(())
    axarr[1].set_yticklabels(())
    axarr[0].set_ylabel('Original Colormap')
    axarr[1].set_ylabel('Interpolated Colormap')

    #
    # Plot the original colormap
    # -------------------------------------------------------------------------
    
    # First, set up a grid and calculate the grid width
    grid = np.linspace(0, 1, 1024)
    width = grid[1] - grid[0]
    
    for i, x in enumerate(grid):
        color = colormap(x)
        patch = patches.Rectangle((i*width, 0), width, 1, facecolor=color,
                                   edgecolor='none')
        axarr[0].add_patch(patch)

    #
    # Plot the interpolated colormap
    # -------------------------------------------------------------------------
    for i, x in enumerate(grid):
        color = interpolate_linearly(x, values)
        patch = patches.Rectangle((i*width, 0), width, 1, facecolor=color,
                                   edgecolor='none')
        axarr[1].add_patch(patch)


# -----------------------------------------------------------------------------
# INBUILT MATPLOTLIB COLORMAPS
# -----------------------------------------------------------------------------

cmaps = {'Sequential':     ['Blues', 'BuGn', 'BuPu',
                             'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd',
                             'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu',
                             'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd'],
         'Sequential (2)': ['afmhot', 'autumn', 'bone', 'cool', 'copper',
                             'gist_heat', 'gray', 'hot', 'pink',
                             'spring', 'summer', 'winter'],
         'Diverging':      ['BrBG', 'bwr', 'coolwarm', 'PiYG', 'PRGn', 'PuOr',
                             'RdBu', 'RdGy', 'RdYlBu', 'RdYlGn', 'Spectral',
                             'seismic'],
         'Qualitative':    ['Accent', 'Dark2', 'Paired', 'Pastel1',
                             'Pastel2', 'Set1', 'Set2', 'Set3'],
         'Miscellaneous':  ['gist_earth', 'terrain', 'ocean', 'gist_stern',
                             'brg', 'CMRmap', 'cubehelix',
                             'gnuplot', 'gnuplot2', 'gist_ncar',
                             'nipy_spectral', 'jet', 'rainbow',
                             'gist_rainbow', 'hsv', 'flag', 'prism']}


# -----------------------------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------------------------

# Loop over all colormaps and generate the corresponding JavaScript variable
for cm_type in cmaps.keys():

    print '// {}'.format(cm_type)
    for cmap in sorted(cmaps[cm_type]):
        values = get_cm_values(cm.get_cmap(cmap), n_shades=512)
        print cm_values_to_js(values, cmap)
    print
