import re
import pandas as pd
import math
from numerize.numerize import numerize
from textwrap import wrap
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
from typing import List, Dict, Optional, Union
from typeguard import typechecked

from afcharts_py.assets.af_colours import (
    main,
    sequential,
    sequential_minus,
    diverging,
    af_colour_values,
)

def create_line_chart(
    df,
    target_col=None,
    forecast_col=None,
    trajectory_col=None,
    area_lower_col=None,
    area_upper_col=None,
    area_name="Range",
    y_axis_start=None,
    y_axis_end=None,
    unit=None,
):
    y_values = df.columns[1:]

    p_multiplier = 1
    tickformat = ",.1f"
    tickprefix = ""
    ticksuffix = ""

    if unit and ("%" in unit):
        p_multiplier = 100
        ticksuffix = "%"
    elif unit and ("£" in unit):
        tickprefix = "£"

    df[y_values] = df[y_values] * p_multiplier

    # Checks if all values are greater than 100,000. If so adds a "m" marker and divides all values by 1,000,000.
    all_hundred_thousands = (
        df[y_values]
        .apply(lambda x: x.dropna().apply(lambda y: y >= 100_000).all())
        .all()
    )

    any_million = (
        df[y_values]
        .apply(lambda x: x.dropna().apply(lambda y: y >= 1_000_000).any())
        .any()
    )

    if all_hundred_thousands and any_million:
        df[y_values] = df[y_values] / 1_000_000
        ticksuffix = "m" + ticksuffix

    # Checks if all values are int. If so adjust the tick format not to show any decimal spaces.
    all_int = (
        df[y_values]
        .apply(
            lambda x: x.dropna()
            .apply(
                lambda y: isinstance(y, int)
                or (isinstance(y, float) and y.is_integer())
            )
            .all()
        )
        .all()
    )
    if all_int:
        tickformat = ",.0f"

    fig = go.Figure()

    # Filters y_values to exclude target/forecast/trajectory/area columns as these are added separately
    for col_group in [
        target_col,
        forecast_col,
        trajectory_col,
        area_lower_col,
        area_upper_col,
    ]:
        if col_group:
            y_values = [col for col in y_values if col not in col_group]

    # Add an area if required
    if area_lower_col and area_upper_col:
        fig.add_trace(
            go.Scatter(
                x=np.concatenate(
                    (df.iloc[:, 0].to_numpy(), df.iloc[:, 0][::-1].to_numpy())
                ),
                y=np.concatenate(
                    (df[area_upper_col].to_numpy(), df[area_lower_col][::-1].to_numpy())
                ),
                fill="toself",
                mode="lines",
                name=area_name,
                line=dict(color=hex_to_rgba(main_palette["rag_red"], 0.1)),
                fillcolor=hex_to_rgba(main_palette["rag_red"], 0.1),
            )
        )

    i = 0
    # Add lines for each column in y_values
    for col in y_values:
        fig.add_trace(
            go.Scatter(
                x=df.iloc[:, 0],
                y=df[col],
                mode="lines",
                name=col,
                line=dict(color=categorical_palette[i]),
            )
        )

        last_index = df[col].last_valid_index()
        last_value_text = f"{float(df[col].loc[last_index]):{tickformat}}"

        if last_index is not None:
            fig.add_annotation(
                dict(
                    x=df.iloc[:, 0].loc[last_index],
                    y=df[col].loc[last_index],
                    text=f"{tickprefix}{last_value_text}{ticksuffix}",
                    font=dict(color=categorical_palette[i]),
                    showarrow=False,
                    xanchor="left",
                    yanchor="middle",
                )
            )

        i = i + 1

    # Add markers/lines for target and forecast columns
    for arg in [target_col, forecast_col]:
        if arg:
            if arg == target_col:
                palette = target_palette
            elif arg == forecast_col:
                palette = categorical_palette

            arg = arg.split(",")

            i = 0

            for col in arg:
                if len(df[col].dropna()) <= 1:
                    mode = "markers"
                else:
                    mode = "lines"

                fig.add_trace(
                    go.Scatter(
                        x=df.iloc[:, 0],
                        y=df[col],
                        line=dict(color=palette[i], dash="dash"),
                        mode=mode,
                        name=col,
                    )
                )

                last_index = df[col].last_valid_index()
                last_value_text = f"{float(df[col].loc[last_index]):{tickformat}}"

                if last_index is not None:
                    fig.add_annotation(
                        dict(
                            x=df.iloc[:, 0].loc[last_index],
                            y=df[col].loc[last_index],
                            text=f"{tickprefix}{last_value_text}{ticksuffix}",
                            showarrow=False,
                            xanchor="right",
                            yanchor="bottom",
                        )
                    )

                i = i + 1

    # if forecast_col:
    #     forecast_col = forecast_col.split(",")
    #     i = 0
    #     for col in forecast_col:
    #         fig.add_trace(
    #             go.Scatter(
    #                 x=df.iloc[:, 0],
    #                 y=df[col],
    #                 line=dict(color=categorical_palette[i], dash="dash"),
    #                 mode="lines",
    #                 name=col,
    #             )
    #         )

    #         last_index = df[col].last_valid_index()
    #         last_value_text = get_last_value_text(df[col], last_index)

    #         if last_index is not None:
    #             fig.add_annotation(
    #                 dict(
    #                     x=df.iloc[:, 0].loc[last_index],
    #                     y=df[col].loc[last_index],
    #                     text=f"{tickprefix}{last_value_text}{ticksuffix}",
    #                     showarrow=False,
    #                     xanchor="right",
    #                     yanchor="bottom",
    #                 )
    #             )

    #         i = i + 1

    # Add line(s) for trajectory column(s)
    if trajectory_col:
        trajectory_col = trajectory_col.split(",")
        for col in trajectory_col:
            fig.add_trace(
                go.Scatter(
                    x=df.iloc[:, 0],
                    y=df[col],
                    line=dict(color=main_palette["secondary"], dash="dash"),
                    mode="lines",
                    name=col,
                )
            )

    if y_axis_start and y_axis_end:
        fig.update_yaxes(range=[y_axis_start * p_multiplier, y_axis_end * p_multiplier])

    fig.update_layout(
        yaxis=dict(
            tickformat=tickformat,
            tickprefix=tickprefix,
            ticksuffix=ticksuffix,
        ),
    )

    return fig


