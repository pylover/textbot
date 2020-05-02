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
    'thud',
    'pippo',
    'pluto',
    'paperino'
]


def test_correctword():
    checker = SpellChecker(DB)
    assert checker.check('bar') == ['bar', 'baz']
    assert checker.check('qux') == ['qux', 'quux', 'quuz'] 
    assert checker.check('walfo') == ['waldo']
    assert checker.check('thid') == ['thud']
    assert checker.check('corge') == ['corge']
    assert checker.check('baz') == ['bar', 'baz']
    assert checker.check('gsrlpy') == ['garply']


