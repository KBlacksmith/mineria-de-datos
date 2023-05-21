import pingouin as pg
import pandas as pd

df = pd.read_csv('Dataset/clean_popular_movies.csv')

aov = pg.anova(data=df, dv='revenue', between='release_year', detailed=True)
print(aov)