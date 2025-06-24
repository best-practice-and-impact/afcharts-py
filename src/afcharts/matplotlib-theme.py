import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Project palettes and colors
from src.afcharts.assets.af_colours import (
    main,
    sequential,
    sequential_minus,
    diverging,
    af_colour_values,
)

"""
Scope: test using the set color maps in the plotly code 
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


def plot_dummy_bar_chart():
    """
    Plot a dummy bar chart using the current matplotlib color cycle.

    colors are taken from the current default matplotlib color cycle.
    """
    categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
    values = [42, 55, 36, 60, 45]

    # Get current matplotlib color cycle
    prop_cycle = plt.rcParams['axes.prop_cycle']
    colors = prop_cycle.by_key()['color']

    # Repeat colors if fewer than bars
    colors = (colors * (len(categories) // len(colors) + 1))[:len(categories)]

    fig, ax = plt.subplots()
    ax.bar(categories, values, color=colors)

    ax.set_title("Dummy Bar Chart")
    ax.set_ylabel("Value")
    ax.set_xlabel("Category")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.show()


# Set default color cycle globally with 5 colors sampled from diverging palette
# n_colors should be dynamic per chart
set_matplotlib_defaults(palette=custom_green_interval, n_colors=5)

# Plot dummy bar chart colored by the default color cycle
plot_dummy_bar_chart()
