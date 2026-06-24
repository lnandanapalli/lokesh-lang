from Expr import Expr, NumberLiteral, Binary
from Token import Token, TokenType


class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current_position: int = 0

    def parse(self) -> Expr:
        expression: Expr = self._parse_expression()
        self._consume(TokenType.END_OF_FILE, "Expected EOF to terminate the program")
        return expression

    def _parse_expression(self) -> Expr:
        working_expression: Expr = self._parse_term()
        while self._match(TokenType.PLUS, TokenType.MINUS):
            operator: Token = self._previous()
            parsed_term: Expr = self._parse_term()
            working_expression = Binary(working_expression, operator, parsed_term)
        return working_expression

    def _parse_term(self) -> Expr:
        working_expression: Expr = self._parse_factor()
        while self._match(TokenType.STAR, TokenType.SLASH):
            operator: Token = self._previous()
            parsed_factor: Expr = self._parse_factor()
            working_expression = Binary(working_expression, operator, parsed_factor)
        return working_expression

    def _parse_factor(self) -> Expr:
        if self._match(TokenType.NUMBER):
            return NumberLiteral(int(self._previous().literal))
        if self._match(TokenType.OPEN_PARENTHESIS):
            parsed_expression: Expr = self._parse_expression()
            self._consume(TokenType.CLOSE_PARENTHESIS, "Failed to parse a factor, Expected ) following (")
            return parsed_expression
        raise ValueError("Unable to parse a factor, Expected a number or open parenthesis")

    def _peek(self) -> Token:
        return self.tokens[self.current_position]

    def _is_at_end(self) -> bool:
        return self._peek().type == TokenType.END_OF_FILE

    def _previous(self) -> Token:
        return self.tokens[self.current_position - 1]

    def _advance(self) -> Token:
        if not self._is_at_end():
            self.current_position += 1
        return self._previous()

    def _check(self, type_of_token: TokenType) -> bool:
        return self._peek().type == type_of_token

    def _consume(self, type_of_token: TokenType, message: str) -> Token:
        if self._check(type_of_token):
            return self._advance()
        raise ValueError(message)

    def _match(self, *token_types: TokenType) -> bool:
        for type_of_token in token_types:
            if self._check(type_of_token):
                self._advance()
                return True
        return False