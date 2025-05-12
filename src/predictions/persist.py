"""Module boundaries.py"""
import json
import os

import pandas as pd

import config
import src.elements.specifications as se
import src.elements.structures as st
import src.functions.objects


class Persist:
    """
    <b>Notes</b><br>
    ------<br>
    This class calculates element errors.<br>
    """

    def __init__(self):
        """
        Constructor
        """

        self.__configurations = config.Config()
        self.__path = os.path.join(self.__configurations.points_, 'predictions')

        self.__objects = src.functions.objects.Objects()


    @staticmethod
    def __get_node(blob: pd.DataFrame) -> dict:
        """

        :param blob:
        :return:
        """

        string: str = blob.to_json(orient='split')

        return json.loads(string)

    def __persist(self, nodes: dict, name: str) -> str:
        """

        :param nodes:
        :param name:
        :return:
        """

        return self.__objects.write(
            nodes=nodes, path=os.path.join(self.__path, f'{name}.json'))

    def exc(self, structures: st.Structures, specifications: se.Specifications) -> str:
        """

        :param structures:
        :param specifications:
        :return:
        """

        nodes = {
            'training': self.__get_node(structures.training),
            'testing': self.__get_node(structures.testing),
            'futures': structures.futures.to_dict(orient='split')}
        nodes.update(specifications._asdict())

        return self.__persist(nodes=nodes, name=str(specifications.ts_id))
