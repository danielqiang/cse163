from cse163_utils import assert_equals

from document import Document
from search_engine import SearchEngine


# This file is left blank for you to fill in with your tests!
def test_document():
    """Tests the Document class"""
    doc = Document('test_search/file.txt')
    assert_equals('test_search/file.txt', doc.get_path())
    assert_equals(['and', 'dog', 'everybody', 'laughed',
                   'licked', 'oil', 'test', 'the'],
                  sorted(doc.get_words()))
    assert_equals(27 / 99, doc.term_frequency('test'))


def test_search_engine():
    """Tests the SearchEngine class"""
    engine = SearchEngine('test_search')
    assert_equals(None, engine.search('asdf'))
    assert_equals(['test_search/file.txt'], engine.search('dog'))
    assert_equals(['test_search/file.txt', 'test_search/file1.txt'],
                  engine.search('test'))


def main():
    test_document()
    test_search_engine()


if __name__ == '__main__':
    main()
