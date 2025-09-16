# Expose main public API for the package
from .models import DictFieldRedacter
from .utils import __sanitize__ as strict_sanitize, __loose_sanitize__ as loose_sanitize

# Expose help as a top-level import
help = DictFieldRedacter.help

__all__ = [
    "DictFieldRedacter",
    "strict_sanitize",
    "loose_sanitize",
    "help"
]