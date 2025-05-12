"""Module src.elements.parts.py"""
import typing

import pandas as pd


class Structures(typing.NamedTuple):
    """
    The data type class ⇾ Structures

    Attributes
    ----------

    """

    training: pd.DataFrame
    testing: pd.DataFrame
    futures: pd.DataFrame
