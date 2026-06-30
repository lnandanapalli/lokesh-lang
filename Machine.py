from Instruction import Instruction, PushInt, StoreLocal, LoadLocal


class Machine:
    def __init__(self):
        self.stack: list[int] = []
        self.locals: dict[int, int] = {}

    def run(self, instructions: list[Instruction]) -> list[int]:
        for instruction in instructions:
            self._execute(instruction)
        return list(self.stack)

    def _execute(self, instruction: Instruction):
        if isinstance(instruction, PushInt):
            self.stack.append(instruction.value)
        elif isinstance(instruction, StoreLocal):
            value = self._pop()
            self.locals[instruction.slot] = value
        elif isinstance(instruction, LoadLocal):
            self.stack.append(self.locals[instruction.slot])
        elif instruction is Instruction.Add:
            right = self._pop()
            left = self._pop()
            self.stack.append(left + right)
        elif instruction is Instruction.Sub:
            right = self._pop()
            left = self._pop()
            self.stack.append(left - right)
        elif instruction is Instruction.Mul:
            right = self._pop()
            left = self._pop()
            self.stack.append(left * right)
        elif instruction is Instruction.Div:
            right = self._pop()
            left = self._pop()
            self.stack.append(int(left / right))
        elif instruction is Instruction.LessThan:
            right = self._pop()
            left = self._pop()
            if left < right:
                self.stack.append(1)
            else:
                self.stack.append(0)
        elif instruction is Instruction.GreaterThan:
            right = self._pop()
            left = self._pop()
            if left > right:
                self.stack.append(1)
            else:
                self.stack.append(0)
        else:
            raise ValueError(f"Unsupported instruction {instruction}")

    def _pop(self) -> int:
        if not self.stack:
            raise RuntimeError("Stack underflow")
        return self.stack.pop()