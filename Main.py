from Compiler import Compiler
from Expr import Expr, NumberLiteral, Binary, Variable
from Instruction import Instruction
from Machine import Machine
from Parser import Parser
from Stmt import Stmt, VarDeclaration, ExpressionStmt, VarUpdate
from Token import Token
from Lexer import Lexer

source: str = """
let day = 161;
let month = 6;
update day to 160;
let birthday = day + month;
birthday;
"""
print(source)

tokens: list[Token] = Lexer(source).scan_tokens()
# for token in tokens:
#     print(token)
print("===")

program: list[Stmt] = Parser(tokens, should_log=False).parse()

def pretty_print_stmt(stmt: Stmt, indent: int):
    padding: str = "    " * indent
    if isinstance(stmt, VarDeclaration):
        print(f"{padding}VarDeclaration named {stmt.name}")
        pretty_print_expr(stmt.initializer, indent + 1)
    elif isinstance(stmt, ExpressionStmt):
        print(f"{padding}ExpressionStmt")
        pretty_print_expr(stmt.expression, indent + 1)
    elif isinstance(stmt, VarUpdate):
        print(f"{padding}VarUpdate named {stmt.name}")
        pretty_print_expr(stmt.value, indent + 1)


def pretty_print_expr(expr: Expr, indent: int):
    padding: str = "    " * indent
    if isinstance(expr, NumberLiteral):
        print(f"{padding}Number({expr.value})")
    elif isinstance(expr, Binary):
        print(f"{padding}Binary({expr.operator.type})")
        pretty_print_expr(expr.left, indent + 1)
        pretty_print_expr(expr.right, indent + 1)
    elif isinstance(expr, Variable):
        print(f"{padding}Variable({expr.name})")

for stmt_of_program in program:
    pretty_print_stmt(stmt_of_program, 0)

instructions: list[Instruction] = Compiler(should_log=False).compile(program)
print("===")
for instruction in instructions:
    print(instruction)
final_stack: list[int] = Machine().run(instructions)
print("===")
print(f"Final stack = {final_stack}")
