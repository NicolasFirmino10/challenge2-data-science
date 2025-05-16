import pandas as pd

def extrair_dados():
    df = pd.read_json('../data/TelecomX_Data.json')
    return df

def transformar_dados(df):
    # Exemplo: limpar dados, preencher valores ausentes, etc
    df = df.dropna()
    return df
