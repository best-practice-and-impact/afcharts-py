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

# Path to the colour configuration YAML file
unit_test_config_path = "../src/afcharts/config/af_colours.yaml"


@pytest.mark.parametrize(
    "palette, colour_format, number_of_colours, config_path",
    [
        # Test categorical palette for length boundaries (1–6 supported values)
        ("categorical", "hex", 1, unit_test_config_path),
        ("categorical", "hex", 2, unit_test_config_path),
        ("categorical", "hex", 3, unit_test_config_path),
        ("categorical", "hex", 4, unit_test_config_path),
        ("categorical", "hex", 5, unit_test_config_path),
        ("categorical", "hex", 6, unit_test_config_path),
    ],
)
def test_categorical_list_length(
    palette, colour_format, number_of_colours, config_path
):
    """
    Ensure the categorical palette returns exactly the requested number of colours.

    For each input combination (palette, format, N colours),
    verify that the resulting colour list length equals `number_of_colours`.
    """
    result = af_colours(palette, colour_format, number_of_colours, config_path)
    assert len(result) == number_of_colours, (
        f"Expected {number_of_colours} colours but got {len(result)} for "
        f"palette='{palette}', format='{colour_format}'"
    )
