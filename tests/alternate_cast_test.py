# -*- coding: utf-8 -*-
import sys
import pytest

import six

def _string(text):
    """For Python2 routines that can only process str type."""
    if sys.version_info[0] == 3:
        if type(text) != str:
            return str(text)
        else:
            return text

    elif sys.version_info[0] == 2:
        if type(text) == str:
            return text

        if type(text) == int:
            return str(text)

        return text.encode("utf-8")

def alternate_cast(string):
    if isinstance(string, str):
        return string
    casted = six.text_type(string)
    if sys.version_info[0] == 2:
        casted = casted.encode("utf-8")
    return casted

@pytest.mark.parametrize('alternate_cast', [alternate_cast])
@pytest.mark.parametrize('string', ['a normal string', u'B\xe9l', u'ééééééé', 'é',
                                    u'é'.encode('utf-8')])
def test_that_string_is_equivalent_to_string_cast(string, alternate_cast):
    try:
        alternate_cast(string)
    except (UnicodeDecodeError, UnicodeEncodeError) as e:
        # Make sure that _string also fails
        with pytest.raises(type(e)):
            _string(string)
        return 
    try:
        _string_result = _string(string)
    except (UnicodeDecodeError, UnicodeEncodeError):
        pass
    else:
        assert _string_result == alternate_cast(string)
