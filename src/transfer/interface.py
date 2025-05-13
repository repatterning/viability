"""Module interface.py"""
import logging

import boto3
import pandas as pd

import config
import src.elements.s3_parameters as s3p
import src.elements.service as sr
import src.s3.ingress
import src.transfer.dictionary
import src.transfer.initial
import src.transfer.metadata


class Interface:
    """
    Class Interface
    """

    def __init__(self, connector: boto3.session.Session, service: sr.Service,  s3_parameters: s3p):
        """

        :param service: A suite of services for interacting with Amazon Web Services.
        :param s3_parameters: The overarching S3 parameters settings of this
                              project, e.g., region code name, buckets, etc.
        """

        self.__service: sr.Service = service
        self.__s3_parameters: s3p.S3Parameters = s3_parameters

        self.__configurations = config.Config()

        # Metadata
        self.__metadata = src.transfer.metadata.Metadata(connector=connector)


        # Instances
        self.__dictionary = src.transfer.dictionary.Dictionary()

    def __get_metadata(self, frame: pd.DataFrame) -> pd.DataFrame:
        """

        :param frame:
        :return:
        """

        _metadata_p = self.__metadata.exc(name='points.json')
        _metadata_m = self.__metadata.exc(name='menu.json')

        frame = frame.assign(
            metadata = frame['section'].apply(
                lambda x: _metadata_p if x == 'points' else _metadata_m))

        return frame

    def exc(self):
        """

        :return:
        """

        # The strings for transferring data to Amazon S3 (Simple Storage Service)
        strings = self.__dictionary.exc(
            path=self.__configurations.variational_, extension='json',
            prefix=self.__configurations.prefix)

        strings = self.__get_metadata(frame=strings.copy())
        logging.info(strings)

        # Prepare the S3 (Simple Storage Service) section
        src.transfer.initial.Initial(
            service=self.__service, s3_parameters=self.__s3_parameters).exc()

        # Transfer
        messages = src.s3.ingress.Ingress(
            service=self.__service, bucket_name=self.__s3_parameters.external).exc(
            strings=strings, tagging='project=hydrography')
        logging.info(messages)
