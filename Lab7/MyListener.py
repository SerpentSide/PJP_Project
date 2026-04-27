# Generated from ./PLC_Lab7_expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PLC_Lab7_exprParser import PLC_Lab7_exprParser
else:
    from PLC_Lab7_exprParser import PLC_Lab7_exprParser

# This class defines a complete listener for a parse tree produced by PLC_Lab7_exprParser.
class PLC_Lab7_exprListener(ParseTreeListener):
    def __init__(self):
        self.stack = []

    # Enter a parse tree produced by PLC_Lab7_exprParser#prog.
    def enterProg(self, ctx:PLC_Lab7_exprParser.ProgContext):
        pass

    # Exit a parse tree produced by PLC_Lab7_exprParser#prog.
    def exitProg(self, ctx:PLC_Lab7_exprParser.ProgContext):
        pass


    # Enter a parse tree produced by PLC_Lab7_exprParser#stat.
    def enterStat(self, ctx:PLC_Lab7_exprParser.StatContext):
        pass

    # Exit a parse tree produced by PLC_Lab7_exprParser#stat.
    def exitStat(self, ctx:PLC_Lab7_exprParser.StatContext):
        if(ctx.expr()):
            result = self.stack.pop()
            #print(result)
        pass


    # Enter a parse tree produced by PLC_Lab7_exprParser#oct.
    def enterOct(self, ctx:PLC_Lab7_exprParser.OctContext):
        pass

    # Exit a parse tree produced by PLC_Lab7_exprParser#oct.
    def exitOct(self, ctx:PLC_Lab7_exprParser.OctContext):
        self.stack.append(int(ctx.getText(),8))
        pass


    # Enter a parse tree produced by PLC_Lab7_exprParser#parens.
    def enterParens(self, ctx:PLC_Lab7_exprParser.ParensContext):
        pass

    # Exit a parse tree produced by PLC_Lab7_exprParser#parens.
    def exitParens(self, ctx:PLC_Lab7_exprParser.ParensContext):
        pass


    # Enter a parse tree produced by PLC_Lab7_exprParser#hex.
    def enterHex(self, ctx:PLC_Lab7_exprParser.HexContext):
        pass

    # Exit a parse tree produced by PLC_Lab7_exprParser#hex.
    def exitHex(self, ctx:PLC_Lab7_exprParser.HexContext):
        self.stack.append(int(ctx.getText(),16))
        pass


    # Enter a parse tree produced by PLC_Lab7_exprParser#addSub.
    def enterAddSub(self, ctx:PLC_Lab7_exprParser.AddSubContext):
        pass

    # Exit a parse tree produced by PLC_Lab7_exprParser#addSub.
    def exitAddSub(self, ctx:PLC_Lab7_exprParser.AddSubContext):
        right = self.stack.pop()
        left = self.stack.pop()
        if(ctx.op.text == "+"): self.stack.append(left + right)
        elif(ctx.op.text == "-"): self.stack.append(left - right)
        pass


    # Enter a parse tree produced by PLC_Lab7_exprParser#id.
    def enterId(self, ctx:PLC_Lab7_exprParser.IdContext):
        pass

    # Exit a parse tree produced by PLC_Lab7_exprParser#id.
    def exitId(self, ctx:PLC_Lab7_exprParser.IdContext):
        pass


    # Enter a parse tree produced by PLC_Lab7_exprParser#int.
    def enterInt(self, ctx:PLC_Lab7_exprParser.IntContext):
        pass

    # Exit a parse tree produced by PLC_Lab7_exprParser#int.
    def exitInt(self, ctx:PLC_Lab7_exprParser.IntContext):
        self.stack.append(int(ctx.getText()))
        pass


    # Enter a parse tree produced by PLC_Lab7_exprParser#mulDiv.
    def enterMulDiv(self, ctx:PLC_Lab7_exprParser.MulDivContext):
        pass

    # Exit a parse tree produced by PLC_Lab7_exprParser#mulDiv.
    def exitMulDiv(self, ctx:PLC_Lab7_exprParser.MulDivContext):
        right = self.stack.pop()
        left = self.stack.pop()
        if(ctx.op.text == "*"): self.stack.append(left * right)
        elif(ctx.op.text == "/"):
            if(right != 0): self.stack.append(left / right)
            else: raise Exception("Dividing by zero, dummy.")
        pass



del PLC_Lab7_exprParser