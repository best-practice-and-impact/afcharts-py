"""
Tests for validating error handling in the `af_colours` function.

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
from afcharts.af_colours import af_colours

# Path to the test configuration file containing palette definitions
unit_test_config_path = "../src/afcharts/config/af_colours.yaml"


def test_invalid_palette_value():
    """
    Verify an invalid colour palette name triggers a ValueError.
    """
    with pytest.raises(ValueError):
        af_colours("wrong_palette", "hex", config_path=unit_test_config_path)


def test_invalid_colour_format_value():
    """
    Verify an unsupported colour format triggers a ValueError.
    """
    with pytest.raises(ValueError):
        af_colours("duo", "wrong_format", config_path=unit_test_config_path)


def test_invalid_low_number_of_colours_value():
    """
    Verify requesting zero colours triggers a ValueError.
    """
    with pytest.raises(ValueError):
        af_colours("categorical", "hex", 0, config_path=unit_test_config_path)


def test_invalid_high_number_of_colours_value():
    """
    Verify requesting more colours than the palette supports triggers a ValueError.
    """
    with pytest.raises(ValueError):
        af_colours("categorical", "hex", 7, config_path=unit_test_config_path)
