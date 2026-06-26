from dataclasses import dataclass

class Instruction:
    pass

@dataclass
class PushInt(Instruction):
    value: int

class _Add(Instruction):
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)  # type: ignore
        return cls._instance

class _Sub(Instruction):
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)  # type: ignore
        return cls._instance

class _Mul(Instruction):
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)  # type: ignore
        return cls._instance

class _Div(Instruction):
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)  # type: ignore
        return cls._instance

Instruction.Add = _Add()
Instruction.Sub = _Sub()
Instruction.Mul = _Mul()
Instruction.Div = _Div()