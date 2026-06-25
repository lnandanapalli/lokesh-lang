from Expr import Expr, NumberLiteral, Binary
from Parser import Parser
from Token import Token
from Lexer import Lexer

source: str = "1 + 2 + 3 + 4"
tokens: list[Token] = Lexer(source).scan_tokens()
for token in tokens:
    print(token)

print("===")

expression: Expr = Parser(tokens).parse()

def pretty_print(expr: Expr, indent: int):
    padding: str = "    " * indent
    if isinstance(expr, NumberLiteral):
        print(f"{padding}Number({expr.value})")
    elif isinstance(expr, Binary):
        print(f"{padding}Binary({expr.operator.type})")
        pretty_print(expr.left, indent + 1)
        pretty_print(expr.right, indent + 1)

pretty_print(expression, 0)