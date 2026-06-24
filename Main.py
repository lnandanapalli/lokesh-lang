from Expr import Expr
from Parser import Parser
from Token import Token
from Lexer import Lexer

source: str = "6 + 4 * 8"
tokens: list[Token] = Lexer(source).scan_tokens()
for token in tokens:
    print(token)

print("===")

expression: Expr = Parser(tokens).parse()
print(expression)