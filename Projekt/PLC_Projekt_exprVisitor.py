# Generated from ./PLC_Projekt_expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PLC_Projekt_exprParser import PLC_Projekt_exprParser
else:
    from PLC_Projekt_exprParser import PLC_Projekt_exprParser

# This class defines a complete generic visitor for a parse tree produced by PLC_Projekt_exprParser.

class PLC_Projekt_exprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PLC_Projekt_exprParser#program.
    def visitProgram(self, ctx:PLC_Projekt_exprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#emptyStmt.
    def visitEmptyStmt(self, ctx:PLC_Projekt_exprParser.EmptyStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#declaration.
    def visitDeclaration(self, ctx:PLC_Projekt_exprParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#exprStmt.
    def visitExprStmt(self, ctx:PLC_Projekt_exprParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#readStmt.
    def visitReadStmt(self, ctx:PLC_Projekt_exprParser.ReadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#writeStmt.
    def visitWriteStmt(self, ctx:PLC_Projekt_exprParser.WriteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#block.
    def visitBlock(self, ctx:PLC_Projekt_exprParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#ifStmt.
    def visitIfStmt(self, ctx:PLC_Projekt_exprParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#whileStmt.
    def visitWhileStmt(self, ctx:PLC_Projekt_exprParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#parens.
    def visitParens(self, ctx:PLC_Projekt_exprParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#assignment.
    def visitAssignment(self, ctx:PLC_Projekt_exprParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#orExpr.
    def visitOrExpr(self, ctx:PLC_Projekt_exprParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#concat.
    def visitConcat(self, ctx:PLC_Projekt_exprParser.ConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#eqExpr.
    def visitEqExpr(self, ctx:PLC_Projekt_exprParser.EqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#notExpr.
    def visitNotExpr(self, ctx:PLC_Projekt_exprParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#addExpr.
    def visitAddExpr(self, ctx:PLC_Projekt_exprParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#literalExpr.
    def visitLiteralExpr(self, ctx:PLC_Projekt_exprParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#unaryMinus.
    def visitUnaryMinus(self, ctx:PLC_Projekt_exprParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#mulExpr.
    def visitMulExpr(self, ctx:PLC_Projekt_exprParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#relExpr.
    def visitRelExpr(self, ctx:PLC_Projekt_exprParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#idExpr.
    def visitIdExpr(self, ctx:PLC_Projekt_exprParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#andExpr.
    def visitAndExpr(self, ctx:PLC_Projekt_exprParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#intExpr.
    def visitIntExpr(self, ctx:PLC_Projekt_exprParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#floatExpr.
    def visitFloatExpr(self, ctx:PLC_Projekt_exprParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#boolExpr.
    def visitBoolExpr(self, ctx:PLC_Projekt_exprParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#stringExpr.
    def visitStringExpr(self, ctx:PLC_Projekt_exprParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Projekt_exprParser#primitiveType.
    def visitPrimitiveType(self, ctx:PLC_Projekt_exprParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)



del PLC_Projekt_exprParser