def create_categorical_grouped_bar_chart(df, chart_type, unit, **kwargs):
    fig = go.Figure()

    tickprefix = ""
    ticksuffix = ""
    tickformat = ",.1f"
    p_multiplier = 1

    for j, col in enumerate(df.columns[1:]):
        if unit and ("%" in unit):
            p_multiplier = 100
            ticksuffix = "%"

        elif unit and ("£" in unit):
            tickprefix = "£"

        x_values = df[col] * p_multiplier
        all_int = (
            x_values.dropna()
            .apply(
                lambda x: isinstance(x, int)
                or (isinstance(x, float) and x.is_integer())
            )
            .all()
        )

        if all_int:
            tickformat = ",.0f"

        fig.add_trace(
            go.Bar(
                x=x_values,
                y=df.iloc[:, 0],  # Repeat the category name for each x value
                name=col,  # Use the x value column name as the trace name
                orientation="h",
                marker=dict(color=categorical_palette[j]),
                offsetgroup=col,  # Ensure bars are grouped correctly
                text=[f"{tickprefix}{p:{tickformat}}{tickprefix}" for p in x_values],
                textposition="auto",  # Position the labels automatically
            )
        )

    fig.update_layout(
        showlegend=True if "Stacked" in chart_type else False,
        barmode="stack" if "Stacked" in chart_type else "group",
        xaxis_title=kwargs.get("xaxis_title", None),
        yaxis_title=kwargs.get("yaxis_title", None),
        xaxis=dict(
            tickformat=tickformat,
            tickprefix=tickprefix,
            ticksuffix=ticksuffix,
        ),
    )

    return fig


