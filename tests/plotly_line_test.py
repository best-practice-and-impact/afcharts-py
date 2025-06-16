from afcharts_py.assets.pio_template import pio
from afcharts_py.theme_af import theme_af
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

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
    template=theme_af(),
    yaxis=dict(showgrid=True),
    xaxis=dict(
        title="Year",
    ),
    title=dict(
        text="Living Longer",
        subtitle=dict(text="Life Expectancy in the United Kingdom and China 1952-2007"),
    ),
    margin=dict(b=100),  # Increase bottom margin to make space for source
    annotations=[
        dict(
            text="Source: Gapminder",
            xref="paper",
            yref="paper",
            x=0,
            y=-0.1,
            showarrow=False,
            xanchor="left",
        )
    ],
    meta=dict(
        alt="Bar chart showing sales of Product A (23 units), Product B (45 units), and Product C (56 units)."
    ),
)

fig.update_yaxes(range=[0, 82])

fig.show()
