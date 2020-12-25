import openpyxl
from openpyxl import load_workbook
import pandas as pd
def process_xlsx(filepath,sheetname):
    wb = load_workbook(filepath)
    ws = wb[sheetname]
    X = []
    Y = []
    for i in ws:
        a = []
        for inn in range(0, len(i)):
            a.append(i[inn].value)
        X.append(a)
    newx = []
    newy = []
    newX = X[2:]
    for i in range(0, len(newX) - 1):
        newx.append(newX[i])
        newy.append(newX[i + 1][0])
    return newx,newy

def regularit(df):
    newDataFrame = pd.DataFrame(index=df.index)
    columns = df.columns.tolist()
    feature_info=[]
    for c in columns:
        d = df[c]
        MAX = d.max()
        MIN = d.min()
        newDataFrame[c] = ((d - MIN) / (MAX - MIN)).tolist()
        feature_info.append([MAX,MIN])
    return newDataFrame,feature_info

def valid_data_scaler(sample,feature_info):
    return [(d - li[1]) / (li[0] - li[1]) for d,li in zip(sample,feature_info)]


