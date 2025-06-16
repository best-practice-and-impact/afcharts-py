from afcharts_py.assets.pio_template import pio
import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv("test_data/bar_chart.csv")

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=df["Category"],
        y=df["Value"],  # Repeat the category name for each x value
        name="test bar",  # Use the x value column name as the trace name
    )
)

fig.update_layout(
    template="af_pio",
    yaxis={"showgrid": True},
    title=dict(
        text="Quarterly Sales Report<br><sup>Sales performance of top products</sup>",
        xref="paper",
        x=0,
        xanchor="left",
    ),
    margin=dict(b=100),  # Increase bottom margin to make space for annotation
    annotations=[
        dict(
            text="Source: Internal Sales Database",
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

fig.show()
