"""
Lexer
"""
from Token import TokenType, Token


class Lexer:
    def __init__(self, input_string: str) -> None:
        self.input = input_string
        self.tokens: list[Token] = []
        self.current_position: int = 0

    def _advance(self) -> str:
        current_char: str = self.input[self.current_position]
        self.current_position += 1
        return current_char

    def _is_end(self) -> bool:
        return self.current_position >= len(self.input)

    def _scan_number(self) -> None:
        number_start: int = self.current_position - 1
        while self._peek().isdigit():
            self._advance()
        self.tokens.append(Token(TokenType.NUMBER, self.input[number_start:self.current_position]))

    def _peek(self) -> str:
        if self._is_end():
            return "EOF"
        return self.input[self.current_position]

    def _scan_next_token(self) -> None:
        current_char: str = self._advance()
        if current_char == "(":
            self.tokens.append(Token(TokenType.OPEN_PARENTHESIS))
        elif current_char == ")":
            self.tokens.append(Token(TokenType.CLOSE_PARENTHESIS))
        elif current_char == "+":
            self.tokens.append(Token(TokenType.PLUS))
        elif current_char == "-":
            self.tokens.append(Token(TokenType.MINUS))
        elif current_char == "*":
            self.tokens.append(Token(TokenType.STAR))
        elif current_char == "/":
            self.tokens.append(Token(TokenType.SLASH))
        elif current_char.isdigit():
            self._scan_number()
        elif current_char.isspace():
            # Whitespace Ignored
            pass
        else:
            raise ValueError(f"Unexpected token '{current_char}'")

    def scan_tokens(self) -> list[Token]:
        while not self._is_end():
            self._scan_next_token()
        self.tokens.append(Token(TokenType.END_OF_FILE))
        return self.tokens