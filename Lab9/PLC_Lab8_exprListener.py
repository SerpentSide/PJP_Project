# Generated from ./PLC_Lab8_expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PLC_Lab8_exprParser import PLC_Lab8_exprParser
else:
    from PLC_Lab8_exprParser import PLC_Lab8_exprParser

from VM import run_vm
from SymbolTable import SymbolTable

# This class defines a complete listener for a parse tree produced by PLC_Lab8_exprParser.
class PLC_Lab8_exprListener(ParseTreeListener):
    def __init__(self):
        self.memory = SymbolTable()
        self.code = []
    # Enter a parse tree produced by PLC_Lab8_exprParser#program.
    def enterProgram(self, ctx:PLC_Lab8_exprParser.ProgramContext):
        pass

    # Exit a parse tree produced by PLC_Lab8_exprParser#program.
    def exitProgram(self, ctx:PLC_Lab8_exprParser.ProgramContext):
        #for str in self.code:
        #    print(str)
        print("run_vm")
        run_vm(self.code)
        pass


    # Enter a parse tree produced by PLC_Lab8_exprParser#declaration.
    def enterDeclaration(self, ctx:PLC_Lab8_exprParser.DeclarationContext):
        pass

    # Exit a parse tree produced by PLC_Lab8_exprParser#declaration.
    def exitDeclaration(self, ctx:PLC_Lab8_exprParser.DeclarationContext):
        var_type = ctx.primitiveType().type

        for identifier in ctx.IDENTIFIER():
            name = identifier.getText()
            self.memory[name] = var_type

            if var_type == "int":
                self.code.append("PUSH I 0")
                self.code.append(f"SAVE I {name}")
            else:
                self.code.append("PUSH F 0")
                self.code.append(f"SAVE F {name}")

        pass


    # Enter a parse tree produced by PLC_Lab8_exprParser#printExpr.
    def enterPrintExpr(self, ctx:PLC_Lab8_exprParser.PrintExprContext):
        pass

    # Exit a parse tree produced by PLC_Lab8_exprParser#printExpr.
    def exitPrintExpr(self, ctx:PLC_Lab8_exprParser.PrintExprContext):
        ctx.type = ctx.expr().type
        #print(ctx.expr().type)
        var_type = ctx.expr().type
        if var_type == "int":
            self.code.append("PRINT I")
        elif var_type == "float":
            self.code.append("PRINT F")
        pass


    # Enter a parse tree produced by PLC_Lab8_exprParser#parens.
    def enterParens(self, ctx:PLC_Lab8_exprParser.ParensContext):
        pass

    # Exit a parse tree produced by PLC_Lab8_exprParser#parens.
    def exitParens(self, ctx:PLC_Lab8_exprParser.ParensContext):
        ctx.type = ctx.expr().type
        pass


    # Enter a parse tree produced by PLC_Lab8_exprParser#assignment.
    def enterAssignment(self, ctx:PLC_Lab8_exprParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PLC_Lab8_exprParser#assignment.
    def exitAssignment(self, ctx:PLC_Lab8_exprParser.AssignmentContext):
        name = ctx.IDENTIFIER().getText()

        var_type = self.memory[name]
        expr_type = ctx.expr().type

        if var_type == "error" or expr_type == "error":
            ctx.type = "error"
            return

        if var_type == "int" and expr_type == "float":
            print(f"Type error: '{name}' is int but assigned float")
            ctx.type = "error"
            return
        else:
            if var_type == "int":
                self.code.append(f"SAVE I {name}")
            else:
                self.code.append(f"SAVE F {name}")
            self.code.append(f"LOAD {name}")
            ctx.type = var_type
        pass


    # Enter a parse tree produced by PLC_Lab8_exprParser#addSub.
    def enterAddSub(self, ctx:PLC_Lab8_exprParser.AddSubContext):
        pass

    # Exit a parse tree produced by PLC_Lab8_exprParser#addSub.
    def exitAddSub(self, ctx:PLC_Lab8_exprParser.AddSubContext):
        left = ctx.expr(0).type
        right = ctx.expr(1).type
        op_type = ctx.op.type
        if left == "error" or right == "error":
            print(f"Error {left} or {right} value not suitable")
            ctx.type = "error"
            return
        if left == "float" or right == "float":
            ctx.type = "float"
        else:
            ctx.type = "int"
        if op_type == ctx.parser.ADD:
            self.code.append("ADD")
        else:
            self.code.append("SUB")
        pass


    # Enter a parse tree produced by PLC_Lab8_exprParser#id.
    def enterId(self, ctx:PLC_Lab8_exprParser.IdContext):
        pass

    # Exit a parse tree produced by PLC_Lab8_exprParser#id.
    def exitId(self, ctx:PLC_Lab8_exprParser.IdContext):
        name = ctx.IDENTIFIER().getText()
        if name not in self.memory:
            print(f"Error variable {name} not declared")
            ctx.type = "error"
        else:
            ctx.type = self.memory[name]
            self.code.append(f"LOAD {name}")
        pass


    # Enter a parse tree produced by PLC_Lab8_exprParser#float.
    def enterFloat(self, ctx:PLC_Lab8_exprParser.FloatContext):
        pass

    # Exit a parse tree produced by PLC_Lab8_exprParser#float.
    def exitFloat(self, ctx:PLC_Lab8_exprParser.FloatContext):
        ctx.type = "float"
        self.code.append(f"PUSH F {ctx.getText()}")
        pass


    # Enter a parse tree produced by PLC_Lab8_exprParser#int.
    def enterInt(self, ctx:PLC_Lab8_exprParser.IntContext):
        pass

    # Exit a parse tree produced by PLC_Lab8_exprParser#int.
    def exitInt(self, ctx:PLC_Lab8_exprParser.IntContext):
        ctx.type = "int"
        self.code.append(f"PUSH I {ctx.getText()}")
        pass


    # Enter a parse tree produced by PLC_Lab8_exprParser#mulDiv.
    def enterMulDiv(self, ctx:PLC_Lab8_exprParser.MulDivContext):
        pass

    # Exit a parse tree produced by PLC_Lab8_exprParser#mulDiv.
    def exitMulDiv(self, ctx:PLC_Lab8_exprParser.MulDivContext):
        left = ctx.expr(0).type
        right = ctx.expr(1).type
        op_type = ctx.op.type
        if left == "error" or right == "error":
            print(f"Error {left} or {right} value not suitable")
            ctx.type = "error"
            return
        if op_type == ctx.parser.MOD:
            if left == "float" or right == "float":
                print(f"Error MOD only viable for int")
                ctx.type = "error"
                return
        if left == "float" or right == "float":
            ctx.type = "float"
        else:
            ctx.type = "int"

        if op_type == ctx.parser.MUL:
            self.code.append("MUL")
        elif op_type == ctx.parser.DIV:
            self.code.append("DIV")
        else:
            self.code.append("MOD")
        pass


    # Enter a parse tree produced by PLC_Lab8_exprParser#primitiveType.
    def enterPrimitiveType(self, ctx:PLC_Lab8_exprParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by PLC_Lab8_exprParser#primitiveType.
    def exitPrimitiveType(self, ctx:PLC_Lab8_exprParser.PrimitiveTypeContext):
        if ctx.getText() == "int":
            ctx.type = "int"
        elif ctx.getText() == "float":
            ctx.type = "float"
        else:
            ctx.type = "error"
        pass



del PLC_Lab8_exprParser