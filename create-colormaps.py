"""
Export colormaps from Python / matplotlib to JavaScript.
"""

# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------

import json

from matplotlib.colors import Colormap

import matplotlib.cm as cm
import matplotlib.colors as colors
import numpy as np


# -----------------------------------------------------------------------------
# MAIN CODE
# -----------------------------------------------------------------------------

if __name__ == "__main__":

    # Loop over all matplotlib colormaps and store them in a dictionary. This
    # dictionary contains the colors of the colormap as list of lists (= RGB
    # tuples), and whether or not the colormap should be interpolated (= false
    # for qualitative colormaps).
    colormaps = {}
    for name in dir(cm):

        # Skip reversed colormaps (they don't contain additional information)
        if name.endswith("_r"):
            continue

        # If `cmap` is a colormap, we can store the association information
        if isinstance(cmap := getattr(cm, name), Colormap):

            # Evaluate colormap on the grid to get colors, drop alpha channel
            # information, and round to a reasonable precision
            colors = np.around(cmap(np.linspace(0, 1, cmap.N))[:, 0:3], 4)

            # Store relevant colormap information
            colormaps[cmap.name] = {
                "interpolate": cmap.N >= 256,
                "colors": colors.tolist(),
            }

    # Save colormap data and shortcuts to data.js. The contents of this file
    # need to be copied manually to js-colormaps.js.
    with open("data.js", "w") as json_file:

        # Write the data dictionary to data.js
        json_file.write(f"const data = {json.dumps(colormaps)};")
        json_file.write('\n\n')

        # Write partial function applications to data.js so that we can use
        # a colormap by its name --- e.g., call viridis(0.5) to evaluate the
        # viridis colormap at a value of 0.5.
        for name in colormaps.keys():
            json_file.write(f"const {name} = partial('{name}');\n")
            json_file.write(f"const {name}_r = partial('{name}_r');\n")

    # Final words
    print("\nExported data to data.js, please copy to js-colormaps.js!\n")
