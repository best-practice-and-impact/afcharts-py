import plotly.graph_objects as go
import plotly.io as pio
from typing import Literal

# Project
from afcharts_py.assets.af_colours import (
    main,
    sequential,
    sequential_minus,
    diverging,
    af_colour_values,
)


def theme_af(
    base_size: int = 14,
    base_line_size: float = None,
    base_rect_size: float = None,
    colour_palette: list = None,
    grid: Literal["x", "y", "xy", None] = None,
    axis: Literal["x", "y", "xy", None] = None,
    ticks: Literal["x", "y", "xy", None] = None,
    legend: Literal["right", "left", "top", "bottom", None] = None,
):
    """
    Analysis Function theme for Plotly charts.

    This function defines a consistent visual theme for charts, inspired by
    ggplot2 styling conventions used in Analysis Function plots.

    Parameters
    ----------
    base_size : float, optional
        Base font size in points. Default is 12.
    base_line_size : float, optional
        Base size for line elements. Default is 0.5.
    base_rect_size : float, optional
        Base size for rectangle elements. Default is 0.5.
    grid : {'x', 'y', 'xy', 'none'}, optional
        Determines which grid lines are shown. Default is 'y'.
    axis : {'x', 'y', 'xy', 'none'}, optional
        Determines which axis lines are shown. Default is 'x'.
    ticks : {'x', 'y', 'xy', 'none'}, optional
        Determines which axis ticks are shown. Default is 'xy'.
    legend : {'right', 'left', 'top', 'bottom', 'none'}, optional
        Position of the legend. Default is 'right'.

    Returns
    -------
    dict
        A dictionary representing the theme configuration for use in a charting library.

    Examples
    --------
    >>> import plotly.graph_objects as go
    >>> fig = go.Figure()
    >>> fig.update_layout(theme=theme_af())
    >>> fig.show()
    """

    if colour_palette:
        colorway = colour_palette
    else:
        colorway = main

    if base_line_size is None:
        base_line_size = base_size / 24
    if base_rect_size is None:
        base_rect_size = base_size / 24

    afcharts_font = "Sans-serif"  # consider using a different font?

    # The half-line (base_size / 2) sets up the basic vertical
    # rhythm of the theme. Most margins will be set to this value.
    # However, when we work with relative sizes, we may want to multiply
    # `half_line` with the appropriate relative size. This applies in
    # particular for axis tick sizes. And also, for axis ticks and
    # axis titles, `half_size` is too large a distance, and we use `half_size/2`
    # instead.
    half_line = base_size / 2

    # Set grid lines dependent on grid arg
    grid_x = grid in ("x", "xy")
    grid_y = grid in ("y", "xy")

    # Set axis lines dependent on axis arg
    axis_x = axis in ("x", "xy")
    axis_y = axis in ("y", "xy")

    # Set axis ticks dependent on ticks arg
    ticks_x = ticks in ("x", "xy")
    ticks_y = ticks in ("y", "xy")

    return go.layout.Template(
        layout={
            "autosize": True,  # Automatically adjusts the scale of the plot based on it's content
            "annotationdefaults": {
                "font": {"size": base_size},
                "showarrow": False,
            },  # Sets default font size for annotation
            "bargap": 0.15,
            "bargroupgap": 0.1,
            "plot_bgcolor": "white",
            "coloraxis": {
                "colorbar": {  # Bar chart colours
                    "outlinewidth": 0,  # Width of the outline around the color bar
                    "tickcolor": af_colour_values[
                        "chart_features"
                    ],  # Bar chart tick colour
                    "ticklen": 6,  # Bar chart tick length
                    "ticks": "outside",  # Bar chart tick position
                }
            },
            "colorscale": {
                "sequential": sequential,  # Sequential colour scale for low to high ranges
                "sequentialminus": sequential_minus,  # Sequential palette for negatives
                "diverging": diverging,  # Diverging colour scale
            },
            "colorway": colorway,  # Sequence of colours to be used in plots
            "font": {
                "color": "black",  # Text colour
                "family": afcharts_font,  # Font
                "size": base_size,
            },  # Text size
            "legend_title": None,  # Removes legend title
            "legend": {
                "borderwidth": 0,
                "title": {"text": None},  # Removes legend title
                "font": {"size": base_size * 1.2},  # Legend font size
                "bgcolor": "rgba(0,0,0,0)",  # Makes legend background transparent
                "orientation": "v",  # Legend orientation
                "x": 1,  # Positions legend (0,0 is the bottom left)
                "y": 0.5,
                "indentation": 0,
                "itemclick": "toggleothers",  # Change behaviour from hiding trace to showing only this trace
                "itemwidth": 30,
                # "itemsizing": "constant",
                "traceorder": "normal",
            },
            "hoverlabel": {
                "align": "left",  # Align hover label text to the left
                "font_size": base_size * 0.9,  # Text size of hover
                "bgcolor": "white",  # Hover box background
            },
            "hovermode": "x unified",  # How hovering affects the display - x unified shows info for all the data at that point in the x-axis
            "paper_bgcolor": "rgba(0,0,0,0)",  # Makes paper (entire area) background transparent
            "plot_bgcolor": "rgba(0,0,0,0)",  # Makes plot area transparent
            "margin": {  # Set margins around the plot area in pixels
                "l": half_line,  # Left margin
                "r": half_line,  # Right margin
                "t": (base_size * 1.6)
                + (0.7 * (base_size * 1.6))
                + half_line
                + base_size,  # Top margin is the size of the title + subtitle size + title_padding + space between title and subtitle (which is set by default)
                "b": half_line,  # Bottom margin
                "pad": 0,  # Padding between grid lines and the tick labels
            },
            "paper_bgcolor": "white",
            "uniformtext_minsize": 8,  # Minimum font size for text elements in the plot
            "uniformtext_mode": "hide",  # Controls visibility of text based on size - hide means that if a text element's size falls below the "uniformtext_minsize" then the text will be hidden
            "title": {
                "text": None,
                "font": {
                    "size": base_size * 1.6,
                },  # Title font size and colour
                "pad": {
                    "t": half_line,
                    "l": half_line,
                    "r": half_line,
                    "b": half_line,
                },  # Padding above and below title
                "x": 0,  # Title position horizonatally
                "xanchor": "left",
                "xref": "paper",
                "y": 1,  # Title position vertically (1 = top of plot)
                "yanchor": "top",
                "yref": "container",
            },
            "xaxis": {  # Configures the x-axis
                "automargin": True,  # Automatically adjust margins on axes to fit the content
                "gridcolor": af_colour_values["chart_features"],  # Grid lines colours
                "linecolor": af_colour_values["chart_features"],  # Axes line colour
                "linewidth": 1,
                "showgrid": grid_x,  # Hide grid lines
                "tickcolor": af_colour_values["chart_features"],  # Tick mark colours
                # "tickfont": {
                #     "size": base_size,
                # },  # Tick label font size
                "tickwidth": 1,
                "ticks": "outside",  # Removes tick marks
                "title": {  # Axes title
                    "text": None,  # Removes axes title
                    # "font": {
                    #     "size": base_size * 1.4,
                    # },  # Axes title size
                    "standoff": half_line / 2,  # Position from axes
                },
                "fixedrange": True,  # Disables zoom and pan, keeps range fixed
                "showline": axis_x,  # Line which marks the boundary of the plotting area
                "zeroline": True,  # Makes zeroline visible
                "zerolinecolor": af_colour_values["chart_features"],  # Zero line colour
            },
            "yaxis": {  # Configures the y-axis (as with the x-axis above)
                "automargin": True,
                "gridcolor": af_colour_values["chart_features"],
                "linecolor": af_colour_values["chart_features"],
                "linewidth": 1,
                "showgrid": grid_y,
                "tickcolor": af_colour_values["chart_features"],
                # "tickfont": {"size": base_size},
                "tickwidth": 1,
                "ticks": "outside",
                "title": {
                    "text": None,
                    # "font": {"size": base_size * 1.4},
                    "standoff": half_line / 2,  # Position from axes
                },
                "fixedrange": True,
                "showline": axis_y,
                "zeroline": True,
                "zerolinecolor": af_colour_values["chart_features"],
            },
        }
    )
