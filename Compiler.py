from Expr import Expr, NumberLiteral, Binary
from Instruction import Instruction, PushInt
from Token import Token, TokenType


class Compiler:
    def __init__(self, should_log: bool = True):
        self.should_log = should_log
        self._next_unique_number = 1

    def _log(self, stmt: str):
        if self.should_log:
            print(stmt)

    def compile(self, expr: Expr) -> list[Instruction]:
        self._log("Top level compile function called")
        instructions: list[Instruction] = []
        self._emit(expr, instructions)
        return instructions

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
            case _:
                raise ValueError(f"Unsupported operator {operator}")
