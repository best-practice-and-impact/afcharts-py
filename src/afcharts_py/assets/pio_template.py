import plotly.graph_objects as go
import plotly.io as pio
from afcharts_py.assets.af_colours import (
    main,
    sequential,
    sequential_minus,
    diverging,
    af_colour_values,
)

afcharts_font = "Sans-serif"  # consider using a different font?
base_size = 14

# The half-line (base_size / 2) sets up the basic vertical
# rhythm of the theme. Most margins will be set to this value.
# However, when we work with relative sizes, we may want to multiply
# `half_line` with the appropriate relative size. This applies in
# particular for axis tick sizes. And also, for axis ticks and
# axis titles, `half_size` is too large a distance, and we use `half_size/2`
# instead.
half_line = base_size / 2

pio.templates["af_pio"] = go.layout.Template(
    layout={
        "autosize": True,  # Automatically adjusts the scale of the plot based on it's content
        "annotationdefaults": {
            "font": {"size": base_size}
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
        "colorway": main,  # Sequence of colours to be used in plots
        "font": {
            "color": "black",  # Text colour
            "family": afcharts_font,  # Font
            "size": base_size,
        },  # Text size
        "legend_title": None,  # Removes legend title
        "legend": {
            "borderwidth": 0,
            # "entrywidth": 0,
            # "entrywidthmode": "pixels",
            "title": {"text": None},  # Removes legend title
            "font": {
                "size": base_size * 1.2,
            },  # Legend font size
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
            "font_size": base_size,  # Text size of hover
            "bgcolor": "white",  # Hover box background
        },
        "hovermode": "x unified",  # How hovering affects the display - x unified shows info for all the data at that point in the x-axis
        "paper_bgcolor": "rgba(0,0,0,0)",  # Makes paper (entire area) background transparent
        "plot_bgcolor": "rgba(0,0,0,0)",  # Makes plot area transparent
        "margin": {  # Set margins around the plot area in pixels
            "l": half_line,  # Left margin
            "r": half_line,  # Right margin
            "t": half_line,  # Top margin
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
            "yref": "paper",
        },
        "xaxis": {  # Configures the x-axis
            "automargin": True,  # Automatically adjust margins on axes to fit the content
            "gridcolor": af_colour_values["chart_features"],  # Grid lines colours
            "linecolor": af_colour_values["chart_features"],  # Axes line colour
            "linewidth": 1,
            "showgrid": False,  # Hide grid lines
            "tickcolor": af_colour_values["chart_features"],  # Tick mark colours
            "tickfont": {
                "size": base_size,
            },  # Tick label font size
            "tickwidth": 1,
            "ticks": "outside",  # Removes tick marks
            "title": {  # Axes title
                "text": None,  # Removes axes title
                "font": {
                    "size": base_size * 1.4,
                },  # Axes title size
                "standoff": 10,  # Position from axes
            },
            "fixedrange": True,  # Disables zoom and pan, keeps range fixed
            "showline": False,  # Line which marks the boundary of the plotting area
            "zeroline": True,  # Makes zeroline visible
            "zerolinecolor": af_colour_values["chart_features"],  # Zero line colour
        },
        "yaxis": {  # Configures the y-axis (as with the x-axis above)
            "automargin": True,
            "gridcolor": af_colour_values["chart_features"],
            "linecolor": af_colour_values["chart_features"],
            "linewidth": 1,
            "showgrid": False,
            "tickcolor": af_colour_values["chart_features"],
            "tickfont": {"size": base_size},
            "tickwidth": 1,
            "ticks": "outside",
            "title": {
                "text": None,
                "font": {"size": base_size * 1.4},
                "standoff": 10,  # Position from axes
            },
            "fixedrange": True,
            "showline": False,
            "zeroline": True,
            "zerolinecolor": af_colour_values["chart_features"],
        },
    }
)

# DEFRA - Template to be used for dashboards, where visualisations do not contain accompanying text, such as titles and sources:
pio.templates.default = "af_pio"
