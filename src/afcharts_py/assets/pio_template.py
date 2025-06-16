import plotly.graph_objects as go
import plotly.io as pio
from afcharts_py.assets.af_colours import (
    main,
    sequential,
    sequential_minus,
    diverging,
    af_colour_values,
)

af_font = "Sans-serif"  # consider using a different font?

pio.templates["af_pio"] = go.layout.Template(
    layout={
        "autosize": True,  # Automatically adjusts the scale of the plot based on it's content
        "annotationdefaults": {
            "font": {"size": 10, "family": af_font}
        },  # Sets default font size for annotation
        "bargap": 0.15,
        "bargroupgap": 0.1,
        "coloraxis": {
            "colorbar": {  # Bar chart colours
                "outlinewidth": 0,  # Width of the outline around the color bar
                "tickcolor": af_colour_values[
                    "chart_axes_and_labels"
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
        "colorway": main,  # Sequence of colours to be used in plots
        "font": {
            "color": af_colour_values["chart_axes_and_labels"],  # Text colour
            "family": af_font,  # Font
            "size": 10,
        },  # Text size
        "legend_title": None,  # Removes legend title
        "legend": {
            "borderwidth": 0,
            # "entrywidth": 0,
            # "entrywidthmode": "pixels",
            "title": {"text": None},  # Removes legend title
            "font": {"size": 8, "family": af_font},  # Legend font size
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
            "font_family": af_font,  # Font of hover
            "font_size": 9,  # Text size of hover
            "bgcolor": "white",  # Hover box background
        },
        "hovermode": "x unified",  # How hovering affects the display - x unified shows info for all the data at that point in the x-axis
        "paper_bgcolor": "rgba(0,0,0,0)",  # Makes paper (entire area) background transparent
        "plot_bgcolor": "rgba(0,0,0,0)",  # Makes plot area transparent
        "margin": {  # Set margins around the plot area in pixels
            "l": 0,  # Left margin
            "r": 0,  # Right margin
            "t": 20,  # Top margin
            "b": 5,  # Bottom margin
            "pad": 0,  # Padding between grid lines and the tick labels
        },
        "uniformtext_minsize": 8,  # Minimum font size for text elements in the plot
        "uniformtext_mode": "hide",  # Controls visibility of text based on size - hide means that if a text element's size falls below the "uniformtext_minsize" then the text will be hidden
        "title": {
            "text": None,
            "font": {
                "family": af_font,
                "size": 14,
                "color": af_colour_values["chart_axes_and_labels"],
            },  # Title font size and colour
            "pad": {"t": 10, "b": 10},  # Padding above and below title
            "x": 0,  # Title position horizonatally
            "y": 1,  # Title position vertically (1 = top of plot)
        },
        "xaxis": {  # Configures the x-axis
            "automargin": True,  # Automatically adjust margins on axes to fit the content
            "gridcolor": af_colour_values["chart_grids"],  # Grid lines colours
            "linecolor": af_colour_values["chart_axes_and_labels"],  # Axes line colour
            "showgrid": False,  # Hide grid lines
            "tickcolor": af_colour_values["chart_axes_and_labels"],  # Tick mark colours
            "tickfont": {"size": 10, "family": af_font},  # Tick label font size
            "ticks": "outside",  # Removes tick marks
            "title": {  # Axes title
                "text": None,  # Removes axes title
                "font": {"size": 12, "family": af_font},  # Axes title size
                "standoff": 10,  # Position from axes
            },
            "fixedrange": True,  # Disables zoom and pan, keeps range fixed
            "showline": False,  # Line which marks the boundary of the plotting area
            "zeroline": True,  # Makes zeroline visible
            "zerolinecolor": af_colour_values[
                "chart_axes_and_labels"
            ],  # Zero line colour
        },
        "yaxis": {  # Configures the y-axis (as with the x-axis above)
            "automargin": True,
            "gridcolor": af_colour_values["chart_grids"],
            "linecolor": af_colour_values["chart_axes_and_labels"],
            "showgrid": False,
            "tickcolor": af_colour_values["chart_axes_and_labels"],
            "tickfont": {"size": 10},
            "ticks": "outside",
            "title": {
                "text": None,
                "font": {"size": 12, "family": af_font},
                "standoff": 10,  # Position from axes
            },
            "fixedrange": True,
            "showline": False,
            "zeroline": True,
            "zerolinecolor": af_colour_values["chart_axes_and_labels"],
        },
    }
)

# DEFRA - Template to be used for dashboards, where visualisations do not contain accompanying text, such as titles and sources:
pio.templates.default = "af_pio"
