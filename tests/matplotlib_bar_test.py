"""
Unit tests for the matplotlib bar charts using the af charts package.
"""

import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb


def test_matplotlib_figure_creation():
    """
    Test that a matplotlib bar chart can be created with the afcharts style and the
    figure object is created successfully.
    """
    plt.style.use('afcharts.afcharts')

    categories = ["A", "B", "C"]
    values = [10, 15, 20]

    fig = plt.figure()
    plt.bar(categories, values)

    assert fig is not None

    plt.close(fig)

def test_matplotlib_style_figure_size():
    """
    Test that the afcharts style sets the default figure size to 6.4 x 4.8.
    """
    plt.style.use('afcharts.afcharts')

    fig = plt.figure()

    assert fig.get_figwidth() == 6.4
    assert fig.get_figheight() == 4.8

    plt.close(fig)

def test_matplotlib_style_y_gridlines_visible():
    """
    Test that the afcharts style enables y-axis gridlines.
    """
    plt.style.use('afcharts.afcharts')

    fig, ax = plt.subplots()

    # Force the gridlines to be drawn to check their visibility
    fig.canvas.draw()

    y_gridlines = ax.get_ygridlines()
    assert any(line.get_visible() for line in y_gridlines)

    plt.close(fig)

def test_matplotlib_default_colour_applied():
    """
    Test that a bar chart uses the first AF colour (dark blue) from the style.
    """
    plt.style.use('afcharts.afcharts')

    fig, ax = plt.subplots()
    ax.bar(["Stuff"], [10])

    bar_patches = ax.patches
    bar_colour = bar_patches[0].get_facecolor()[:3]

    expected_colour = to_rgb("#12436D")

    assert bar_colour == expected_colour

    plt.close(fig)
