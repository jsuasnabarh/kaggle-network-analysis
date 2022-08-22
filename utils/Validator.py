'''
Validate.py
Autor: Joshua Suasnabar
Fecha: Jun 2022
'''

import pandas as pd
import numpy as np

class Validator():
    '''
    Clase para validar dataframes con valores numericos y categoricos
    '''

    def __init__(self):
        self.name = "Validator"

    def validar_numerico(df,list_cols):
        df_final = pd.DataFrame()
        for col in list_cols:
            #Calculo de columnas
            n = df.shape[0]
            missing = df[col].isnull().sum()
            missing_percent = df[col].isnull().sum()/df.shape[0]*100
            negativo = df[df[col]<0][col].count()
            negativo_percent =negativo/df.shape[0]*100
            unico = df[col].nunique()
            media = df[col].mean()
            std = df[col].std()
            minimo = df[col].min()
            maximo = df[col].max()
            #Cuantiles
            Q1 = df[col].quantile(.25)
            Q3 = df[col].quantile(.75)
            IQR = Q3 - Q1
            min_bp = Q1 - 1.5 * IQR
            max_bp = Q3 + 1.5 * IQR
            #Percentiles
            P10 = df[col].quantile(.1)
            P25 = df[col].quantile(.25)
            P50 = df[col].quantile(.5)
            P75 = df[col].quantile(.75)
            P90 = df[col].quantile(.9)
            P95 = df[col].quantile(.95)
            P99 = df[col].quantile(.99)
            IQRMAX = max_bp
            _3SDMAX = media+3*std


            OUT_IQR = np.where((df[col]< min_bp) | (df[col]> max_bp),1,0).sum()
            OUT_IQR_percent = OUT_IQR/df.shape[0]*100

            OUT_3SD = np.where((df[col]> _3SDMAX),1,0).sum()
            OUT_3SD_percent = OUT_3SD/df.shape[0]*100

            OUT_P90 = np.where((df[col]> P90),1,0).sum()
            OUT_P90_percent = OUT_P90/df.shape[0]*100

            OUT_P95 = np.where((df[col]> P95),1,0).sum()
            OUT_P95_percent = OUT_P95/df.shape[0]*100

            OUT_P99 = np.where((df[col]> P99),1,0).sum()
            OUT_P99_percent = OUT_P99/df.shape[0]*100

            valores = [[col,
                        n,+
                        missing,missing_percent,
                        negativo,negativo_percent,
                        unico,
                        media,minimo,maximo,
                        IQRMAX,
                        _3SDMAX,
                        P10,
                        P25,
                        P50,
                        P75,
                        P90,
                        P95,
                        P99,
                        OUT_IQR,
                        OUT_IQR_percent,
                        OUT_3SD,
                        OUT_3SD_percent,
                        OUT_P90,
                        OUT_P90_percent,
                        OUT_P95,
                        OUT_P95_percent,
                        OUT_P99,
                        OUT_P99_percent
                        ]]
            
            nombres = ["Variable",
                    "n",
                    "Missing","%Missing",
                    "Negativo","%Negativo",
                    "Unico",
                    "Media","Min","Max",
                    "IQRMAX",
                    "3STD",
                    "P10",
                    "P25",
                    "P50",
                    "P75",
                    "P90",
                    "P95",
                    "P99",
                    "Outlier IQR",
                    "%Outlier IQR",
                    "Outlier 3SD",
                    "%Outlier 3SD",
                    "Outlier P90",
                    "%Outlier P90",
                    "Outlier P95",
                    "%Outlier P95",
                    "Outlier P99",
                    "%Outlier P99"
                    ]
            tabla = pd.DataFrame(valores,columns=nombres)
            df_final = df_final.append(tabla)

        df_final = df_final.round(decimals =2)
        return df_final

    def validar_categorico(df,list_cols):
        df_final = pd.DataFrame()
        for col in list_cols:
            #Calculo de columnas
            n = df.shape[0]
            missing = df[col].isnull().sum()
            missing_percent = df[col].isnull().sum()/df.shape[0]*100
            unico = df[col].nunique()

            valores = [[col,
                        n,
                        missing,missing_percent,
                        unico
                        ]]

            nombres = ["Variable",
                    "n",
                    "Missing","%Missing",
                    "Unico"
                    ]
            tabla = pd.DataFrame(valores,columns=nombres)
            df_final = df_final.append(tabla)

        df_final = df_final.round(decimals =2)
        return df_final