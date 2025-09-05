import os

import plotly.express as px
import plotly.graph_objects as go

# AF Package
from afcharts.assets.af_colours import duo
from afcharts.pio_template import pio


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
            title="Year",
        ),
        meta=dict(
            alt="Bar chart showing sales of Product A (23 units), Product B (45 units), and Product C (56 units)."
        ),
    )

    fig.update_yaxes(range=[0, 82])

    if not os.environ.get("CI"):
        fig.show()

    assert isinstance(fig, go.Figure)
