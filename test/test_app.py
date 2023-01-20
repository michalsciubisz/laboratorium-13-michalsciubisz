from app import hello
from app import extract_sentiment
from app import text_contain_word
from app import bubble_sort
import pytest


def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want


testdata1 = ["I think today will be a great day"]

@pytest.mark.parametrize('sample', testdata1)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0


testdata2 = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]

@pytest.mark.parametrize('sample, word, expected_output', testdata2)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output


#5 przypadków wykorzystanych do sprawdzenia działania algorytmu

result = [
    ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
    ([102, 23, 424, 13, 244, 323, 103], [13, 23, 102, 103, 244, 323, 424]),
    ([25, 82, 34, 46, 42, 89, 57, 1, 85, 36, 30, 79, 12, 12, 44, 36, 5, 82, 46, 32, 9, 60, 71, 71, 55, 28, 96, 67, 12, 33, 88, 45, 2, 68, 73, 12, 92, 28, 78, 15], 
    [1, 2, 5, 9, 12, 12, 12, 12, 15, 25, 28, 28, 30, 32, 33, 34, 36, 36, 42, 44, 45, 46, 46, 55, 57, 60, 67, 68, 71, 71, 73, 78, 79, 82, 82, 85, 88, 89, 92, 96]),
    ([111, 127, 198, 137, 229, 136, 196, 184, 211, 226, 157, 245, 188, 133, 158, 154, 208, 105, 124, 190],
    [105, 111, 124, 127, 133, 136, 137, 154, 157, 158, 184, 188, 190, 196, 198, 208, 211, 226, 229, 245]),
    ([1, 2, 1, 1, 2, 2, 2, 1, 1, 2], [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]),
    ('String', None),
    ((1,23,52,1,4), None)
    ]

@pytest.mark.parametrize('sample, expected_output', result)
def test_bubble_sort(sample, expected_output):

    assert bubble_sort(sample) == expected_output        