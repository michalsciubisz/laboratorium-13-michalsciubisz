from textblob import TextBlob

def hello(name):
    output = f'Hello {name}'
    return output


def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity


def text_contain_word(word: str, text: str):
    return word in text


def bubble_sort(lst: list):
    '''
    Algorytm sortowania bąbelkowego, zamienia on elementy listy tak aby zwrócić posortowaną listę.
    :param lst: lista która ma zostać posortowana
    :return lst: funkcja zwraca posortowaną listę 
    '''
    if not isinstance(lst, list):
        return None
    n = len(lst)
    for _ in range(n):
        for j in range(n-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst