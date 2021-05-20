import wikipedia
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt


def create_wc(text):
    stop_words = set(STOPWORDS)
    wc = WordCloud(background_color="white",max_words=100,stopwords=stop_words)
    wc.generate(text)
    plt.imshow(wc, interpolation= 'bilinear')
    plt.axis('off')
    plt.show()

def get_wiki(title):
    title = wikipedia.search(title)[0]
    page = wikipedia.page(title)
    return page.content


create_wc(get_wiki("Java"))
