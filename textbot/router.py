import re

from .agents import EmailAgent


def route(command):
    for pattern, agent in patterns:
        if pattern.match(command):
            return agent


patterns = [
    (
        '^(?P<verb>\w{2,}) (an|a)?(?P<subject>\w+) .* (?P<target>\w+)$',
        EmailAgent
    ),
]
patterns = [(re.compile(p), a) for p, a in patterns]

