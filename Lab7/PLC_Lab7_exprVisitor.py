# Generated from ./PLC_Lab7_expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PLC_Lab7_exprParser import PLC_Lab7_exprParser
else:
    from PLC_Lab7_exprParser import PLC_Lab7_exprParser

# This class defines a complete generic visitor for a parse tree produced by PLC_Lab7_exprParser.

class PLC_Lab7_exprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PLC_Lab7_exprParser#prog.
    def visitProg(self, ctx:PLC_Lab7_exprParser.ProgContext):
        results = []
        for stat in ctx.stat():
            result = self.visit(stat)
            results.append(result)
            #print(result)
        return results


    # Visit a parse tree produced by PLC_Lab7_exprParser#stat.
    def visitStat(self, ctx:PLC_Lab7_exprParser.StatContext):
        if ctx.expr() and ctx.ID() is None:
            return self.visit(ctx.expr())
        return None


    # Visit a parse tree produced by PLC_Lab7_exprParser#oct.
    def visitOct(self, ctx:PLC_Lab7_exprParser.OctContext):
        return int(ctx.getText(),8)


    # Visit a parse tree produced by PLC_Lab7_exprParser#parens.
    def visitParens(self, ctx:PLC_Lab7_exprParser.ParensContext):
        return self.visit(ctx.expr())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Lab7_exprParser#hex.
    def visitHex(self, ctx:PLC_Lab7_exprParser.HexContext):
        return int(ctx.getText(),16)

    # Visit a parse tree produced by PLC_Lab7_exprParser#addSub.
    def visitAddSub(self, ctx:PLC_Lab7_exprParser.AddSubContext):
        left = self.visit(ctx.expr()[0])
        right = self.visit(ctx.expr()[1])
        #print(ctx.op.text)
        if(ctx.op.text == "+"): return left + right
        elif(ctx.op.text == "-"):
            return left - right
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Lab7_exprParser#id.
    def visitId(self, ctx:PLC_Lab7_exprParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Lab7_exprParser#int.
    def visitInt(self, ctx:PLC_Lab7_exprParser.IntContext):
        return int(ctx.getText())


    # Visit a parse tree produced by PLC_Lab7_exprParser#mulDiv.
    def visitMulDiv(self, ctx:PLC_Lab7_exprParser.MulDivContext):
        left = self.visit(ctx.expr()[0])
        right = self.visit(ctx.expr()[1])
        #print(ctx.op.text)
        if(ctx.op.text == "*"): return left * right
        elif(ctx.op.text == "/"):
            if right != 0: return left / right
            else: raise Exception("Zero divison dummy.")



del PLC_Lab7_exprParser