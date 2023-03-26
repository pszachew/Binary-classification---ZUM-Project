import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def categorical_counptlot(data: pd.DataFrame, xy: tuple, colname: str) -> None:
    plt.figure(figsize=(xy[0], xy[1]))
    ax = sns.countplot(x=data[colname].fillna('Missing'))
    plt.show()

def continuous_histplot(data: pd.DataFrame, xy: tuple, colname: str) -> None:
    plt.figure(figsize=(xy[0], xy[1]))
    ax = sns.histplot(x=data[colname])
    plt.show()