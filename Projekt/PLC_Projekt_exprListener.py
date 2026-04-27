# Generated from ./PLC_Projekt_expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PLC_Projekt_exprParser import PLC_Projekt_exprParser
else:
    from PLC_Projekt_exprParser import PLC_Projekt_exprParser

# This class defines a complete listener for a parse tree produced by PLC_Projekt_exprParser.
class PLC_Projekt_exprListener(ParseTreeListener):

    # Enter a parse tree produced by PLC_Projekt_exprParser#program.
    def enterProgram(self, ctx:PLC_Projekt_exprParser.ProgramContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#program.
    def exitProgram(self, ctx:PLC_Projekt_exprParser.ProgramContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#emptyStmt.
    def enterEmptyStmt(self, ctx:PLC_Projekt_exprParser.EmptyStmtContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#emptyStmt.
    def exitEmptyStmt(self, ctx:PLC_Projekt_exprParser.EmptyStmtContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#declaration.
    def enterDeclaration(self, ctx:PLC_Projekt_exprParser.DeclarationContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#declaration.
    def exitDeclaration(self, ctx:PLC_Projekt_exprParser.DeclarationContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#exprStmt.
    def enterExprStmt(self, ctx:PLC_Projekt_exprParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#exprStmt.
    def exitExprStmt(self, ctx:PLC_Projekt_exprParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#readStmt.
    def enterReadStmt(self, ctx:PLC_Projekt_exprParser.ReadStmtContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#readStmt.
    def exitReadStmt(self, ctx:PLC_Projekt_exprParser.ReadStmtContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#writeStmt.
    def enterWriteStmt(self, ctx:PLC_Projekt_exprParser.WriteStmtContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#writeStmt.
    def exitWriteStmt(self, ctx:PLC_Projekt_exprParser.WriteStmtContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#block.
    def enterBlock(self, ctx:PLC_Projekt_exprParser.BlockContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#block.
    def exitBlock(self, ctx:PLC_Projekt_exprParser.BlockContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#ifStmt.
    def enterIfStmt(self, ctx:PLC_Projekt_exprParser.IfStmtContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#ifStmt.
    def exitIfStmt(self, ctx:PLC_Projekt_exprParser.IfStmtContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#whileStmt.
    def enterWhileStmt(self, ctx:PLC_Projekt_exprParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#whileStmt.
    def exitWhileStmt(self, ctx:PLC_Projekt_exprParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#parens.
    def enterParens(self, ctx:PLC_Projekt_exprParser.ParensContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#parens.
    def exitParens(self, ctx:PLC_Projekt_exprParser.ParensContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#assignment.
    def enterAssignment(self, ctx:PLC_Projekt_exprParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#assignment.
    def exitAssignment(self, ctx:PLC_Projekt_exprParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#orExpr.
    def enterOrExpr(self, ctx:PLC_Projekt_exprParser.OrExprContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#orExpr.
    def exitOrExpr(self, ctx:PLC_Projekt_exprParser.OrExprContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#concat.
    def enterConcat(self, ctx:PLC_Projekt_exprParser.ConcatContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#concat.
    def exitConcat(self, ctx:PLC_Projekt_exprParser.ConcatContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#eqExpr.
    def enterEqExpr(self, ctx:PLC_Projekt_exprParser.EqExprContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#eqExpr.
    def exitEqExpr(self, ctx:PLC_Projekt_exprParser.EqExprContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#notExpr.
    def enterNotExpr(self, ctx:PLC_Projekt_exprParser.NotExprContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#notExpr.
    def exitNotExpr(self, ctx:PLC_Projekt_exprParser.NotExprContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#addExpr.
    def enterAddExpr(self, ctx:PLC_Projekt_exprParser.AddExprContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#addExpr.
    def exitAddExpr(self, ctx:PLC_Projekt_exprParser.AddExprContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#literalExpr.
    def enterLiteralExpr(self, ctx:PLC_Projekt_exprParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#literalExpr.
    def exitLiteralExpr(self, ctx:PLC_Projekt_exprParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#unaryMinus.
    def enterUnaryMinus(self, ctx:PLC_Projekt_exprParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#unaryMinus.
    def exitUnaryMinus(self, ctx:PLC_Projekt_exprParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#mulExpr.
    def enterMulExpr(self, ctx:PLC_Projekt_exprParser.MulExprContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#mulExpr.
    def exitMulExpr(self, ctx:PLC_Projekt_exprParser.MulExprContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#relExpr.
    def enterRelExpr(self, ctx:PLC_Projekt_exprParser.RelExprContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#relExpr.
    def exitRelExpr(self, ctx:PLC_Projekt_exprParser.RelExprContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#idExpr.
    def enterIdExpr(self, ctx:PLC_Projekt_exprParser.IdExprContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#idExpr.
    def exitIdExpr(self, ctx:PLC_Projekt_exprParser.IdExprContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#andExpr.
    def enterAndExpr(self, ctx:PLC_Projekt_exprParser.AndExprContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#andExpr.
    def exitAndExpr(self, ctx:PLC_Projekt_exprParser.AndExprContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#intExpr.
    def enterIntExpr(self, ctx:PLC_Projekt_exprParser.IntExprContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#intExpr.
    def exitIntExpr(self, ctx:PLC_Projekt_exprParser.IntExprContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#floatExpr.
    def enterFloatExpr(self, ctx:PLC_Projekt_exprParser.FloatExprContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#floatExpr.
    def exitFloatExpr(self, ctx:PLC_Projekt_exprParser.FloatExprContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#boolExpr.
    def enterBoolExpr(self, ctx:PLC_Projekt_exprParser.BoolExprContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#boolExpr.
    def exitBoolExpr(self, ctx:PLC_Projekt_exprParser.BoolExprContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#stringExpr.
    def enterStringExpr(self, ctx:PLC_Projekt_exprParser.StringExprContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#stringExpr.
    def exitStringExpr(self, ctx:PLC_Projekt_exprParser.StringExprContext):
        pass


    # Enter a parse tree produced by PLC_Projekt_exprParser#primitiveType.
    def enterPrimitiveType(self, ctx:PLC_Projekt_exprParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by PLC_Projekt_exprParser#primitiveType.
    def exitPrimitiveType(self, ctx:PLC_Projekt_exprParser.PrimitiveTypeContext):
        pass



del PLC_Projekt_exprParser