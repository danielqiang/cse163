import re


class Document:
    def __init__(self, fpath: str):
        self._fpath = fpath
        self._counter = self._build_counter(fpath)

    def __repr__(self):
        return f'Document({self._fpath})'

    @staticmethod
    def _build_counter(fpath: str) -> dict:
        """Helper method to initialize internal counter index"""
        with open(fpath) as f:
            tokens = [re.sub(r'\W+', '', token)
                      for token in f.read().split()]
        counter = {}
        for token in tokens:
            if token not in counter:
                counter[token] = 0.
            counter[token] += 1.
        # Remove empty strings
        del counter['']
        return {k: v / len(tokens) for k, v in counter.items()}

    def get_path(self) -> str:
        return self._fpath

    def term_frequency(self, term: str) -> float:
        return self._counter.get(term, 0.)

    def get_words(self) -> list:
        return list(self._counter)
