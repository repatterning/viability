
import numpy as np
import pandas as pd

import src.elements.structures as st

class Errors:

    def __init__(self):
        pass

    @staticmethod
    def __get_errors(data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data:
        :return:
        """

        estimates = data[['median', 'lower_w', 'upper_w']].to_numpy()

        data.loc[:, ['error', 'error_l', 'error_u']] = estimates - data['observation'].to_numpy()[:,None]
        data['p_error'] = 100*np.true_divide(data['error'].to_numpy(), data['measure'].to_numpy())

        return data

    def exc(self, structures: st.Structures):

        structures = structures._replace(
            training=self.__get_errors(data=structures.training),
            testing=self.__get_errors(data=structures.testing))

        return structures
