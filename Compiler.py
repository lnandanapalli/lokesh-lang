from Expr import Expr, NumberLiteral, Binary, Variable
from Instruction import Instruction, PushInt, StoreLocal, LoadLocal
from Stmt import Stmt, ExpressionStmt, VarDeclaration, VarUpdate
from Token import Token, TokenType


class Compiler:
    def __init__(self, should_log: bool = True):
        self.should_log = should_log
        self._next_unique_number: int = 1
        self.locals: dict[str, int] = {}
        self.next_local_slot: int = 0

    def _log(self, stmt: str):
        if self.should_log:
            print(stmt)

    def compile(self, statements: list[Stmt]) -> list[Instruction]:
        self._log("Top level compile function called")
        instructions: list[Instruction] = []
        for statement in statements:
            self._emit_stmt(statement, instructions)
        return instructions

    def _emit_stmt(self, stmt: Stmt, instructions: list[Instruction]):
        if isinstance(stmt, ExpressionStmt):
            self._emit(stmt.expression, instructions)
        elif isinstance(stmt, VarDeclaration):
            if stmt.name in self.locals:
                raise ValueError("Duplicate definition of variable detected")
            else:
                self._emit(stmt.initializer, instructions)
                slot: int = self.next_local_slot
                self.next_local_slot += 1
                self.locals[stmt.name] = slot
                instructions.append(StoreLocal(slot))
        elif isinstance(stmt, VarUpdate):
            slot: int = self.locals[stmt.name]
            if slot is None:
                raise ValueError(f"Failed to update a variable with {stmt.name} as name before declaration")
            self._emit(stmt.value, instructions)
            instructions.append(StoreLocal(slot))


    def _emit(self, expr: Expr, instructions: list[Instruction]):
        log_id = self._next_unique_number
        self._next_unique_number += 1

        if isinstance(expr, NumberLiteral):
            self._log(f"[{log_id}] Emit called with number literal {expr.value}")
            instructions.append(PushInt(expr.value))
        elif isinstance(expr, Binary):
            self._log(f"[{log_id}] Emit called with binary expression {expr}")
            self._log(f"[{log_id}] Recursing on the left side")
            self._emit(expr.left, instructions)
            self._log(f"[{log_id}] Recursing on the right side")
            self._emit(expr.right, instructions)
            self._log(f"[{log_id}] Now adding binary operator {self._instruction_for_operator(expr.operator)}")
            instructions.append(self._instruction_for_operator(expr.operator))
        elif isinstance(expr, Variable):
            slot: int | None = self.locals[expr.name]
            if slot is None:
                raise ValueError(f"Referencing an undefined variable {expr.name}")
            instructions.append(LoadLocal(slot))


    @staticmethod
    def _instruction_for_operator(operator: Token) -> Instruction:
        match operator.type:
            case TokenType.PLUS:
                return Instruction.Add
            case TokenType.MINUS:
                return Instruction.Sub
            case TokenType.STAR:
                return Instruction.Mul
            case TokenType.SLASH:
                return Instruction.Div
            case TokenType.LESS_THAN:
                return Instruction.LessThan
            case TokenType.GREATER_THAN:
                return Instruction.GreaterThan
            case _:
                raise ValueError(f"Unsupported operator {operator}")
