"""
Token Types

E -> T ('+' | '-' T)*
T -> F ('*' | '/' F)*
F -> integer | '(' E ')'
"""

from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    NUMBER = "NUMBER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    STAR = "STAR"
    SLASH = "SLASH"
    OPEN_PARENTHESIS = "OPEN_PARENTHESIS"
    CLOSE_PARENTHESIS = "CLOSE_PARENTHESIS"
    END_OF_FILE = "END_OF_FILE"

@dataclass()
class Token:
    type: TokenType
    literal: str = ""