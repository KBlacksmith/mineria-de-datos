import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt
import seaborn as sns
import matplotlib.pyplot as plt
from os import path, mkdir

def classify(): 
    img_path = "img/classifications"

    if not path.exists(img_path): 
        mkdir(img_path)

    df: pd.DataFrame = pd.read_csv('Dataset/clean_popular_movies.csv')
    df = df.drop(['title', 'release_date', 'genres', 'original_language', 'overview', 'production_companies', 'tagline'], axis=1)
    print(df.columns)
    correlation_matrix = df.corr()
    print(correlation_matrix['budget'])
    print(correlation_matrix['popularity'])

    X = df.drop('budget', axis=1).values

    y = df['budget'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12345)
    knn_model = KNeighborsRegressor(n_neighbors=20)
    knn_model.fit(X_train, y_train)

    train_preds = knn_model.predict(X_train)
    mse = mean_squared_error(y_train, train_preds)
    rmse = sqrt(mse)

    test_preds = knn_model.predict(X_test)
    mse = mean_squared_error(y_test, test_preds)
    rmse = sqrt(mse)

    cmap = sns.cubehelix_palette(as_cmap=True)
    f, ax = plt.subplots()
    points = ax.scatter(X_test[: , 3], X_test[: , 4], c=test_preds, s=50, cmap=cmap)
    f.colorbar(points)
    plt.savefig(f'{img_path}/test_prediction.png')

    cmap = sns.cubehelix_palette(as_cmap=True)
    f, ax = plt.subplots()
    points = ax.scatter(X_test[: , 3], X_test[: , 4], c=y_test, s=50, cmap=cmap)
    f.colorbar(points)
    plt.savefig(f'{img_path}/y_test.png')