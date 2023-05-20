import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

def regress_line(dataset: str): 
    df: pd.DataFrame = pd.read_csv(f'Dataset/{dataset}')
    X = df.iloc[:, 0].values.reshape(-1, 1)
    Y = df.iloc[:, 1].values.reshape(-1, 1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    Y_pred = linear_regressor.predict(X)
    plt.cla()
    plt.scatter(X, Y)
    plt.plot(X, Y_pred, color='red')
    plt.show()

def get_linear_regressions(): 
    regress_line('releases_by_year.csv')