def create_categorical_bar_chart(
    df, chart_type, timeline=None, rag_scale=False, unit=None, **kwargs
):
    fig = go.Figure()

    if not timeline:
        df = df.sort_values(by=df.columns[1], ascending=True)

    column_colors = categorical_palette[
        : len(df.columns[1:])
    ]  # Assign colors to each column

    for i, col in enumerate(df.columns[1:]):  # Loop over category columns
        x_values = df[col]
        all_int = (
            x_values.dropna()
            .apply(
                lambda x: isinstance(x, int)
                or (isinstance(x, float) and x.is_integer())
            )
            .all()
        )

        if all_int:
            tickformat = ",.0f"
        else:
            tickformat = ",.1f"

        if unit and ("%" in unit):
            x_values = x_values * 100
            text = [f"{p:{tickformat}}%" for p in x_values]
            tickprefix = ""
            ticksuffix = "%"
        elif unit and ("£" in unit):
            text = [f"£{p:{tickformat}}" for p in x_values]
            tickprefix = "£"
            ticksuffix = ""
        else:
            text = [f"{p:{tickformat}}" for p in x_values]
            tickprefix = ""
            ticksuffix = ""

        if rag_scale and rag_palette:
            color_palette = rag_palette.get(col, categorical_palette[i])
        else:
            color_palette = column_colors[i]  # Ensure each column gets its own color

        fig.add_trace(
            go.Bar(
                x=x_values,  # X-axis: values from columns
                y=df.iloc[:, 0],  # Y-axis: column names
                name=col,
                orientation="h",
                marker=dict(color=color_palette),
                text=text,  # Show values as text
                textposition="inside",  # Auto-position the text
                textangle=90,  # Rotate text by 90 degrees
            )
        )

    fig.update_layout(
        showlegend=True if (len(df.columns[1:]) > 1) else False,
        barmode="stack" if "Stacked" in chart_type else "group",
        xaxis_title=kwargs.get("xaxis_title", None),
        yaxis_title=kwargs.get("yaxis_title", None),
        xaxis=dict(
            tickformat=tickformat,
            tickprefix=tickprefix,
            ticksuffix=ticksuffix,
        ),
    )

    return fig


def create_single_stacked_bar_chart(df, y_axis_column, label_column, unit):
    fig = go.Figure()

    if not y_axis_column:
        y_axis_column = df.columns[1]

    if not label_column:
        label_column = df.columns[1]

    for i, cat in enumerate(df[df.columns[0]].unique()):
        df_filtered = df[df[df.columns[0]] == cat]
        all_int = (
            df_filtered[y_axis_column]
            .dropna()
            .apply(
                lambda x: isinstance(x, int)
                or (isinstance(x, float) and x.is_integer())
            )
            .all()
        )
        x_values = df_filtered[y_axis_column]
        if all_int:
            tickformat = ",.0f"
        else:
            tickformat = ",.1f"

        if unit and ("%" in unit):
            x_values = x_values * 100
            text = [f"{p:{tickformat}}%" for p in x_values]
            tickprefix = ""
            ticksuffix = "%"
        elif unit and ("£" in unit):
            text = [f"£{p:{tickformat}}" for p in x_values]
            tickprefix = "£"
            ticksuffix = ""
        else:
            text = [f"{p:{tickformat}}" for p in x_values]
            tickprefix = ""
            ticksuffix = ""

        fig.add_trace(
            go.Bar(
                y=[0] * len(df_filtered[y_axis_column]),
                x=x_values,
                name=cat,
                orientation="h",
                marker=dict(color=categorical_palette[i % len(categorical_palette)]),
                text=text,
            )
        )

    fig.update_layout(
        barmode="stack",
        yaxis=dict(visible=False, tickformat=tickformat),
        xaxis=dict(
            tickformat=tickformat,
            tickprefix=tickprefix,
            ticksuffix=ticksuffix,
        ),
    )

    return fig


