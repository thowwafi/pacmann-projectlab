import pandas as pd
import os


SN13_KRT_PATH = './data/susenas13/sn13_krt.csv'
COLUMNS = ['urut', 'b1r1', 'b1r5', 'b8r1', 'b8r1', 'b8r2a', 'b8r2b', 'b8r2c', 'b8r3a', 'b8r3b', 'b9r1a', 'b9r1al', 'b9r1b', 'exp_cap', 'wert']
def get_dataframe(path):
    return pd.read_csv(path)


if __name__ == '__main__':
    df_sn13_krt = get_dataframe(SN13_KRT_PATH)
    df_raw = df_sn13_krt[COLUMNS]
