import os

import plotly.express as px
import plotly.graph_objects as go

from afcharts.af_colours import get_af_colours
from afcharts.pio_template import pio

# Set default theme
pio.templates.default = "theme_af"

# Get the duo colour palette
duo = get_af_colours("duo")


def test_plotly_line_chart():
    # Only set the renderer to "browser" if not running in CI
    if not os.environ.get("CI"):
        pio.renderers.default = "browser"

    # Load the gapminder dataset from plotly.express
    df = px.data.gapminder()

    df = df[df["country"].isin(["United Kingdom", "China"])]

    fig = go.Figure()

    # Add a trace for each continent
    for i, country in enumerate(df["country"].unique()):
        df_country = df[df["country"] == country]
        fig.add_trace(
            go.Scatter(
                x=df_country["year"],
                y=df_country["lifeExp"],
                mode="lines",
                name=country,
                text=df_country["country"],
                line=dict(color=duo[i % len(duo)]),
            )
        )

    # Update layout
    fig.update_layout(
        xaxis=dict(
            showgrid=False,  # Hide x-axis grid lines
        ),
        yaxis=dict(
            title="Life Expectancy",
            range=[0, 82],
            tickmode="linear",
            dtick=20,  # Show ticks every 20 units
        ),
        height=300,
    )

    if not os.environ.get("CI"):
        fig.show()

    assert isinstance(fig, go.Figure)
