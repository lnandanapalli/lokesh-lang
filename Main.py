from Compiler import Compiler
from Expr import Expr, NumberLiteral, Binary
from Instruction import Instruction
from Machine import Machine
from Parser import Parser
from Token import Token
from Lexer import Lexer

source: str = "1 + 2 + 3 + 4"
print(source)

tokens: list[Token] = Lexer(source).scan_tokens()
# for token in tokens:
#     print(token)
print("===")

expression: Expr = Parser(tokens, should_log=False).parse()

def pretty_print(expr: Expr, indent: int):
    padding: str = "    " * indent
    if isinstance(expr, NumberLiteral):
        print(f"{padding}Number({expr.value})")
    elif isinstance(expr, Binary):
        print(f"{padding}Binary({expr.operator.type})")
        pretty_print(expr.left, indent + 1)
        pretty_print(expr.right, indent + 1)

pretty_print(expression, 0)
instructions: list[Instruction] = Compiler(should_log=False).compile(expression)
print("===")
for instruction in instructions:
    print(instruction)

final_stack: list[int] = Machine().run(instructions)
print("===")
print(f"Final stack = {final_stack}")