import os
import math
from document import Document


class SearchEngine:
    def __init__(self, dirname: str):
        self._index = self._build_index(dirname)
        self._docs = len(os.listdir(dirname))

    @staticmethod
    def _build_index(dirname: str) -> dict:
        """Helper method to initialize inverted index"""
        inv_index = {}
        for fname in os.listdir(dirname):
            if fname.startswith('.'):
                continue
            doc = Document(f'{dirname}/{fname}')
            for word in doc.get_words():
                if word not in inv_index:
                    inv_index[word] = []
                inv_index[word].append(doc)
        return inv_index

    def _calculate_idf(self, term: str) -> float:
        if term not in self._index:
            return 0
        return math.log(self._docs / len(self._index[term]))

    def search(self, query: str):
        terms = query.split()
        docs = {doc
                for term in terms
                for doc in self._index.get(term, [])}
        scores = {}
        for doc in docs:
            docname = doc.get_path()
            tf_idf = sum(doc.term_frequency(term) * self._calculate_idf(term)
                         for term in terms)
            scores[docname] = tf_idf
        rankings = sorted(scores, key=scores.get, reverse=True)
        return rankings or None


from pprint import pprint

engine = SearchEngine('small_wiki')
pprint(engine.search('asdf'))
# print('a'.split())
