from enum import Enum


class Token(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    EXP = "^"
    MOD = "%"
    NEWL = "\n"
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    FALSE = "false"
    TRUE = "true"
    VOID = "void"
    OR = "||"
    AND = "&&"
    NOT = "!"
    EQ = "=="
    NEQ = "!="
    LEQ = "<="
    GEQ = ">="
    LE = "<"
    GE = ">"
    ASSIGN = "="
    OUT = "out"
    COMMA = ","
    IDENTIFIER = "id"
    FUNC = "func"
    LPAREN = "("
    RPAREN = ")"
    LSQBR = "["
    RSQBR = "]"
    LBRACE = "{"
    RBRACE = "}"
    COLLON = ":"
    RETURN = "return"
    IF = "if"
    ELIF = "elif"
    ELSE = "else"
    FOR = "for"
    IN = "in"
    WHILE = "while"


ARITHMETIC_OPERATIONS = [Token.ADD, Token.SUB, Token.MUL, Token.DIV, Token.EXP, Token.MOD]
ARITHMETIC_OPERATION_VALUES = list(token.value for token in ARITHMETIC_OPERATIONS)
