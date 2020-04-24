from textbot import SpellChecker


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
    checker = SpellChecker(DB)
    assert checker.check('bar') == ['bar', 'baz']
    assert checker.check('qux') == ['qux', 'quux', 'quuz']
