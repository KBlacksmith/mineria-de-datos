import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from os import path, mkdir

def regress_line_from_csv(df): 
    result = df['']
    X = df.iloc[:, 0].values.reshape(-1, 1)
    Y = df.iloc[:, 1].values.reshape(-1, 1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    Y_pred = linear_regressor.predict(X)
    plt.cla()
    plt.scatter(X, Y)
    plt.plot(X, Y_pred, color='red')
    plt.show()

def regress_line(df: pd.DataFrame, x_axis: str, y_axis: str, agg_func = ''): 

    img_path = 'img/linear_regressions'
    if not path.exists(img_path): 
        mkdir(img_path)

    if agg_func != '': 
        result = df.groupby(x_axis)[y_axis].aggregate(agg_func)

        X = np.array(result.keys()).reshape(-1, 1)
        Y = np.array(result.values).reshape(-1, 1)
    else: 
        X = np.array(df[x_axis].values).reshape(-1, 1)
        Y = np.array(df[y_axis].values).reshape(-1, 1)

    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    Y_pred = linear_regressor.predict(X)
    plt.cla()
    plt.scatter(X, Y)
    plt.plot(X, Y_pred, color='red')
    plt.xlabel(xlabel=x_axis.upper())
    plt.ylabel(ylabel=y_axis.upper())
    plt.title(label=x_axis.upper() + " vs. " + y_axis.upper())
    plt.savefig(f'{img_path}/{x_axis}_vs_{y_axis}.png')

def get_linear_regressions(): 
    df: pd.DataFrame = pd.read_csv('Dataset/clean_popular_movies.csv')
    regress_line(df, x_axis='release_year', y_axis='id', agg_func='count')
    regress_line(df, x_axis='release_year', y_axis='budget', agg_func='mean')
    regress_line(df, x_axis='release_year', y_axis='revenue', agg_func='mean')
    regress_line(df, x_axis='release_year', y_axis='runtime', agg_func='mean')
    regress_line(df, x_axis='budget', y_axis='revenue')
    regress_line(df, x_axis='runtime', y_axis='revenue')
    regress_line(df, x_axis='budget', y_axis='popularity')
    regress_line(df, x_axis='budget', y_axis='vote_average')
    regress_line(df, x_axis='vote_average', y_axis='popularity')
    return
    #regress_line_from_csv('releases_by_year.csv')
    df: pd.DataFrame = pd.read_csv('Dataset/clean_popular_movies.csv')
    
    #Releases by year
    result = df.groupby('release_year')['id'].aggregate('count')
    #print(result.keys())
    X = np.array(result.keys()).reshape(-1, 1)
    #print(result.values)
    Y = np.array(result.values).reshape(-1, 1)

    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    Y_pred = linear_regressor.predict(X)
    plt.cla()
    plt.scatter(X, Y)
    plt.plot(X, Y_pred, color='red')
    plt.show()
    return
    regress_line_from_df('clean_popular_movies.csv', x_axis='release_year', y_axis='idx')