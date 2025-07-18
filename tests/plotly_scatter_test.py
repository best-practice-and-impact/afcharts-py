import os

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

from afcharts.assets.af_colours import duo

# AF Package
from afcharts.theme_af import theme_af


def test_plolty_line_chart():
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
        template=theme_af(grid="xy", colour_palette=duo),
        xaxis=dict(
            title="GDP (US$, inflation-adjusted)",
        ),
        yaxis=dict(
            title="Life\nExpectancy",
        ),
        title=dict(
            text="The relationship between GDP and Life Expectancy is complex",
            subtitle=dict(text="GDP and Life Expectancy for all countires, 2007"),
        ),
        annotations=[
            dict(
                text="Source: Gapminder",
                xref="paper",
                yref="paper",
                x=0,
                y=-0.1,
                xanchor="left",
            )
        ],
    )

    if not os.environ.get("CI"):
        fig.show()

    assert isinstance(fig, go.Figure)
