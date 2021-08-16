from packman.lib import inverse_words

def test_inverse_words():
    assert inverse_words('Hello world') == 'olleH dlrow'
    assert inverse_words('hello World') == 'olleh dlroW'