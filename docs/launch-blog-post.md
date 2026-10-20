# afcharts for Python: accessible charts made easier

The [Analysis Function data visualisation guidance](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/) helps analysts create charts that are clear, impactful and accessible to all users. But applying it by hand — choosing the right fonts, colours, gridlines and layout for every chart — takes time and leaves room for mistakes. The [afcharts R package](https://best-practice-and-impact.github.io/afcharts/) has long solved this for R users. Now afcharts is available for Python too.

afcharts automatically applies the recommended styles and [accessible colour palettes](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-colours-in-charts/) to your charts. Write your chart as normal in Matplotlib or Plotly — afcharts handles the rest.

## Getting started

Install afcharts from PyPI with a single command:

```bash
pip install afcharts
```

Then apply the afcharts style to all your charts. For Matplotlib:

```python
import matplotlib.pyplot as plt
plt.style.use('afcharts.afcharts')
```

For Plotly:

```python
from afcharts.pio_template import pio
pio.templates.default = "afcharts"
```

Every chart you create after running these lines will have the recommended fonts, axes, gridlines and layout automatically.

## Accessible colour palettes

The `get_af_colours()` function returns colours from the [Analysis Function colour palettes](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-colours-in-charts/). There are four palettes to choose from: categorical (up to 6 groups), duo (comparisons), sequential (ordered data) and focus (highlight a single series). Each palette is designed to be accessible and easy to distinguish.

```python
from afcharts.af_colours import get_af_colours
colours = get_af_colours("categorical")
```

## Example charts

With afcharts, the core formatting in both charts below came for free — fonts, axes, gridlines and layout applied automatically.

**Figure 1: Life expectancy in the UK and China, 1952 to 2007**

[IMAGE (docs\images\example_charts\line_chart-matplotlib_afcharts.svg): A line chart showing life expectancy over time in the UK and China, using the duo colour palette. | alt text: Line chart showing life expectancy in China and the UK from 1952 to 2007, styled with the afcharts duo colour palette. Two lines rise from 1952 to 2007, with China showing a steeper increase.]
Full code: [Matplotlib](https://best-practice-and-impact.github.io/afcharts-py/02-matplotlib-usage.html#line-chart-with-duo-palette) | [Plotly](https://best-practice-and-impact.github.io/afcharts-py/03-plotly-usage.html#line-chart-with-duo-palette)

**Figure 2: Population by continent, 1952 to 2007**

[IMAGE (docs\images\example_charts\area_chart-matplotlib_afcharts.svg): A small multiples area chart showing population over time by continent from 1952 to 2007. | alt text: Small multiples area chart showing population growth by continent from 1952 to 2007 in Africa, Asia, Europe and the Americas, styled with afcharts. Each panel displays one continent with a shaded area beneath the line.]
Full code: [Matplotlib](https://best-practice-and-impact.github.io/afcharts-py/02-matplotlib-usage.html#small-multiples) | [Plotly](https://best-practice-and-impact.github.io/afcharts-py/03-plotly-usage.html#small-multiples)

## The afcharts cookbook

The [afcharts cookbook](https://best-practice-and-impact.github.io/afcharts-py/) contains full, reusable code examples for common chart types — including bar charts, scatter plots and maps — in both Matplotlib and Plotly.

The cookbook goes beyond what afcharts applies automatically, covering techniques such as [text wrapping](https://best-practice-and-impact.github.io/afcharts-py/02-matplotlib-usage.html#wrapping-text) to improve readability and [chart annotations](https://best-practice-and-impact.github.io/afcharts-py/03-plotly-usage.html#annotations) to supplement or replace legends that rely on colour alone. Each example is designed to be copied and adapted for your own charts, saving you time and helping you consistently meet the Analysis Function guidance.

## Give feedback

We welcome your feedback. If you find a bug or want to suggest a feature, raise an issue on our [GitHub](https://github.com/best-practice-and-impact/afcharts-py). For general questions, start a thread on [GitHub Discussions](https://github.com/best-practice-and-impact/afcharts-py/discussions).


*Thank you to the Data Visualisation Python Tools group in the GSS Presentation Champions Network for building this package. The afcharts Python package builds on the afcharts R package and the py-af-colours package.*
