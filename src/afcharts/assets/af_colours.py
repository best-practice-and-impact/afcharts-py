# For testing taken from 
# Government Analysis Function (AF) colours and palettes
# Source: https://analysisfunction.civilservice.gov.uk/policy-store/
#   data-visualisation-colours-in-charts/
#

af_colour_values = {
    # CORE COLOURS
    "black": "#000000",
    "white": "#FFFFFF",
    "rag_green": "#8ED973",
    "rag_amber": "#FFC000",
    "rag_red": "#C00000",
    "chart_features": "#D9D9D9",
    "chart_axes_and_labels": "#595959",
    "dark_blue": "#12436D",  # Categorical colour 1 and sequential #1
    "turquoise": "#28A197",  # Categorical colour 2
    "dark_pink": "#801650",  # Categorical colour 3
    "orange": "#F46A25",  # Categorical colour 4
    "dark_grey": "#3D3D3D",  # Categorical colour 5
    "light_purple": "#A285D1",  # Categorical colour 6
    "mid_blue": "#2073BC",  # Sequential colour mid
    "light_blue": "#6BACE6",  # Sequential colour #3
    "grey": "#BFBFBF",
}

main = [
    af_colour_values["dark_blue"],  # Dark blue
    af_colour_values["turquoise"],  # Turquoise
    af_colour_values["dark_pink"],  # Dark pink
    af_colour_values["orange"],  # Orange
    af_colour_values["dark_grey"],  # Dark grey
    af_colour_values["light_purple"],  # Light purple
]

duo = [
    af_colour_values["dark_blue"],  # Dark blue
    af_colour_values["orange"],  # Orange
]

# Sequential palette
sequential = [
    [0, af_colour_values["dark_blue"]],  # Lightest blue
    [0.5, af_colour_values["mid_blue"]],  # Lightest blue
    [1, af_colour_values["light_blue"]],  # Darkest blue
]

sequential_minus = list(reversed(sequential))


# DU diverging palette [style guide analytical palette 4]
diverging = [
    [0, af_colour_values["dark_pink"]],  # Dark pink
    [0.5, af_colour_values["orange"]],  # Orange
    [1, af_colour_values["dark_blue"]],  # Dark blue
]


rag = {
    "Green": af_colour_values["rag_green"],  # RAG green
    "Amber": af_colour_values["rag_amber"],  # RAG Amber (for 3 point scale)
    "Red": af_colour_values["rag_red"],  # RAG red
}

# Font colors for hicontrast with rag colors
rag_font_colors = {
    "Green": af_colour_values["black"],  # text color
    "Amber": af_colour_values["black"],  # text color
    "Red": af_colour_values["white"],  # White
}