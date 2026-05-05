"""
Tests for the sequential palette in `get_af_colours`.

These tests verify:
- Length: requesting 3, 4, or 5 colours returns the correct count.
- Invalid values: requesting 1, 2, 6, 7, or 0 raises ValueError.
- Exact values: 3, 4, and 5 return the guidance-specified hex lists.
- Grey inclusion: include_grey=True appends the grey colour.
"""

import pytest

from afcharts.af_colours import get_af_colours


# Test valid list lengths
@pytest.mark.parametrize(
    "palette, colour_format, number_of_colours",
    [
        ("sequential", "hex", 3),
        ("sequential", "hex", 4),
        ("sequential", "hex", 5),
        ("sequential", "rgb", 3),
        ("sequential", "rgb", 4),
        ("sequential", "rgb", 5),
    ],
)
def test_sequential_list_length(palette, colour_format, number_of_colours):
    """
    Ensure the sequential palette returns exactly the requested number of colours.
    """
    result = get_af_colours(palette, colour_format, number_of_colours)
    assert len(result) == number_of_colours

# Test invalid values
@pytest.mark.parametrize(
    "palette, colour_format, number_of_colours",
    [
        ("sequential", "hex", 1),
        ("sequential", "hex", 2),
        ("sequential", "hex", 6),
        ("sequential", "hex", 7),
        ("sequential", "rgb", 0),
    ],
)
def test_sequential_invalid_number_of_colours(palette, colour_format, number_of_colours):
    """
    Ensure invalid number_of_colours values raise ValueError.
    """
    with pytest.raises(ValueError):
        get_af_colours(palette, colour_format, number_of_colours)

# Test exact colour lists
@pytest.mark.parametrize(
    "number_of_colours, expected",
    [
        (3, ["#12436D", "#2073BC", "#6BACE6"]),
        (4, ["#092135", "#12436D", "#2073BC", "#6BACE6"]),
        (5, ["#092135", "#12436D", "#2073BC", "#6BACE6", "#ADD1F1"]),
    ],
)
def test_sequential_exact_values(number_of_colours, expected):
    """
    Ensure sequential palettes return the exact hex values in the correct order.
    """
    result = get_af_colours("sequential", "hex", number_of_colours)
    assert result == expected


# Test with include_grey
@pytest.mark.parametrize(
    "number_of_colours, expected_length",
    [
        (3, 4),
        (4, 5),
        (5, 6),
    ],
)
def test_sequential_list_length_with_grey(number_of_colours, expected_length):
    """
    Ensure the sequential palette with include_grey=True returns N+1 colours.
    """
    result = get_af_colours("sequential", "hex", number_of_colours, include_grey=True)
    assert len(result) == expected_length


@pytest.mark.parametrize(
    "number_of_colours, expected",
    [
        (3, ["#12436D", "#2073BC", "#6BACE6", "#F2F2F2"]),
        (4, ["#092135", "#12436D", "#2073BC", "#6BACE6", "#F2F2F2"]),
        (5, ["#092135", "#12436D", "#2073BC", "#6BACE6", "#ADD1F1", "#F2F2F2"]),
    ],
)
def test_sequential_exact_values_with_grey(number_of_colours, expected):
    """
    Ensure sequential palettes with include_grey=True return the correct hex values with grey appended.
    """
    result = get_af_colours("sequential", "hex", number_of_colours, include_grey=True)
    assert result == expected
