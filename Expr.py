from Token import Token


class Expr:
    def __init__(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}()"

class NumberLiteral(Expr):
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value: int = value

    def __repr__(self):
        return f"NumberLiteral(value={self.value})"

class Binary(Expr):
    def __init__(self, left: Expr, operator: Token, right: Expr) -> None:
        super().__init__()
        self.left: Expr = left
        self.operator: Token = operator
        self.right: Expr = right

    def __repr__(self):
        return f"Binary(left={self.left}, operator={self.operator}, right={self.right})"