from dataclasses import dataclass

from Expr import Expr


class Stmt:
    pass

@dataclass()
class VarDeclaration(Stmt):
    name: str
    initializer: Expr

@dataclass()
class ExpressionStmt(Stmt):
    expression: Expr

@dataclass()
class VarUpdate(Stmt):
    name: str
    value: Expr

@dataclass()
class IfStmt(Stmt):
    condition: Expr
    body: list[Stmt]