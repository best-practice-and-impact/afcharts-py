import pandas as pd
import plotly.graph_objects as go

# TODO: auto adjust label position

def add_line_end_labels(
    fig: go.Figure,
    *,
    include_value: bool = False,
) -> go.Figure:
    """Add a label to the final valid point of each line trace.

    Args:
        fig: Plotly figure to update.
        include_value: Include the final y value after the trace name.

    Returns:
        The updated Plotly figure.
    """
    for trace in fig.data:
        # Only label Scatter traces containing a line.
        if not isinstance(trace, go.Scatter):
            continue

        mode = trace.mode or ""
        if "lines" not in mode:
            continue

        if trace.x is None or trace.y is None:
            continue

        # Work backwards to find the final non-null x/y pair.
        last_point = next(
            ((x, y) for x, y in reversed(list(zip(trace.x, trace.y, strict=False))) if pd.notna(x) and pd.notna(y)),
            None,
        )

        if last_point is None:
            continue

        x, y = last_point

        label = str(trace.name or "")
        if include_value:
            label = f"{label}: {y:g}" if label else f"{y:g}"

        fig.add_annotation(
            x=x,
            y=y,
            text=label,
            showarrow=False,
            xanchor="left",
            yanchor="middle",
            bgcolor="white",  # Add a white background
        )
    return fig
