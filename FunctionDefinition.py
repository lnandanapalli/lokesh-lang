from dataclasses import dataclass

from Instruction import Instruction

@dataclass()
class FunctionDefinition:
    name: str
    parameters: list[str]
    instructions: list[Instruction]
