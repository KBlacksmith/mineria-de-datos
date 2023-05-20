from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

def create_wordcloud(column: str): 
    avoided_words = []
    df: pd.DataFrame = pd.read_csv('Dataset/clean_popular_movies.csv')
    words = ""
    for x in df.index: 
        title: str = df.loc[x, column]
        title = title.upper()
        temp_words = title.strip().split(" ")
        words += " ".join(temp_words) + " "
    word_list = words.strip().split(" ")

    #Research purposes
    all_words = ""
    for w in word_list: 
        if w in avoided_words: 
            continue 
        all_words += (w + " ")
    #print(df)
    nube = WordCloud(background_color='white', min_font_size=5).generate(all_words)
    plt.close()
    plt.figure(figsize=(5, 5), facecolor=None)
    plt.imshow(nube)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.title(f'{column.upper()} WORD CLOUD')
    plt.show()
    plt.savefig(f"img/{column}_word_cloud.png")
    plt.close()

def analyze_text(): 
    create_wordcloud('title')
    create_wordcloud('overview')
    create_wordcloud('tagline')