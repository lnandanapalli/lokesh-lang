"""
Grammar:

expression -> term ('+' | '-' term)*
term -> factor ('*' | '/' factor)*
factor -> integer | '(' expression ')' | identifier

program -> statement*
statement -> "let" identifier "=" expression ';' | expression ';'
identifier -> [a-z][a-z]*

Start symbol = statement
"""

from Expr import Expr, NumberLiteral, Binary, Variable
from Stmt import Stmt, VarDeclaration, ExpressionStmt
from Token import Token, TokenType


class Parser:
    def __init__(self, tokens: list[Token], should_log: bool = True):
        self.tokens = tokens
        self.current_position: int = 0
        self.should_log = should_log

    def _log(self, stmt: str):
        if self.should_log:
            print(stmt)

    def parse(self) -> list[Stmt]:
        self._log("parse() Top level public parse function called")
        statements: list[Stmt] = []
        while not self._is_at_end():
            statements.append(self._parse_statement())
        self._log("parse() Done parsing expression, verifying EOF exists")
        self._consume(TokenType.END_OF_FILE, "Expected EOF to terminate the program")
        return statements

    def _parse_statement(self):
        if self._match(TokenType.LET):
            return self._parse_var_declaration()
        return self._parse_expression_statement()

    def _parse_var_declaration(self) -> Stmt:
        name: str = self._consume(TokenType.IDENTIFIER, "Expected a name for a variable declaration").literal
        self._consume(TokenType.EQUAL, "Expected equals sign after a variable name")
        initializer: Expr = self._parse_expression()
        self._consume(TokenType.SEMICOLON, "Expected semicolon at the end of statement")
        return VarDeclaration(name, initializer)

    def _parse_expression_statement(self) -> Stmt:
        expression: Expr = self._parse_expression()
        self._consume(TokenType.SEMICOLON, "Expected semicolon at the end of statement")
        return ExpressionStmt(expression)

    def _parse_expression(self) -> Expr:
        self._log("parseExpression() called, will start by parsing term()")
        working_expression: Expr = self._parse_term()
        self._log("parseExpression() done parsing term, now checking for + - Term")
        while self._match(TokenType.PLUS, TokenType.MINUS):
            self._log(f"parseExpression() found a {self._previous()}, will parse term again")
            operator: Token = self._previous()
            parsed_term: Expr = self._parse_term()
            working_expression = Binary(working_expression, operator, parsed_term)
        return working_expression

    def _parse_term(self) -> Expr:
        self._log("parseTerm() called, will start by calling parseFactor()")
        working_expression: Expr = self._parse_factor()
        self._log("parseTerm() done parsing term, now checking for * / Term")
        while self._match(TokenType.STAR, TokenType.SLASH):
            self._log(f"parseTerm() found a {self._previous()}, will parse term again")
            operator: Token = self._previous()
            parsed_factor: Expr = self._parse_factor()
            working_expression = Binary(working_expression, operator, parsed_factor)
        return working_expression

    def _parse_factor(self) -> Expr:
        self._log("parseFactor() called")
        if self._match(TokenType.NUMBER):
            self._log(f"parseFactor() matched a {self._previous()}, will return literal")
            return NumberLiteral(int(self._previous().literal))
        if self._match(TokenType.OPEN_PARENTHESIS):
            self._log("parseFactor() matched an open parenthesis, will parse expression now")
            parsed_expression: Expr = self._parse_expression()
            self._log("parseFactor() done parsing expression, checking for close parenthesis")
            self._consume(TokenType.CLOSE_PARENTHESIS, "Failed to parse a factor, Expected ) following (")
            return parsed_expression
        if self._match(TokenType.IDENTIFIER):
            return Variable(self._previous().literal)
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