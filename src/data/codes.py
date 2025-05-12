"""Module codes.py"""
import logging
import glob
import os
import pathlib

import config


class Codes:
    """
    <b>Notes</b><br>
    ------<br>
    Determines the institutions list.<br>
    """

    def __init__(self):
        """
        Constructor
        """

        self.__configurations = config.Config()


    @staticmethod
    def __re_cut(string: str) -> str:
        """

        :param string: A path string
        :return:
        """

        string = string.rstrip(os.sep)
        values = string.split(sep=os.sep)

        return values[-2] + os.sep + values[-1]

    def __get_codes(self) -> list[str] | None:
        """

        :return:
        """

        listings = glob.glob(pathname=os.path.join(self.__configurations.data_, '**', '**'))
        logging.info(listings)


        codes = []
        for listing in listings:
            state = (pathlib.Path(os.path.join(listing, 'estimates.csv')).exists() &
                     pathlib.Path(os.path.join(listing, 'training.csv')).exists() &
                     pathlib.Path(os.path.join(listing, 'testing.csv')).exists())
            if state:
                codes.append(os.path.basename(listing))


        return codes

    def exc(self) -> list[str] | None:
        """

        :return:
        """

        return self.__get_codes()
