# bibliotecas
import pandas as pd
import datetime

# função para converter as datas
def converter_data(data_str):
    try:
        return pd.to_datetime(data_str, format="%Y-%m-%d %H:%M:%S")
    except ValueError:
        try:
            return pd.to_datetime(data_str, format="%d/%m/%Y")
        except ValueError:
            return pd.NaT
        
# função para converter as horas
def converter_hora(hora_str):
    try:
        return pd.to_datetime(hora_str, format="%H:%M:%S").strftime("%H:%M")
    except ValueError:
        try:
            return pd.to_datetime(hora_str, format="%H:%M").strftime("%H:%M")
        except ValueError:
            return pd.NaT
        