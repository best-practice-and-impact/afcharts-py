# Government Analysis Function (AF) colours and palettes
# Source: https://analysisfunction.civilservice.gov.uk/policy-store/
#   data-visualisation-colours-in-charts/
# Py-af-colours source: https://github.com/best-practice-and-impact/py-af-colours

from pathlib import Path

import yaml


def get_af_colours(
    palette: str, colour_format="hex", number_of_colours=6, config_path=None
):
    """
    get_af_colours() is the top level function in af_colours. This returns
    the chosen Analysis Function colour palette in hex or rgb format.
    For the categorical palette, this can be a chosen number of colours
    up to 6.

    Parameters
    ----------
    palette : string
        Type of palette required, with accepted values of "duo",
        "focus", "categorical", and "sequential".

    colour_format : string, optional
        Colour format required, with accepted values of "hex" or "rgb".

    number_of_colours : int, optional
        Number of colours required (categorical palette only). Takes
        values between 2 and 6. Returns 2 colours by default. If a
        palette other than categorical is chosen, any value passed
        is ignored.

    config_path : NoneType, optional
        Takes the default value None, inside the function this is
        mapped to the relative path independent of operating system.
        Should not require changing.

    Raises
    ------
    ValueError
        If palette is not "categorical", "duo", "sequential", or "focus".
        Or if colour_format is not "hex" or "rgb".

    Returns
    -------
    list
        chosen_colours_list

    """
    if config_path is None:
        parent_dir = Path(__file__).parent
        config_path = parent_dir.joinpath("config", "af_colours.yaml")

    with open(config_path) as file:
        config = yaml.load(file, Loader=yaml.BaseLoader)

    categorical_hex_list = config["categorical_hex_list"]
    duo_hex_list = config["duo_hex_list"]
    sequential_hex_list = config["sequential_hex_list"]
    focus_hex_list = config["focus_hex_list"]

    if palette not in ["categorical", "duo", "sequential", "focus"]:
        raise ValueError(
            "palette must be one of 'categorical', 'duo', 'sequential' " +
            f"or 'focus', not {palette}."
        )
    if colour_format not in ["hex", "rgb"]:
        raise ValueError(
            f"colour_format must be 'hex' or 'rgb', not {colour_format}.")

    if number_of_colours < 1:
        raise ValueError("number_of_colours must be greater than 0.")

    elif palette == "sequential":
        chosen_colours_list = sequential_colours(sequential_hex_list, colour_format)

    elif palette == "focus":
        chosen_colours_list = focus_colours(focus_hex_list, colour_format)

    elif palette == "duo":
        chosen_colours_list = duo_colours(duo_hex_list, colour_format)

    elif palette == "categorical":
        chosen_colours_list = categorical_colours(
            categorical_hex_list, duo_hex_list, colour_format, number_of_colours
        )

    return chosen_colours_list


def categorical_colours(
    categorical_hex_list, duo_hex_list, colour_format="hex", number_of_colours=2
):
    """
    Return the Analysis Function categorical colour palette as a list
    in hex or rgb format for up to 6 colours. If number_of_colours is
    2, the function returns the duo palette.

    Parameters
    ----------
    categorical_hex_list : list
        List of categorical colours as a hex list, stored in the config.

    duo_hex_list : list
        List of duo hex codes, stored in the config. This is needed for the
        case of number_of_colours = 2.

    colour_format : string
        Colour format required, with accepted values of "hex" or "rgb".

    number_of_colours : int
        Number of colours required, with accepted values between 2 and 6
        inclusive. Returns 2 colours if no value given.

    Raises
    ------
    ValueError
        If number_of_colours is greater than 6.

    Returns
    -------
    list
        categorical_colours_list

    """

    if number_of_colours > 6:
        raise ValueError(
            "number_of_colours must not be more than 6 for the categorical palette."
        )

    if number_of_colours == 2:
        categorical_colours_list = duo_colours(duo_hex_list, colour_format)
        return categorical_colours_list

    elif colour_format == "hex":
        full_categorical_colours_list = categorical_hex_list

    elif colour_format == "rgb":
        full_categorical_colours_list = hex_to_rgb(categorical_hex_list)

    else:
        raise ValueError(
            f"colour_format must be 'hex' or 'rgb', not {colour_format}.")

    categorical_colours_list = full_categorical_colours_list[0:number_of_colours]

    return categorical_colours_list


def duo_colours(duo_hex_list, colour_format="hex"):
    """
    Return the Analysis Function duo colour palette as a list of 2
    colours in hex or rgb format. This function is also called by
    sequential_colours() if number_of_colours is equal to 2.

    Parameters
    ----------
    duo_hex_list : list
        List of duo colours hex codes, stored in the config. This is needed for the
        case of number_of_colours = 2.

    colour_format : string
        Colour format required, with accepted values of "hex" or "rgb".

    Returns
    -------
    list
        duo_colours_list

    """

    if colour_format == "hex":
        duo_colours_list = duo_hex_list
    elif colour_format == "rgb":
        duo_colours_list = hex_to_rgb(duo_hex_list)
    else:
        raise ValueError(
            f"colour_format must be 'hex' or 'rgb', not {colour_format}.")

    return duo_colours_list


def sequential_colours(sequential_hex_list, colour_format="hex"):
    """
    Return the Analysis Function sequential colour palette as a list
    of 3 colours in hex or rgb format.

    Parameters
    ----------
    sequential_hex_list : list
        List of sequential colours hex codes, stored in the config.

    colour_format : string
        Colour format required, with accepted values of "hex" or "rgb".

    Returns
    -------
    list
        sequential_colours_list

    """

    if colour_format == "hex":
        sequential_colours_list = sequential_hex_list
    elif colour_format == "rgb":
        sequential_colours_list = hex_to_rgb(sequential_hex_list)
    else:
        raise ValueError(
            f"colour_format must be 'hex' or 'rgb', not {colour_format}.")

    return sequential_colours_list


def focus_colours(focus_hex_list, colour_format="hex"):
    """
    Return the Analysis Function focus colour palette as a list of 2
    colours in hex or rgb format.

    Parameters
    ----------
    focus_hex_list : list
        List of focus colours hex codes, stored in the config.

    colour_format : string
        Colour format required, with accepted values of "hex" or "rgb".

    Returns
    -------
    list
        focus_colours_list

    """

    if colour_format == "hex":
        focus_colours_list = focus_hex_list
    elif colour_format == "rgb":
        focus_colours_list = hex_to_rgb(focus_hex_list)
    else:
        raise ValueError(
            f"colour_format must be 'hex' or 'rgb', not {colour_format}.")

    return focus_colours_list


def hex_to_rgb(hex_colours):
    """
    Convert a list of hex codes to a list of rgb colours.

    Parameters
    ----------
    hex_colours : list
        The hex colours to be converted as a list of strings, with or
        without # at the beginning.

    Raises
    ------
    TypeError
        If hex_colours is not a list.

    Returns
    -------
    list
        converted_list

    """
    if type(hex_colours) is not list:
        raise TypeError("hex_colours must be a list.")

    hex_colours_new = [i.lstrip("#") for i in hex_colours]

    converted_list = [
        (tuple(int(value[i : i + 2], 16) for i in (0, 2, 4)))
        for value in hex_colours_new
    ]
    return converted_list
