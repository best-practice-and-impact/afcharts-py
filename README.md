
# afcharts <img src="src/afcharts/assets/logo.svg" alt="afcharts logo" align="right" height="150"/>

afcharts is a Python package for creating accessible charts following Government Analysis Function best practice. Currently, the package supports plots made in Matplotlib or Plotly.

The package has been developed using the [Government Analysis Function Data Visualisation
guidance](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/).
afcharts should be used in conjunction with these guidance documents.

## Installation

```bash
pip install afcharts
```

## Usage

See the [afcharts cookbook](https://best-practice-and-impact.github.io/afcharts/) for examples of many different types of chart.

### Matplotlib

```python
import matplotlib.pyplot as plt

# Apply the afcharts style to all Matplotlib plots
plt.style.use('afcharts.afcharts')
```

### Plotly

```python
from afcharts.pio_template import pio

# Apply the afcharts style to all Plotly plots
pio.templates.default = "theme_af"
```

## Contributing
Interested in contributing? Check out the [contributing guidelines](CONTRIBUTING.md). 

## Acknowledgments

The afcharts package is based on the
[afcharts](https://github.com/best-practice-and-impact/afcharts.git) R package and the [py-af-colours](https://github.com/best-practice-and-impact/py-af-colours) package.

## License

Unless stated otherwise, the codebase is released under [the MIT License](LICENSE.md). This covers both the codebase and any sample code in the documentation.

The documentation is [© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/) and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.