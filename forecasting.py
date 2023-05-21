import pandas as pd
import numbers
import statsmodels.api as sm
import matplotlib.pyplot as plt

def transform_variable(df: pd.DataFrame, x: str) -> pd.Series: 
    if isinstance(df[x][0], numbers.Number): 
        print("Hi")
        return df[x]
    else: 
        return pd.Series([i for i in range(len(df[x]))])

def linear_regression(df: pd.DataFrame, x: str, y: str) -> dict[str, float]: 
    fixed_x = transform_variable(df, x)
    model = sm.OLS(df[y], sm.add_constant(fixed_x)).fit()
    print(type(model))
    print(model.summary())
    bands = pd.read_html(model.summary().tables[1].as_html(), header=0, index_col= 0)[0]
    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
    r_2_t = pd.read_html(model.summary().tables[0].as_html(),header=None,index_col=None)[0]

    return {'m': coef.values[1], 'b': coef.values[0], 'r2': r_2_t.values[0][3], 'r2_adj': r_2_t.values[1][3], 'low_band': bands['[0.025'][0], 'hi_band': bands['0.975]'][0]}

def plt_lr(df: pd.DataFrame, x: str, y: str, m: float, b: float, r2: float, r2_adj: float, low_band: float, hi_band: float, colors: tuple[str, str]): 
    fixed_x = transform_variable(df=df, x=x)
    df.plot(x=x, y=y, kind='scatter')
    plt.plot(df[x], [m * x + b for _, x in fixed_x.items()], color=colors[0])
    plt.fill_between(df[x], [m * x + low_band for _, x in fixed_x.items()], [m * x + hi_band for _, x in fixed_x.items()], alpha=0.2, color=colors[1])

def forecasting(): 
    df = pd.read_csv('Dataset/clean_popular_movies.csv')
    df['release_date'] = pd.to_datetime(df['release_date'], infer_datetime_format=True)
    df_by_rev = df.groupby('release_date').aggregate(revenue=pd.NamedAgg(column='revenue', aggfunc=pd.DataFrame.mean))
    df_by_rev.reset_index(inplace=True)

    a = linear_regression(df_by_rev, x='release_date', y='revenue')
    print(a)
    plt_lr(df=df_by_rev, x='release_date', y='revenue', colors=('red', 'orange'), **a)
    plt.show()
    #print(df_by_rev)
    return
 