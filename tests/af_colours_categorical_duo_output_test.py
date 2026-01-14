"""
Unit tests for the `get_af_colours` function in the afcharts package.

These tests verify behaviour when the categorical palette is asked to return 2 colours.
The expected behaviour is that the `categorical` palette should fall back to the
`duo` palette when 2 colours are requested, ensuring consistent brand colour usage.

We test this behaviour for both HEX and RGB output formats.
"""

import pytest
from afcharts.af_colours import get_af_colours


@pytest.mark.parametrize(
    "palette, colour_format, number_of_colours, expected",
    [
        # Requesting 2 colours from DUO palette (baseline expectation)
        (
            "duo",
            "hex",
            2,
            get_af_colours("duo", "hex", 2),
        ),
        # Requesting 2 colours from CATEGORICAL palette should match DUO result
        (
            "categorical",
            "hex",
            2,
            get_af_colours("duo", "hex", 2),
        ),
    ],
)
def test_palette_fallback_to_duo_hex(
    palette, colour_format, number_of_colours, expected
):
    """
    Test that requesting 2 HEX colours from the categorical palette
    returns the same values as the duo palette (fallback behaviour).
    """
    assert get_af_colours(palette, colour_format, number_of_colours) == expected


@pytest.mark.parametrize(
    "palette, colour_format, number_of_colours, expected",
    [
        # DUO palette Standard RGB baseline
        (
            "duo",
            "rgb",
            2,
            get_af_colours("duo", "rgb", 2),
        ),
        # CATEGORICAL palette should match DUO when requesting 2 RGB colours
        (
            "categorical",
            "rgb",
            2,
            get_af_colours("duo", "rgb", 2),
        ),
    ],
)
def test_palette_fallback_to_duo_rgb(
    palette, colour_format, number_of_colours, expected
):
    """
    Test that requesting 2 RGB colours from the categorical palette
    returns the same values as the duo palette (fallback behaviour).
    """
    assert get_af_colours(palette, colour_format, number_of_colours) == expected
