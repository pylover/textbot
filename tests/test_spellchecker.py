from textbot import spellcheck


DB = [
    'foo',
    'bar',
    'baz',
    'qux',
    'quux',
    'quuz',
    'corge',
    'grault',
    'garply',
    'waldo',
    'fred',
    'xyzzy',
    'thud'
]


def test_correctword():
    assert spellcheck(DB, 'bar') == ['bar', 'baz']
    assert spellcheck(DB, 'qux') == ['qux', 'quux', 'quuz']