def create_stacked_column_chart(
    df,
    chart_type,
    unit=None,
    timeline=None,
    target_col=None,
    rag_scale=False,
    rag_lookup=False,
):
    fig = go.Figure()

    tickprefix = ""
    ticksuffix = ""
    tickformat = ",.1f"
    p_multiplier = 1

    if unit and ("%" in unit):
        p_multiplier = 100
        ticksuffix = "%"

    elif unit and ("£" in unit):
        tickprefix = "£"

    if not timeline:
        df = df.sort_values(by=df.columns[1], ascending=False)

    if target_col:
        categories = df.drop(columns=[target_col]).columns[1:]
    else:
        categories = df.columns[1:]

    x_values = df.iloc[:, 0]

    # Checks if all values are greater than 100,000 and at least one value is greater than one million.
    # If so adds a "m" marker and divides all values by 1,000,000.
    all_hundred_thousands = (
        df[categories]
        .apply(lambda x: x.dropna().apply(lambda y: y >= 100_000).all())
        .all()
    )

    any_million = (
        df[categories]
        .apply(lambda x: x.dropna().apply(lambda y: y >= 1_000_000).any())
        .any()
    )

    if all_hundred_thousands and any_million:
        df[categories] = df[categories] / 1_000_000
        ticksuffix = "m" + ticksuffix

    all_int = (
        df[categories]
        .apply(
            lambda x: x.dropna()
            .apply(
                lambda y: isinstance(y, int)
                or (isinstance(y, float) and (y * p_multiplier).is_integer())
            )
            .all()
        )
        .all()
    )
    if all_int:
        tickformat = ",.0f"

    for i, cat in enumerate(categories):
        if rag_scale:
            if rag_lookup:
                rag_lookup_dict = dict(
                    item.split(":") for item in rag_lookup.split(";")
                )
                rag_value = rag_lookup_dict.get(cat)
                color_palette = rag_palette[rag_value]
            else:
                color_palette = rag_palette[cat]
        else:
            color_palette = categorical_palette[i]

        fig.add_trace(
            go.Bar(
                x=x_values,  # Use the first column for x-axis values
                y=df[cat]
                * p_multiplier,  # Use the values of the current category for y-axis
                name=cat,
                marker=dict(color=color_palette),
                text=[
                    f"{tickprefix}{p * p_multiplier:{tickformat}}{ticksuffix}"
                    for p in df[cat]
                ],
                textposition="auto",
                textfont=dict(size=9),
            )
        )

    if target_col:
        fig.add_trace(
            go.Scatter(
                x=x_values,
                y=df[target_col] * p_multiplier,
                line=dict(color=main_palette["target"], dash="dash", width=2),
                mode="lines",
                name=str(target_col),
            )
        )

        fig.add_annotation(
            dict(
                x=x_values.iloc[-1],
                y=df[target_col].iloc[-1] * p_multiplier,
                xanchor="left",
                yanchor="middle",
                text=f"{tickprefix}{df[target_col].iloc[-1] * p_multiplier:{tickformat}}{ticksuffix}",
                showarrow=False,
            )
        )

    max_y = df[categories].max().max()
    max_y = max_y + (0.1 * max_y)
    min_y = df[categories].min().min()
    min_y = 0 if min_y >= 0 else min_y + (min_y * 0.1)

    fig.update_layout(
        barmode="stack" if "Stacked" in chart_type else "group",
        showlegend=True if (len(df.columns[1:]) > 1) else False,
        yaxis=dict(
            tickformat=tickformat,
            tickprefix=tickprefix,
            ticksuffix=ticksuffix,
            range=[min_y, max_y],
        ),
    )

    return fig


def create_pie_chart(df, rag_scale=False, rag_lookup=False, unit=False):
    tickformat = ",.1f"
    tickprefix = ""
    ticksuffix = ""

    if rag_scale:
        rag_lookup_dict = dict(item.split(":") for item in rag_lookup.split(";"))
        df["rag"] = df.iloc[:, 0].map(rag_lookup_dict)
        df["rag"] = pd.Categorical(df["rag"], categories=rag_order, ordered=True)
        df = df.sort_values(
            by=["rag"],
        ).reset_index(drop=True)

    labels = df.iloc[:, 0]
    values = df.iloc[:, 1]

    if unit and ("%" in unit):
        values = values * 100
        ticksuffix = "%"
    elif unit and ("£" in unit):
        tickprefix = "£"

    all_hundred_thousands = values.dropna().apply(lambda x: x >= 100_000).all()
    any_million = values.dropna().apply(lambda x: x >= 1_000_000).any()
    if all_hundred_thousands and any_million:
        values = values / 1_000_000
        ticksuffix = "m" + ticksuffix

    all_int = (
        values.dropna()
        .apply(
            lambda x: isinstance(x, int) or (isinstance(x, float) and x.is_integer())
        )
        .all()
    )
    if all_int:
        tickformat = ",.0f"

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                direction="clockwise",
                sort=True if rag_scale else False,
                texttemplate=[
                    f"{tickprefix}{p:{tickformat}}{ticksuffix}" for p in values
                ],
                hole=0.4,
            )
        ]
    )

    if rag_scale:
        fig.update_traces(marker=dict(colors=[rag_palette[key] for key in df["rag"]]))

    fig.update_layout(margin=dict(t=50))
    return fig


