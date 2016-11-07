import json

from .errors import ParseError


__all__ = ('loads', 'dumps', 'ParseError')


def loads(data):
    """
    Parse a TJSON string and return as python objects.
    """
    return json.loads(data)


def dumps(data):
    """
    Generate a TJSON string form a python dict.:
    """
    return json.dumps(data)
