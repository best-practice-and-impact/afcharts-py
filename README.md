
# afcharts-py <img src="docs/images/logo.svg" alt="afcharts logo" align="right" height="150"/>

## Overview

The afcharts python package helps make accessible Matplotlib and Plotly charts following [Government Analysis Function Data Visualisation guidance](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/):

- **Automatic chart formatting** with pre-built style sheets for Matplotlib and Plotly
- **Chart colours** from the Analysis Function [accessible colour palettes](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-colours-in-charts/#section-4)
- **Example code** for common chart types in the [cookbook](https://best-practice-and-impact.github.io/afcharts-py/)

Looking for the R version? Check out the [afcharts R package](https://best-practice-and-impact.github.io/afcharts/).

<img src="docs/images/example_charts/bar_chart-matplotlib_afcharts.png" width="28.1%" alt="A grouped bar chart in afcharts style showing life expectancy in 1967 and 2007 for four countries. Bars use Analysis Function palette: dark blue for 1967, orange for 2007."/> <img src="docs/images/example_charts/scatterplot-matplotlib_afcharts.png" width="30%" alt="A scatterplot in afcharts style showing life expectancy against GDP per capita for 142 countries in 2007."/> <img src="docs/images/example_charts/line_chart-matplotlib_afcharts.png" width="37.5%" alt="A line chart in afcharts style showing life expectancy in China and the UK from 1952 to 2007"/>

## Installation

afcharts is available at the Python Package Index (PyPI):
```bash
pip install afcharts
```
or see the [alternative installation](https://best-practice-and-impact.github.io/afcharts-py/getting-started.html) instructions.

## Usage

Format any Matplotlib or Plotly chart in the Analysis Function style using the built-in style sheets.

See the [Getting Started](https://best-practice-and-impact.github.io/afcharts-py/getting-started.html) guide for more options and the [cookbook](https://best-practice-and-impact.github.io/afcharts-py/) for extensive examples.

### Matplotlib

```python
import matplotlib.pyplot as plt

# Apply the afcharts style to all Matplotlib plots
plt.style.use('afcharts.afcharts')
```

Example: A [Matplotlib bar chart](https://best-practice-and-impact.github.io/afcharts-py/01-matplotlib-usage.html#grouped-bar-chart) with afcharts (left) and without (right)

<img src="docs/images/example_charts/bar_chart-matplotlib_afcharts.png" width="35%" alt="Grouped bar chart (afcharts style) showing life expectancy in 1967 and 2007 for four countries. Bars use Analysis Function palette: dark blue for 1967, orange for 2007."/> <img src="docs/images/example_charts/bar_chart-matplotlib_default.png" width="34.7%" alt="Grouped bar chart (default Matplotlib) showing life expectancy in 1967 and 2007 for four countries. Bars: blue for 1967, orange for 2007."/>

### Plotly

```python
from afcharts.pio_template import pio

# Apply the afcharts style to all Plotly plots
pio.templates.default = "theme_af"
```

Example: A [Plotly bar chart](https://best-practice-and-impact.github.io/afcharts-py/03-plotly-usage.html#grouped-bar-chart) with afcharts (left) and without (right)

<img src="docs/images/example_charts/bar_chart-plotly_afcharts.png" width="35%" alt="Grouped bar chart (afcharts style) showing life expectancy in 1967 and 2007 for four countries. Bars use Analysis Function palette: dark blue for 1967, orange for 2007."/> <img src="docs/images/example_charts/bar_chart-plotly_default.png" width="35%" alt="Grouped bar chart (default Plotly) showing life expectancy in 1967 and 2007 for four countries. Bars: blue for 1967, red for 2007."/>

### Colours

Easily return a list of colours from any of the Analysis Function [accessible colour palettes](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-colours-in-charts/#section-4) with the `get_af_colours()` function:

```python
from py_af_colours import get_af_colours

# Get the duo colour palette hex codes
duo = get_af_colours("duo")

# Get four hex codes from the categorical palette
cat4 = get_af_colours("categorical", "rgb", 5)
```

## Getting help
If you encounter a bug, please file a minimal reproducible example on [Github Issues](https://github.com/best-practice-and-impact/afcharts-py/issues). For questions and other discussion, please start a [discussion](https://github.com/best-practice-and-impact/afcharts-py/discussions).

## Contributing
Interested in contributing? Check out the [contributing guidelines](CONTRIBUTING.md). 

## Acknowledgments
The afcharts python package is based on the
[afcharts](https://github.com/best-practice-and-impact/afcharts.git) R package and the [py-af-colours](https://github.com/best-practice-and-impact/py-af-colours) package.

## License
Unless stated otherwise, the codebase is released under [the MIT License](LICENSE.md). This covers both the codebase and any sample code in the documentation.

The documentation is [© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/) and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.