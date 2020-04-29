import sys

import pytest
from bddcli import Given, given, when, stdout, status, stderr, Application
from textbot import Download

from textbot import __version__


app = Application('textbot', 'textbot.cli:Textbot.quickstart')



def test_version():
    with Given(app, '--version'):
        assert stdout.startswith(__version__)

