"""
Unit tests for `af_colours` function in the afcharts package.

This test verifies that requesting N colours from the categorical palette
returns exactly N colours. It ensures the function respects the requested
length and does not return fewer or more colours than expected.

The categorical palette supports up to 6 colours, so we parameterise tests
for sizes 1 through 6.

"""

import pytest
from afcharts.af_colours import af_colours


@pytest.mark.parametrize(
    "palette, colour_format, number_of_colours",
    [
        # Test categorical palette for length boundaries (1–6 supported values)
        ("categorical", "hex", 1),
        ("categorical", "hex", 2),
        ("categorical", "hex", 3),
        ("categorical", "hex", 4),
        ("categorical", "hex", 5),
        ("categorical", "hex", 6),
    ],
)
def test_categorical_list_length(palette, colour_format, number_of_colours):
    """
    Ensure the categorical palette returns exactly the requested number of colours.

    For each input combination (palette, format, N colours),
    verify that the resulting colour list length equals `number_of_colours`.
    """
    result = af_colours(palette, colour_format, number_of_colours)
    assert len(result) == number_of_colours, (
        f"Expected {number_of_colours} colours but got {len(result)} for "
        f"palette='{palette}', format='{colour_format}'"
    )
