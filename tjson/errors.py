class TJSONError(Exception):
    """
    Base class for TJSON exceptions.
    """


class EncodingError(TJSONError):
    """
    Invalid string encoding exception.
    """


class ParseError(TJSONError):
    """
    Failure to parse TJSON document.
    """


class DuplicateNameError(TJSONError):
    """
    Duplicate object name.
    """
