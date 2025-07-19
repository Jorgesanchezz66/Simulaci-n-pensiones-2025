import pandas as pd

def cargar_parametros(filepath):
    df = pd.read_csv(filepath)
    parametros = df.set_index("variable")["valor"].to_dict()
    return parametros
