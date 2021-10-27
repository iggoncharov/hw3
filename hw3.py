class CountVectorizer:
    """
    Класс CountVectorizer, имеющий методы:
    fit_transform - Возвращает список списков где подсчитывается число слов
    в тексте из списка уникальных слов
    get_feature_names - возвращает список уникальных слов из всего корпуса
    """

    def __init__(self, lowercase=True):
        self.lowercase = lowercase
        self._vocabulary = {}

    def get_feature_names(self):
        return list(self._vocabulary.keys())

    def fit_transform(self, corpus):
        if self.lowercase:
            corpus = [text.lower() for text in corpus]

        vocabulary = []
        corpus_list = []
        for text in corpus:
            words = text.split()
            corpus_list.append(words)
            for word in words:
                if word not in vocabulary:
                    vocabulary.append(word)

        self._vocabulary = {word: index for index, word in enumerate(vocabulary)}

        count_matrix = []
        for text in corpus_list:
            text_matrix = [0]*len(self._vocabulary)
            for word in text:
                text_matrix[self._vocabulary[word]] += 1
            count_matrix.append(text_matrix)
        return count_matrix

if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)

    test1 = ['one']
    vectorizer = CountVectorizer()
    assert vectorizer.fit_transform(test1) == [[1]] and vectorizer.get_feature_names() == ['one']

    test2 = []
    vectorizer = CountVectorizer()
    assert vectorizer.fit_transform(test2) == [] and vectorizer.get_feature_names() == []

    test3 = ['one two three', 'one two', 'one']
    vectorizer = CountVectorizer()
    assert vectorizer.fit_transform(test3) == [[1, 1, 1], [1, 1, 0], [1, 0, 0]] and vectorizer.get_feature_names() == ['one', 'two', 'three']
