import re


class Document:
    def __init__(self, fpath: str):
        """
        Constructs a Document object with a file location
        specified by `fpath`.
        """
        self._fpath = fpath
        self._counter = self._build_counter(fpath)

    def __repr__(self):
        return f'Document({self._fpath})'

    @staticmethod
    def _build_counter(fpath: str) -> dict:
        """Helper method to initialize internal counter index"""
        with open(fpath) as f:
            tokens = [re.sub(r'\W+', '', token).lower()
                      for token in f.read().split()]
        counter = {}
        for token in tokens:
            if token not in counter:
                counter[token] = 0.
            counter[token] += 1 / len(tokens)
        # Remove empty strings
        if '' in counter:
            del counter['']
        return counter

    def get_path(self) -> str:
        """
        Returns the file path of this Document.
        """
        return self._fpath

    def term_frequency(self, term: str) -> float:
        """
        Returns the number of times `term` appears in
        this Document.
        """
        return self._counter.get(term, 0.)

    def get_words(self) -> list:
        """
        Returns a list of all words in this Document.
        """
        return list(self._counter)
