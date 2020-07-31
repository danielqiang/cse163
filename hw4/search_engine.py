import os
import math
from document import Document


class SearchEngine:
    def __init__(self, dirname: str):
        """
        Constructs a SearchEngine object using files
        located in directory `dirname` as the search space.
        """
        self._inv_index = self._build_index(dirname)
        self._num_docs = len(os.listdir(dirname))

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
        if term not in self._inv_index:
            return 0
        return math.log(self._num_docs / len(self._inv_index[term]))

    def search(self, query: str):
        """
        Returns all documents in the directory specified in constructor
        containing the string `query`. If `query` is a multi-word
        string, returns all documents containing any word in `query`.
        Results are ranked using TF-IDF (term frequency-inverse
        document frequency) in descending order.

        If no matching documents are found, returns None.
        """
        terms = query.split()
        docs = {doc
                for term in terms
                for doc in self._inv_index.get(term, [])}
        scores = {}
        for doc in docs:
            docname = doc.get_path()
            tf_idf = sum(doc.term_frequency(term) * self._calculate_idf(term)
                         for term in terms)
            scores[docname] = tf_idf
        rankings = sorted(scores, key=scores.get, reverse=True)
        return rankings or None
