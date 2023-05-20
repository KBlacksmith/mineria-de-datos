import pandas as pd
from random import randint
from math import inf
import matplotlib.pyplot as plt
from os import path, mkdir

def get_points(df: pd.DataFrame, column_x: str, column_y: str) -> tuple[list, list]: 
    x_values = list()
    y_values = list()

    for x in df.index: 
        if x == 0: 
            continue
        x_values.append(df.loc[x, column_x])
        y_values.append(df.loc[x, column_y])
    return (x_values, y_values)

def get_centroids(k: int, x_values: list, y_values: list): 
    centroids = list()
    size = len(x_values)
    for _ in range(k): 
        idx = randint(0, size - 1)
        c = (x_values[idx], y_values[idx])
        while c in centroids: 
            idx = randint(0, size - 1)
            c = (x_values[idx], y_values[idx])
        centroids.append(c)
    return centroids

def get_distance(centroid: tuple, point: tuple): 
    x = centroid[0] - point[0]
    y = centroid[1] - point[1]
    return (x ** 2 + y ** 2) ** 0.5

def get_new_centroid(cluster: list) -> tuple: 
    x_sum = 0
    y_sum = 0
    for x, y in cluster: 
        x_sum += x
        y_sum += y
    return (x_sum/len(cluster), y_sum / len(cluster))

def cluster_data(df: pd.DataFrame, column_x: str, column_y: str, k = 3):

    img_path = 'img/clusters'
    if not path.exists(img_path): 
        mkdir(img_path)

    x_values, y_values = get_points(df, column_x=column_x, column_y=column_y)
    centroids = get_centroids(k, x_values, y_values)
    
    new_clusters = list()
    old_clusters = None

    while old_clusters != new_clusters: 
        del old_clusters
        distances: list[list] = list()

        old_clusters = new_clusters
        new_clusters = [ [] for c in centroids ]

        for idx in range(len(x_values)): 
            distances.append( [] ) 
            smallest_distance = inf
            smallest_idx = -1
            for c in range(len(centroids)): 
                distances[idx].append(get_distance(centroids[c], (x_values[idx], y_values[idx])))
                if distances[idx][c] < smallest_distance: 
                    smallest_distance = distances[idx][c]
                    smallest_idx = c
                new_clusters[smallest_idx].append((x_values[idx], y_values[idx]))
        centroids = []
        for _ in range(k): 
            centroids.append(get_new_centroid(new_clusters[_]))
    plt.cla()
    for cluster in new_clusters: 
        x_values = []
        y_values = []

        for x, y in cluster: 
            x_values.append(x)
            y_values.append(y)
        plt.scatter(x=x_values, y=y_values)
    plt.title(f'{column_x.upper()} vs. {column_y.upper()}')
    plt.xlabel(f'{column_x.upper()}')
    plt.ylabel(f'{column_y.upper()}')
    plt.savefig(f'{img_path}/{column_x}_vs_{column_y}_clusters.png')
    #print(new_clusters)

def cluster(dataset: str): 
    df: pd.DataFrame = pd.read_csv(f'Dataset/{dataset}')
    cluster_data(df, 'budget', 'revenue')
    cluster_data(df, column_x='runtime', column_y='revenue')
    cluster_data(df, column_x='budget', column_y='popularity')
    cluster_data(df, column_x='budget', column_y='vote_average')