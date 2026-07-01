from dataclasses import dataclass
from io import StringIO
from typing import ClassVar

@dataclass()
class Instruction:
    Add: ClassVar["Instruction"]
    Sub: ClassVar["Instruction"]
    Mul: ClassVar["Instruction"]
    Div: ClassVar["Instruction"]
    LessThan: ClassVar["Instruction"]
    GreaterThan: ClassVar["Instruction"]
    Return: ClassVar["Instruction"]

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

class _LessThan(Instruction):
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)  # type: ignore
        return cls._instance

class _GreaterThan(Instruction):
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)  # type: ignore
        return cls._instance

class _Return(Instruction):
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)  # type: ignore
        return cls._instance

Instruction.Add = _Add()
Instruction.Sub = _Sub()
Instruction.Mul = _Mul()
Instruction.Div = _Div()
Instruction.LessThan = _LessThan()
Instruction.GreaterThan = _GreaterThan()
Instruction.Return = _Return()

@dataclass()
class LoadLocal(Instruction):
    slot: int

@dataclass()
class StoreLocal(Instruction):
    slot: int

@dataclass()
class JumpIfFalse(Instruction):
    target: int

@dataclass()
class CallFunction(Instruction):
    name: str
    arity: int