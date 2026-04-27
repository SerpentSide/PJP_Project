# Generated from ./PLC_Lab8_expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PLC_Lab8_exprParser import PLC_Lab8_exprParser
else:
    from PLC_Lab8_exprParser import PLC_Lab8_exprParser

# This class defines a complete generic visitor for a parse tree produced by PLC_Lab8_exprParser.

class PLC_Lab8_exprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PLC_Lab8_exprParser#program.
    def visitProgram(self, ctx:PLC_Lab8_exprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Lab8_exprParser#declaration.
    def visitDeclaration(self, ctx:PLC_Lab8_exprParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Lab8_exprParser#printExpr.
    def visitPrintExpr(self, ctx:PLC_Lab8_exprParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Lab8_exprParser#parens.
    def visitParens(self, ctx:PLC_Lab8_exprParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Lab8_exprParser#assignment.
    def visitAssignment(self, ctx:PLC_Lab8_exprParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Lab8_exprParser#addSub.
    def visitAddSub(self, ctx:PLC_Lab8_exprParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Lab8_exprParser#id.
    def visitId(self, ctx:PLC_Lab8_exprParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Lab8_exprParser#float.
    def visitFloat(self, ctx:PLC_Lab8_exprParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Lab8_exprParser#int.
    def visitInt(self, ctx:PLC_Lab8_exprParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Lab8_exprParser#mulDiv.
    def visitMulDiv(self, ctx:PLC_Lab8_exprParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Lab8_exprParser#primitiveType.
    def visitPrimitiveType(self, ctx:PLC_Lab8_exprParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)



del PLC_Lab8_exprParser