def replace_first_list_element(lst: list, new_value) -> list:
    """
    Replace an element in a list by its position.

    Parameters:
    lst (list): The input list.
    position (int): The index position of the element to be replaced.
    new_value: The new value to replace the old element.

    Returns:
    list: The list with the element replaced.
    """
    if 0 < len(lst):
        lst[0] = new_value
    else:
        raise IndexError("Position out of range")
    return lst


def create_waterfall_chart(df):
    fig = go.Figure(
        go.Waterfall(
            x=df.iloc[:, 0],
            y=df.iloc[:, 1],
            decreasing={"marker": {"color": main_palette["secondary"]}},
            increasing={"marker": {"color": main_palette["primary"]}},
            text=replace_first_list_element(df.iloc[:, 1], None),
            textposition="outside",
            connector={"line": {"width": 2, "color": main_palette["chart_features"]}},
        )
    )

    return fig


def create_variable_chart(
    df,
    title,
    chart_type,
    area_lower_col=None,
    area_upper_col=None,
    area_name=None,
    target_col=None,
    forecast_col=None,
    trajectory_col=None,
    y_axis_start=None,
    y_axis_end=None,
    unit=None,
    rag_scale=False,
):

    commentary = row["commentary"] if row["commentary"] else None
    source = row["source"] if row["source"] else None
    notes_and_caveats = row["notes_and_caveats"] if row["notes_and_caveats"] else None
    latest_return = row["latest_return"] if row["latest_return"] else None

    # Run the appropriate create chart function based on chart type

    if chart_type == "Line Area" or chart_type == "Line":
        figure = create_line_chart(
            df,
            area_lower_col=row.get("area_low_bound", None),
            area_upper_col=row.get("area_upper_bound", None),
            area_name=row.get("area_label", None),
            target_col=row.get("target_col", None),
            forecast_col=row.get("forecast_col", None),
            trajectory_col=row.get("trajectory_col", None),
            y_axis_start=row.get("y_axis_start", None),
            y_axis_end=row.get("y_axis_end", None),
            unit=row.get("unit", None),
        )
    elif chart_type == "Single Stacked Bar":
        figure = create_single_stacked_bar_chart(
            df,
            y_axis_column=row.get("y_axis_column", None),
            label_column=row.get("label_column", None),
            unit=row.get("unit", None),
        )
    elif chart_type in ["Categorical Bar", "Stacked Categorical Bar"]:
        figure = create_categorical_bar_chart(
            df,
            chart_type,
            timeline=row.get("timeline", False),
            rag_scale=row.get("rag_scale", None),
            unit=row.get("unit", None),
        )
    elif chart_type in ["Grouped Bar", "Stacked Bar"]:
        figure = create_categorical_grouped_bar_chart(
            df, chart_type, unit=row.get("unit", None), rag_scale=rag_scale
        )
    elif chart_type in ["Column", "Grouped Column", "Stacked Column"]:
        figure = create_stacked_column_chart(
            df,
            chart_type,
            unit=row.get("unit", None),
            timeline=row.get("timeline", False),
            target_col=row.get("target_col", None),
            rag_scale=row.get("rag_scale", None),
            rag_lookup=row.get("rag_lookup", None),
        )
    elif chart_type == "Pie":
        figure = create_pie_chart(
            df,
            rag_scale=row.get("rag_scale", None),
            rag_lookup=row.get("rag_lookup", None),
            unit=row.get("unit", None),
        )
    elif chart_type == "Waterfall":
        figure = create_waterfall_chart(df)

    return figure
