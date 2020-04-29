import sys

import pytest

from bddcli import Given, given, when, stdout, status, stderr, Application
from textbot import Download


def foo():  # pragma: no cover
    print(' '.join(sys.argv))

app = Application('textbot', 'textbot.cli:Textbot.quickstart')


def test_arguments():
    with Given(app, 'English'):
        assert stdout == 'foo bar\n'
#        assert status == 0

#        when(given - 'download')
#        assert stdout == 'foo\n'

#        when(given + 'English')
#        assert stdout == 'foo bar baz\n'

#    Given without arguments
#    with Given(app):

