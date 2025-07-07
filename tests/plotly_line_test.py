import os

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

from afcharts.assets.af_colours import duo

# AF Package
from afcharts.theme_af import theme_af

# Only set the renderer to "browser" if not running in CI
if not os.environ.get("CI"):
    pio.renderers.default = "browser"

# Load the gapminder dataset from plotly.express
df = px.data.gapminder()

df = df[df["country"].isin(["United Kingdom", "China"])]

fig = go.Figure()

# Add a trace for each continent
for country in df["country"].unique():
    df_country = df[df["country"] == country]
    fig.add_trace(
        go.Scatter(
            x=df_country["year"],
            y=df_country["lifeExp"],
            mode="lines",
            name=country,
            text=df_country["country"],
        )
    )

# Update layout
fig.update_layout(
    template=theme_af(grid="y", colour_palette=duo),
    xaxis=dict(
        title="Year",
    ),
    title=dict(
        text="Living Longer",
        subtitle=dict(text="Life Expectancy in the United Kingdom and China 1952-2007"),
    ),
    margin=dict(b=70),  # Increase bottom margin to make space for source
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
    meta=dict(alt="Bar chart showing sales of Product A (23 units), Product B (45 units), and Product C (56 units)."),
)

fig.update_yaxes(range=[0, 82])

if not os.environ.get("CI"):
    fig.show()
else:
    if isinstance(fig, go.Figure):
        pass
