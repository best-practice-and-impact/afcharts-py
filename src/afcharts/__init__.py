import matplotlib.pyplot as plt
import os

def register_mpl_styles():
    """Automatically register afcharts style with matplotlib on import"""
    style_dir = os.path.join(os.path.dirname(__file__), 'stylelib')

    for style_file in os.listdir(style_dir):
        if style_file.endswith('.mplstyle'):
            style_name = style_file[:-9]
            style_path = os.path.join(style_dir, style_file)

        # If unregistered, register style
        if style_name not in plt.style.library:
            plt.style.library[style_name] = style_path

# run on import
register_mpl_styles()
