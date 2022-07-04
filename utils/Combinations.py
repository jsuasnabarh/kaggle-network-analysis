'''
Validate.py
Autor: Joshua Suasnabar
Fecha: Jun 2022
'''

import pandas as pd
import numpy as np
from itertools import combinations

class Combinations():
    '''
    Clase para validar dataframes con valores numericos y categoricos
    '''
    
    def __init__(self):
        self.name = "Combinations"
        
    def create_combinations(df,group_by,name_col_1,name_col_2):
        df_fin = pd.DataFrame([
            [n, x, y]
            for n, g in df.groupby([group_by]).UserId
            for x, y in combinations(g, 2)
        ], columns=[group_by, name_col_1, name_col_2])

        return df_fin