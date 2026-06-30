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
    LET = "LET"
    IDENTIFIER = "IDENTIFIER"
    EQUAL = "EQUAL"
    SEMICOLON = "SEMICOLON"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"
    OPEN_BRACE = "OPEN_BRACE"
    CLOSE_BRACE = "CLOSE_BRACE"
    IF = "IF"

@dataclass()
class Token:
    type: TokenType
    literal: str = ""