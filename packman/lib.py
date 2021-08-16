def inverse_words(text):
    return ' '.join([word[::-1] for word in text.split()])

if __name__=='__main__':
    print(inverse_words('Hello world'))