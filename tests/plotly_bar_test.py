import os

import plotly.express as px
import plotly.graph_objects as go

from afcharts.pio_template import pio

# Set default theme
pio.templates.default = "afcharts"


def test_plotly_bar_chart():
    # Only set the renderer to "browser" if not running in CI
    if not os.environ.get("CI"):
        pio.renderers.default = "browser"

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
    fig.update_layout(height=300)

    if not os.environ.get("CI"):
        fig.show()

    assert isinstance(fig, go.Figure)
