"""
Token Types

E -> T ('+' | '-' T)*
T -> F ('*' | '/' F)*
F -> integer | '(' E ')'
"""

from enum import Enum

class TokenType(Enum):
    NUMBER = "NUMBER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    STAR = "STAR"
    SLASH = "SLASH"
    OPEN_PARENTHESIS = "OPEN_PARENTHESIS"
    CLOSE_PARENTHESIS = "CLOSE_PARENTHESIS"
    END_OF_FILE = "END_OF_FILE"

class Token:
    def __init__(self, token_type: TokenType, literal: str = "") -> None:
        self.type = token_type
        self.literal = literal

    def __repr__(self) -> str:
        return f"Token(type={self.type.name}, literal={self.literal})"