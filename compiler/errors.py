from __future__ import annotations
from typing import Tuple, List, TYPE_CHECKING

from compiler.ast.types import *
from compiler.parsing.tokens import Token

if TYPE_CHECKING:
    from compiler.ast.ast import AstNode


def location_str(location: Tuple[int, int]) -> str:
    return f"({location[0] + 1}, {location[1] + 1})"


class SyntaxError(Exception):
    def __init__(self, expected: Token or List[Token], got: str, location: Tuple[int, int]):
        expected_str = " or ".join([str(token) for token in expected]) if type(expected) == list else expected
        self.message = f"At {location_str(location)}: Expected {expected_str} - Got '{got}'"
        super(SyntaxError, self).__init__(self.message)
        

class TypeError(Exception):
    def __init__(self, node: AstNode, expected: Type or List[Type], got: Type):
        expected_str: str = " or ".join(str(token) for token in expected) if type(expected) else expected
        self.message = f"At {location_str(node.location)}: Expected {expected_str} - Got {got}"
        super(TypeError, self).__init__(self.message)


class IdentifierInUseError(Exception):
    def __init__(self, name: str, node: AstNode):
        self.message = f"At {location_str(node.location)}: Identifier '{name}' already in use."
        super(IdentifierInUseError, self).__init__(self.message)


class IdentifierNotDeclaredError(Exception):
    def __init__(self, name: str, node: AstNode):
        self.message = f"At {location_str(node.location)}: Identifier '{name}' has not been declared yet."
        super(IdentifierNotDeclaredError, self).__init__(self.message)


class IdentifierNotAssignedError(Exception):
    def __init__(self, name: str, node: AstNode):
        self.message = f"At {location_str(node.location)}: No value has been assigned to identifier '{name}'."
        super(IdentifierNotAssignedError, self).__init__(self.message)


class FunctionNameInUseError(Exception):
    def __init__(self, name: str, node: AstNode):
        self.message = f"At {location_str(node.location)}: Function name '{name} is in use already."
        super(FunctionNameInUseError, self).__init__(self.message)


class FunctionNotDefinedError(Exception):
    def __init__(self, name: str, node: AstNode):
        self.message = f"At {location_str(node.location)}: Function with name {name} is not defined."
        super(FunctionNotDefinedError, self).__init__(self.message)


class VoidFunctionReturnError(Exception):
    def __init__(self, name: str, node: AstNode):
        self.message = f"At {location_str(node.location)}: Void function {name} should not contain a return statement."
        super(VoidFunctionReturnError, self).__init__(self.message)


class ReturnTypeError(Exception):
    def __init__(self, expected: ReturnType, got: ReturnType, node: AstNode):
        self.message = f"At {location_str(node.location)}: Expected {expected} - Got {got}"
        super(ReturnTypeError, self).__init__(self.message)


class ArgumentCountError(Exception):
    def __init__(self, expected: int, got: int, node: AstNode):
        self.message = f"At {location_str(node.location)}: Expected {expected} - Got {got}"