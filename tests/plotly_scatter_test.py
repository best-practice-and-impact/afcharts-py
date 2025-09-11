import os

import plotly.express as px
import plotly.graph_objects as go

# AF Package
from afcharts.pio_template import pio

# Set default theme
pio.templates.default = "theme_af"


def test_plotly_scatter_chart():
    # Only set the renderer to "browser" if not running in CI
    if not os.environ.get("CI"):
        pio.renderers.default = "browser"

    # Load the gapminder dataset from plotly.express
    df = px.data.gapminder()

    df = df.query("year == 2007")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["gdpPercap"],
            y=df["lifeExp"],
            mode="markers",
        )
    )

    # Update layout
    fig.update_layout(
        xaxis=dict(
            title="GDP (US$, inflation-adjusted)",
        ),
        yaxis=dict(
            title="Life\nExpectancy",
        ),
        height=300,
    )

    if not os.environ.get("CI"):
        fig.show()

    assert isinstance(fig, go.Figure)
