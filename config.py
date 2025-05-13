"""config.py"""
import datetime
import logging
import os


class Config:
    """
    Config
    """

    def __init__(self) -> None:
        """
        Constructor<br>
        -----------<br>

        Variables denoting a path - including or excluding a filename - have an underscore suffix; this suffix is
        excluded for names such as warehouse, storage, depository, etc.<br><br>
        """

        now = datetime.datetime.now()
        self.stamp = now.strftime('%Y-%m-%d')
        logging.info(self.stamp)

        # Directories
        self.data_ = os.path.join(os.getcwd(), 'data')
        self.warehouse = os.path.join(os.getcwd(), 'warehouse')

        self.variational_ = os.path.join(self.warehouse, 'variational')
        self.points_ = os.path.join(self.variational_, 'points')
        self.menu_ = os.path.join(self.variational_, 'menu')

        # The model assets section
        self.origin = 'assets' + '/' + 'variational' + '/' + self.stamp

        # Keys, etc
        self.s3_parameters_key = 's3_parameters.yaml'
        self.metadata_ = 'external/metadata/variational'

        sections = ['warehouse', 'variational']
        self.prefix = '/'.join(sections)
