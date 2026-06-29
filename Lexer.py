from Token import TokenType, Token

class EOF:
    pass

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
        peek_result = self._peek()
        while not isinstance(peek_result, EOF) and peek_result.isdigit():
            self._advance()
            peek_result = self._peek()
        self.tokens.append(Token(TokenType.NUMBER, self.input[number_start:self.current_position]))

    def _scan_identifier(self):
        identifier_start: int = self.current_position - 1
        peek_result = self._peek()
        while not isinstance(peek_result, EOF) and peek_result.isalpha():
            self._advance()
            peek_result = self._peek()
        literal = self.input[identifier_start:self.current_position]
        if literal == "let":
            self.tokens.append(Token(TokenType.LET))
        elif literal == "update":
            self.tokens.append(Token(TokenType.UPDATE))
        elif literal == "to":
            self.tokens.append(Token(TokenType.TO))
        else:
            self.tokens.append(Token(TokenType.IDENTIFIER, literal))

    def _peek(self) -> EOF | str:
        if self._is_end():
            return EOF()
        return self.input[self.current_position]

    def _scan_next_token(self) -> None:
        current_char: str = self._advance()
        if current_char == "=":
            self.tokens.append(Token(TokenType.EQUAL))
        elif current_char == ";":
            self.tokens.append(Token(TokenType.SEMICOLON))
        elif current_char == "(":
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
        elif current_char.isalpha():
            self._scan_identifier()
        else:
            raise ValueError(f"Unexpected token '{current_char}'")

    def scan_tokens(self) -> list[Token]:
        while not self._is_end():
            self._scan_next_token()
        self.tokens.append(Token(TokenType.END_OF_FILE))
        return self.tokens