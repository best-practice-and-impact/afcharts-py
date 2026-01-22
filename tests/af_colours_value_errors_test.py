"""
Tests for validating error handling in the `get_af_colours` function.

These tests ensure that the function raises `ValueError` when invalid input
parameters are provided, including:
- Unsupported palette name
- Unsupported colour format
- Requesting fewer colours than allowed
- Requesting more colours than allowed

This guarantees the function fails safely and predictably when encountering
invalid user input.
"""

import pytest
from afcharts.af_colours import get_af_colours


def test_invalid_palette_value():
    """
    Verify an invalid colour palette name triggers a ValueError.
    """
    with pytest.raises(ValueError):
        get_af_colours("wrong_palette", "hex")


def test_invalid_colour_format_value():
    """
    Verify an unsupported colour format triggers a ValueError.
    """
    with pytest.raises(ValueError):
        get_af_colours("duo", "wrong_format")


def test_invalid_low_number_of_colours_value():
    """
    Verify requesting zero colours triggers a ValueError.
    """
    with pytest.raises(ValueError):
        get_af_colours("categorical", "hex", 0)


def test_invalid_high_number_of_colours_value():
    """
    Verify requesting more colours than the palette supports triggers a ValueError.
    """
    with pytest.raises(ValueError):
        get_af_colours("categorical", "hex", 7)
