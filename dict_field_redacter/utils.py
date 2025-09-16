# utils.py
# This file contains utility functions for the project.
# Here is the method that parse through the dict and replace the matched key's value with the placeholder
def __sanitize__(keys_to_hide, data:dict, maskWith:str="Redacted") -> dict:
    """
    A function to redact specified fields in a dictionary by replacing their values with a placeholder.
    Args:
        keys_to_hide (list): List of keys whose values need to be redacted.
        data (dict): The dictionary to be sanitized.
    Returns:
        dict: The sanitized dictionary.
    """
    for i in data:
        # what about nested dict ?
        if i in keys_to_hide and isinstance(data[i], (str, int, float, bool)):
            data[i] = maskWith
        elif isinstance(data[i], dict):
            data[i] = __sanitize__(keys_to_hide, data[i], maskWith=maskWith)
    return data

def __loose_sanitize__(keys_to_hide, data:dict, maskWith:str = "Redacted") -> dict:
    """
    A function to redact specified fields in a dictionary by replacing their values with a placeholder.
    Args:
        keys_to_hide (list): List of keys whose values need to be redacted.
        data (dict): The dictionary to be sanitized.
    Returns:
        dict: The sanitized dictionary.
    """
    for i in data:
        # what about nested dict ?
        if any(key in i.lower() for key in keys_to_hide) and isinstance(data[i], (str, int, float, bool)):
            data[i] = maskWith
        elif isinstance(data[i], dict):
            data[i] = __loose_sanitize__(keys_to_hide, data[i], maskWith=maskWith)
    return data
# print(__sanitize__(["secret", "password", "username"], {"username": "user1", "password": "pass123", "details": {"age": 30, "location": "USA"}}))