# models.py
# This file contains the DictFieldRedacter class which is responsible for redacting specified fields in a dictionary.
from .utils import __sanitize__, __loose_sanitize__
class DictFieldRedacter():
    """
    A class to redact specified fields in a dictionary by replacing their values with a placeholder.
    Attributes:
        keys_to_hide (list): List of keys whose values need to be redacted.
        placeHolder (str): The placeholder string to replace the redacted values. Default is "Redacted".
    Methods:
        sanitize(data: dict) -> dict: Redacts the specified fields in the provided dictionary.
    """
    def __repr__(self) -> str:
        return f"DictFieldRedacter(keys_to_hide={self.keys_to_hide}, maskWith='{self.maskWith}')"

    def __str__(self) -> str:
        return f"DictFieldRedacter with keys to hide: {self.keys_to_hide} and maskWith: '{self.maskWith}'"

    help = """A class to redact specified fields in a dictionary by replacing their values with a placeholder.
    Attributes:
        keys_to_hide (list): List of keys whose values need to be redacted.
        maskWith (str): The placeholder string to replace the redacted values. Default is "Redacted".
    Methods:
        sanitize(data: dict) -> dict: Redacts the specified fields in the provided dictionary.
        loose_sanitize(data: dict) -> dict: Redacts the specified fields in the provided dictionary using loose matching.
        strict_sanitize(data: dict) -> dict: Redacts the specified fields in the provided dictionary using strict matching.
    Usage:
        
        # 1. Import the class and create an instance for your use case with the fields you want to redact, and the placeholder you want to use.
        from dict_field_redacter import DictFieldRedacter
        redacter = DictFieldRedacter(["secret", "password", "username"], maskWith="***REDACTED***") 
        # 2. Use the instance to redact fields in your dictionary. By default, it uses strict matching, but it's recommended to specify the mode explicitly and choose loose whenever possible.
        redacted_data = redacter.sanitize(data)
        redacted_data_loose = redacter.loose_sanitize(data)
        
    """
    def __init__(self, keys_to_hide:list, maskWith:str = "Redacted") -> None:
        self.keys_to_hide = keys_to_hide
        self.maskWith = maskWith

    def strict_sanitize(self, data:dict) -> dict:
        """
        Redacts the specified fields in the provided dictionary using strict matching.
        """
        return __sanitize__(self.keys_to_hide, data, maskWith=self.maskWith)

    def loose_sanitize(self, data:dict) -> dict:
        """
        Redacts the specified fields in the provided dictionary using loose matching.
        """
        return __loose_sanitize__(self.keys_to_hide, data, maskWith=self.maskWith)

    def sanitize(self, data:dict, mode:str="strict") -> dict:
        """
        Redacts the specified fields in the provided dictionary based on the selected mode.
        Args:
            data (dict): The dictionary to be sanitized.
            mode (str): The mode of sanitization, either "strict" or "loose". Default is "strict".
        Returns:
            dict: The sanitized dictionary.
        """
        if mode not in ["strict", "loose"]:
            raise ValueError("Mode must be either 'strict' or 'loose'")
        if mode == "strict":
            return self.strict_sanitize(data)
        else:
            return self.loose_sanitize(data)
