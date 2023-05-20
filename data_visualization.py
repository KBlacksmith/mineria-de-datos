import pandas as pd
import os
import matplotlib.pyplot as plt

def visualize_data(dataset): 
    img_path = 'img/graphs'
    if not os.path.exists(img_path): 
        os.mkdir(img_path)

    df: pd.DataFrame = pd.read_csv(f'Dataset/{dataset}')

    result = df.groupby('release_year')['id'].aggregate('count')
    result.plot(kind='line', xlabel='Año de lanzamiento', ylabel='Cantidad de películas', title='Películas más populares')
    plt.savefig(f"{img_path}/number_of_movies_by_release_year.png")

    plt.cla()
    result = pd.read_csv('Dataset/number_of_movies_by_genre.csv')
    result = result.groupby('genres')['count'].aggregate('sum')
    result.plot(kind='bar', ylabel='Cantidad de Películas', xlabel='Géneros', title='Películas por Géneros')
    plt.savefig(f'{img_path}/number_of_movies_by_genre.png')
    
    plt.cla()
    result = df.groupby('original_language')['id'].aggregate('count')
    result.plot(kind='bar', xlabel='Lenguaje Original', ylabel='Cantidad de Películas', title='Películas por Lenguaje Original')
    plt.savefig(f'{img_path}/movies_by_original_language.png')
    
    plt.cla()
    result = df.groupby('release_month')['id'].aggregate('count')
    result.plot(kind='bar', title='Películas por mes de lanzamiento', xlabel='Mes de Lanzamiento', ylabel='Cantidad de películas')
    plt.savefig(f'{img_path}/movies_by_release_month.png')

    plt.cla()
    result = df.groupby('release_month')['revenue'].aggregate('mean')
    result.plot(kind='bar', title='Ganancias promedio por mes', xlabel='Mes de Lanzamiento', ylabel='Ganancias')
    plt.savefig(f'{img_path}/revenue_by_release_month.png')

    plt.cla()
    result = df.groupby('release_year')['budget'].aggregate('mean')
    result.plot(kind='line', xlabel='Año de Lanzamiento', ylabel='Presupuesto', title='Presupuesto promedio por año')
    plt.savefig(f'{img_path}/average_budget_by_year.png')

    plt.cla()
    result = df.groupby('release_year')['revenue'].aggregate('mean')
    result.plot(kind='line', xlabel='Año de Lanzamiento', ylabel='Ganancias', title='Ganancias promedio por año')
    plt.savefig(f'{img_path}/average_revenue_by_year.png')

    plt.cla()
    result = df.groupby('release_year')['runtime'].aggregate('mean')
    result.plot(kind='line', xlabel='Año de Lanzamiento', ylabel='Duración (minutos)', title='Duración promedio por año')
    plt.savefig(f'{img_path}/average_runtime_by_year.png')

    plt.cla()
    result = df[['popularity', 'vote_average']]
    result.plot(kind='scatter', x='popularity', y='vote_average', xlabel='Índice de Popularidad', ylabel='Calificación promedio', title='Popularidad vs Calificación')
    plt.savefig(f'{img_path}/vote_average_by_popularity_index.png')

    plt.cla()
    result = df[['budget', 'vote_average']]
    result.plot(kind='scatter', x='budget', y='vote_average', xlabel='Presupuesto', ylabel='Calificación Promedio', title='Presupuesto vs Calificación')
    plt.savefig(f'{img_path}/vote_average_vs_budget.png')

    plt.cla()
    df.plot(kind='scatter', x='runtime', y='revenue', title='Duración vs Ganancias', xlabel='Duración (minutos)', ylabel='Ganancias')
    plt.savefig(f'{img_path}/revenue_vs_runtime.png')