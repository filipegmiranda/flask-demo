import json

"""
This module groups together functions that operate and analyse Strings, and JSON objects
that contain palindromes
"""


def palindromes_in_json_keys(jsons, key="key"):
    """Returns a list with all palindromes found in the list of jsons checking if the json
    property in the `key` argument is a palindrome, the default is key
    :param key: str
    :type jsons: list
    """
    key_values = map(lambda s: _extract_json_value(s, key), jsons)
    key_values = filter(lambda v: v is not None, key_values)
    return list(filter(is_palindrome, key_values))


def count_palindromes(jsons, key="key"):
    """Counts and returns the count of palindrome strings
    found in the values of the json properties defined in the key argument, the default
    is to analyse the json property 'key'
    :rtype: int
        """
    return len(palindromes_in_json_keys(jsons, key))


def is_palindrome(string):
    """Return true if `string` is a palindrome, false otherwise
        :rtype: bool
        """
    return string.lower() == _reverse_string(string).lower()


def _extract_json_value(json_doc, key):
    """Extracts the value of a json string from the property defined in key argument
    :rtype: str
            """
    doc = json.loads(json_doc)
    return doc.get(key)


def _reverse_string(string):
    """Return a reversed copy of `string`
    :rtype: string
    """
    return string[::-1]
