"""
Token Types

E -> E + T
E -> E - T
E -> T

T -> T * F
T -> T / F
T -> F

F -> integer
F -> (E)
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

class Token:
    def __init__(self, token_type: TokenType, literal: str = "") -> None:
        self.type = token_type
        self.literal = literal

    def __repr__(self) -> str:
        return f"Token({self.type.name}, {self.literal})" if self.literal else f"Token({self.type.name})"