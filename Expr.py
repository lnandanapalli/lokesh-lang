from Token import Token
from dataclasses import dataclass


class Expr:
    pass

@dataclass()
class NumberLiteral(Expr):
    value: int

@dataclass()
class Binary(Expr):
    left: Expr
    operator: Token
    right: Expr