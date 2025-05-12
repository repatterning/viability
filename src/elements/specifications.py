"""Module specifications.py"""
import typing

class Specifications(typing.NamedTuple):
    """
    The data type class ⇾ Specifications

    Attributes
    ----------

    """

    station_id: int
    station_name: str
    catchment_id: int
    catchment_name: str
    ts_id: int
    ts_name: str
    starting: str
    until: str
    latitude: float
    longitude: float
    river_name: str
