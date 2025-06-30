import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import pandas as pd

# Project palettes and colors
from src.afcharts.assets.af_colours import (
    main,
    sequential,
    sequential_minus,
    diverging,
    af_colour_values,
)

"""
Scope: test using the set color maps in the plotly code and integrate pandas.
This implementation first checks the instance type before plotting (see pandas-matplotlib.py
for a more consistent approach.
ToDo: Enable dynamic colouring so we do not need to specify number of colours 
"""

# A custom color scheme not AF compliant for testing
custom_green_ramp = [
    [0.0, "#D0EACB"],  # Light green
    [0.5, "#76C27A"],  # Mid green
    [1.0, "#2C7744"],  # Dark green
]

custom_green_interval = [
    "#D0EACB",  # Light green
    "#76C27A",  # Mid green
    "#2C7744",  # Dark green
]

def create_colormap_from_stops(stops, name='custom_cmap'):
    """
    Create a continuous colormap from [position, color] stops.

    Args:
        stops (list of [float, str]): List of tuples where each tuple contains
            a float position (0 to 1) and a hex color string.
        name (str): Name of the colormap.

    Returns:
        matplotlib.colors.LinearSegmentedColormap: Continuous colormap.
    """
    positions, colors = zip(*stops)
    return LinearSegmentedColormap.from_list(name, list(zip(positions, colors)))


def sample_colors_from_cmap(cmap, n_colors):
    """
    Sample evenly spaced colors from a continuous colormap.

    Args:
        cmap (matplotlib.colors.Colormap): Continuous colormap to sample from.
        n_colors (int): Number of discrete colors to sample.

    Returns:
        list: List of RGBA color tuples sampled from the colormap.
    """
    return [cmap(i / (n_colors - 1)) for i in range(n_colors)]


def set_matplotlib_defaults(palette=None, n_colors=6):
    """
    Set the default matplotlib color cycle based on the given palette.

    Supports:
        - List of hex color strings (e.g., `main`).
        - List of [position, color] stops for gradients (e.g., `sequential`).

    If a sequential palette is provided, samples `n_colors` evenly spaced colors
    from the continuous gradient.

    Args:
        palette (list, optional): Color palette to set as default. Defaults to `main`.
        n_colors (int, optional): Number of colors to sample from gradients. Defaults to 6.
    """
    if palette is None:
        palette = main

    # Detect if palette is gradient stops, then sample colors
    if isinstance(palette, list) and all(isinstance(c, list) and len(c) == 2 for c in palette):
        cmap = create_colormap_from_stops(palette)
        palette_colors = sample_colors_from_cmap(cmap, n_colors)
    else:
        palette_colors = palette

    # Set matplotlib default color cycle globally
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=palette_colors)


def plot_bar(x, y=None, title="Bar Plot", xlabel=None, ylabel=None):
    """
    Create a bar plot from various data formats.

    Parameters:
    - x: list, dict, or pandas DataFrame
    - y: list or column name (only used if x is list or DataFrame)
    - title: plot title
    - xlabel: label for x-axis
    - ylabel: label for y-axis
    """
    # Dictionary input
    if isinstance(x, dict):
        labels = list(x.keys())
        values = list(x.values())

    # DataFrame input
    elif isinstance(x, pd.DataFrame):
        if isinstance(y, str) and y in x.columns:
            labels = x[x.columns[0]]
            values = x[y]
        else:
            raise ValueError("For DataFrame input, specify a column name for y.")

    # Lists input
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            raise ValueError("Lists x and y must be the same length.")
        labels = x
        values = y

    # other elif stmts go here

    else:
        raise TypeError("Input must be a dict, two lists, or a DataFrame + column name.")

    # Plotting
    plt.bar(labels, values)
    plt.title(title)
    plt.xlabel(xlabel or "Category")
    plt.ylabel(ylabel or "Value")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Examples
# Set default color cycle globally with 5 colors sampled from diverging palette
# n_colors should be dynamic per chart
set_matplotlib_defaults(palette=main, n_colors=5)

# From dictionary
plot_bar({'Apples': 10, 'Bananas': 15, 'Cherries': 7}, title="From Dict")

# From lists
plot_bar(['Apples', 'Bananas', 'Cherries'], [11, 12, 2], title="From Lists")

# From DataFrame
df = pd.DataFrame({
    'Fruit': ['Apples', 'Bananas', 'Cherries'],
    'Count': [1, 5, 12]
})
plot_bar(df, y='Count', title="From DataFrame")
