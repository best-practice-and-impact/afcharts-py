
# afcharts-py <img src="src/afcharts/assets/logo.svg" alt="afcharts logo" align="right" height="150"/>

afcharts-py is an Python package for creating accessible plots by the Government
Analysis Function. Currently, functions are available for styling
plotly and basic matplotlib plots.

The package has been developed using the [Government Analysis Function
Data Visualisation
guidance](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/).
afcharts-py should be used in conjunction with these guidance documents.

More information about the package and its functions can be found on the
[afcharts
website](https://best-practice-and-impact.github.io/afcharts/).

## Installation

```bash
pip install afcharts-py
```

## Usage

### Matplotlib

To use the afcharts style in matplotlib, import the package, then simple use the afcharts style with

```python
import afcharts
import matplotlib.pytplot as plt
plt.style.use('afcharts')
```

### Ploty

Basic exaple of using the plotly pio template to produce charts.

```python

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# AF Package
from afcharts.pio_template import pio

# # Set the template
# pio.templates.default = "theme_af"

# Load the gapminder dataset from plotly.express
df = px.data.gapminder().query("year == 2007 & continent == 'Americas'")

top5 = df.nlargest(5, "pop")

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=top5["country"],
        y=top5["pop"],  # Repeat the category name for each x value
        name="test bar",  # Use the x value column name as the trace name
    )
)

# Update layout
fig.update_layout(
    meta=dict(alt="Bar chart showing sales of Product A (23 units), Product B (45 units), and Product C (56 units)."),
)

fig.show()

```

then create your chart as normal.

## Acknowledgments

The afcharts package is based on the
[afcharts](https://github.com/best-practice-and-impact/afcharts.git) package

## License

Unless stated otherwise, the codebase is released under [the MIT
License](LICENSE). This covers both the codebase and any sample code in
the documentation.

The documentation is [© Crown
copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/)
and available under the terms of the [Open Government
3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
licence.
