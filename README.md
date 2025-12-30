
# afcharts-py <img src="src/afcharts/assets/logo.svg" alt="afcharts logo" align="right" height="150"/>

afcharts-py is a Python package for creating accessible charts following Government Analysis Function best practice. Currently, the package supports plots made in Matplotlib or Plotly.

The package has been developed using the [Government Analysis Function Data Visualisation
guidance](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/).
afcharts-py should be used in conjunction with these guidance documents.

## Installation

```bash
pip install afcharts-py
```

## Usage

Analysis Function **formatting** can be applied to any Matplotlib or Plotly chart using the built-in style sheets. afcharts-py also provides easy access to the Analysis Function recommended **colour palettes**.

See the [afcharts-py cookbook](https://best-practice-and-impact.github.io/afcharts-py/) for extensive code examples for many common chart types.

### Matplotlib

```python
import matplotlib.pyplot as plt

# Apply the afcharts style to all Matplotlib plots
plt.style.use('afcharts.afcharts')
```

Example: A [Matplotlib bar chart](https://best-practice-and-impact.github.io/afcharts-py/01-matplotlib-usage.html#grouped-bar-chart) with afcharts (left) and without (right)

<img src="docs/images/example_charts/bar_chart-matplotlib_afcharts.png" width="45%" alt="Grouped bar chart (afcharts style) showing life expectancy in 1967 and 2007 for four countries. Bars use Analysis Function palette: dark blue for 1967, orange for 2007."/> <img src="docs/images/example_charts/bar_chart-matplotlib_default.png" width="44.6%" alt="Grouped bar chart (default Matplotlib) showing life expectancy in 1967 and 2007 for four countries. Bars: blue for 1967, orange for 2007."/>

<!-- | Matplotlib + afcharts | Default Matplotlib |
|:---------------:|:------------------:|
| <img src="docs/images/example_charts/bar_chart-matplotlib_afcharts.png" alt="Grouped bar chart (afcharts style) showing life expectancy in 1967 and 2007 for four countries. Bars use Analysis Function palette: dark blue for 1967, orange for 2007."/> | <img src="docs/images/example_charts/bar_chart-matplotlib_default.png" alt="Grouped bar chart (default Matplotlib) showing life expectancy in 1967 and 2007 for four countries. Bars: blue for 1967, orange for 2007."/> | -->

### Plotly

```python
from afcharts.pio_template import pio

# Apply the afcharts style to all Plotly plots
pio.templates.default = "theme_af"
```

Example: A [Plotly bar chart](https://best-practice-and-impact.github.io/afcharts-py/03-plotly-usage.html#grouped-bar-chart), with afcharts (left) and without (right)

<img src="docs/images/example_charts/bar_chart-plotly_afcharts.png" width="45%" alt="Grouped bar chart (afcharts style) showing life expectancy in 1967 and 2007 for four countries. Bars use Analysis Function palette: dark blue for 1967, orange for 2007."/> <img src="docs/images/example_charts/bar_chart-plotly_default.png" width="45%" alt="Grouped bar chart (default Plotly) showing life expectancy in 1967 and 2007 for four countries. Bars: blue for 1967, red for 2007."/>

### Colours

Easily return a list of colours from the Analysis Function [accessible colour palettes](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-colours-in-charts/#section-4) with the `af_colours()` function:

```python
from py_af_colours import af_colours

# Get the duo colour palette hex codes
duo = af_colours("duo")

# Get a five colour categorical palette as rgb codes
cat5 = af_colours("categorical", "rgb", 5)
```

## Getting help
If you encounter a bug, please file a minimal reproducible example on [Github Issues](https://github.com/best-practice-and-impact/afcharts-py/issues). For questions and other discussion, please start a [discussion](https://github.com/best-practice-and-impact/afcharts-py/discussions).

## Contributing
Interested in contributing? Check out the [contributing guidelines](CONTRIBUTING.md). 

## Acknowledgments
The afcharts-py package is based on the
[afcharts](https://github.com/best-practice-and-impact/afcharts.git) R package and the [py-af-colours](https://github.com/best-practice-and-impact/py-af-colours) package.

## License
Unless stated otherwise, the codebase is released under [the MIT License](LICENSE.md). This covers both the codebase and any sample code in the documentation.

The documentation is [© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/) and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.