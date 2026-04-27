from PLC_Lab8_exprListener import PLC_Lab8_exprListener
from symbol_table import SymbolTable

class ListenerType(PLC_Lab8_exprListener):

    def __init__(self):
        self.symbols = SymbolTable()
        self.types = {}

    def enterProgram(self, ctx):
        pass

    def exitProgram(self, ctx):
        pass


    def enterDeclaration(self, ctx):
        pass

    def exitDeclaration(self, ctx):
        dtype = self.types[ctx.primitiveType()]

        for iden in ctx.VARIABLE():
            self.symbols[iden.getText()] = dtype



    def enterEmpty(self, ctx):
        pass

    def exitEmpty(self, ctx):
        pass


    def enterExpression(self, ctx):
        pass

    def exitExpression(self, ctx):
        self.types[ctx] = self.types[ctx.expr()]


    def enterRead(self, ctx):
        pass

    def exitRead(self, ctx):
        for var in ctx.VARIABLE():
            self.symbols[var.getText()]


    def enterWrite(self, ctx):
        pass

    def exitWrite(self, ctx):
        pass

    def enterIndexExpr(self, ctx):
        pass

    # Exit a parse tree produced by PLC_Lab8_exprParser#indexExpr.
    def exitIndexExpr(self, ctx):
        base_t = self.types[ctx.expr(0)]
        idx_t = self.types[ctx.expr(1)]

        if base_t != "string":
            raise TypeError("Indexing only allowed on string")

        if idx_t != "int":
            raise TypeError("Index must be int")

        self.types[ctx] = "char"



    def enterBlock(self, ctx):
        self.symbols.enter_scope()

    def exitBlock(self, ctx):
        self.symbols.exit_scope()


    def enterIfStatement(self, ctx):
       pass
       

    def exitIfStatement(self, ctx):
        if self.types[ctx.expr()] != "bool":
            raise TypeError("Condition in if must be bool")


    def enterWhileStatement(self, ctx):
        pass

    def exitWhileStatement(self, ctx):
        if self.types[ctx.expr()] != "bool":
            raise TypeError("Condition in while must be bool")



    def enterVarExpr(self, ctx):
        pass

    def exitVarExpr(self, ctx):
        name = ctx.VARIABLE().getText()
        t = self.symbols[name]
        self.types[ctx] = t


    def enterParens(self, ctx):
        pass

    def exitParens(self, ctx):
        self.types[ctx] = self.types[ctx.expr()]


    def enterEqExpr(self, ctx):
        pass

    def exitEqExpr(self, ctx):
        left = ctx.expr(0)
        right = ctx.expr(1)

        left_t = self.types[left]
        right_t = self.types[right]

        if left_t in ("int", "float") and right_t in ("int", "float"):
            self.types[ctx] = "bool"
        elif left_t == "string" and right_t == "string":
            self.types[ctx] = "bool"
        else:
            raise TypeError("Invalid types for == or !=")
    


    def enterNotExpr(self, ctx):
        pass

    def exitNotExpr(self, ctx):
        expr_type = self.types[ctx.expr()]

        if expr_type != "bool":
            raise TypeError("Operator ! requires bool")

        self.types[ctx] = "bool"


    def enterAddExpr(self, ctx):
        pass

    def exitAddExpr(self, ctx):
        left = self.types[ctx.expr(0)]
        right = self.types[ctx.expr(1)]

        if ctx.DOT():
            if left == "string" and right == "string":
                self.types[ctx] = "string"
            else:
                raise TypeError("Dot requires string operands")

        else:
            if left in ("int", "float") and right in ("int", "float"):
                if left == "float" or right == "float":
                    self.types[ctx] = "float"
                else:
                    self.types[ctx] = "int"
            else:
                raise TypeError("Invalid types for arithmetic operation")


    def enterAssignment(self, ctx):
        pass

    def exitAssignment(self, ctx):
        var_name = ctx.VARIABLE().getText()
        token = ctx.VARIABLE().symbol

        var_type = self.symbols[var_name]
        expr_type = self.types[ctx.expr()]

        
        if var_type == "float" and expr_type == "int":
            self.types[ctx] = "float"
            return

        
        if var_type == expr_type:
            self.types[ctx] = var_type
            return

      
        
        raise TypeError(f"{token.line}:{token.column} - Cannot assign {expr_type} to {var_type}")


    def enterLiteralExpr(self, ctx):
        pass

    def exitLiteralExpr(self, ctx):
        lit = ctx.literal()

        if lit.INT():
            self.types[ctx] = "int"
        elif lit.FLOAT():
            self.types[ctx] = "float"
        elif lit.BOOL():
            self.types[ctx] = "bool"
        else:
            self.types[ctx] = "string"


    def enterUnaryMinus(self, ctx):
        pass

    def exitUnaryMinus(self, ctx):
        t = self.types[ctx.expr()]

        if t in ("int", "float"):
            self.types[ctx] = t
        else:
            raise TypeError("Unary minus requires int or float")


    def enterMulExpr(self, ctx):
        pass

    def exitMulExpr(self, ctx):
        left = self.types[ctx.expr(0)]
        right = self.types[ctx.expr(1)]

        if ctx.MOD():
            if left == "int" and right == "int":
                self.types[ctx] = "int"
            else:
                raise TypeError("Mod requires integer operands")

        else:
            if left in ("int", "float") and right in ("int", "float"):
                if left == "float" or right == "float":
                    self.types[ctx] = "float"
                else:
                    self.types[ctx] = "int"
            else:
                raise TypeError("Invalid types for arithmetic operation")



    def enterOrExpr(self, ctx):
        pass

    def exitOrExpr(self, ctx):
        left = self.types[ctx.expr(0)]
        right = self.types[ctx.expr(1)]

        if left == "bool" and right == "bool":
            self.types[ctx] = "bool"
        else:
            raise TypeError("Operator || requires bool operands")


    def enterRelExpr(self, ctx):
        pass

    def exitRelExpr(self, ctx):
        left = self.types[ctx.expr(0)]
        right = self.types[ctx.expr(1)]

        if left in ("int", "float") and right in ("int", "float"):
            self.types[ctx] = "bool"
        else:
            raise TypeError("Relational operators require numeric operands")


    def enterAndExpr(self, ctx):
        pass

    def exitAndExpr(self, ctx):
        left = self.types[ctx.expr(0)]
        right = self.types[ctx.expr(1)]

        if left == "bool" and right == "bool":
            self.types[ctx] = "bool"
        else:
            raise TypeError("Operator && requires bool operands")


    def enterLiteral(self, ctx):
        pass

    def exitLiteral(self, ctx):
        pass


    def enterPrimitiveType(self, ctx):
        pass

    def exitPrimitiveType(self, ctx):
        if ctx.INT_KEYWORD():
            self.types[ctx] = "int"
        elif ctx.FLOAT_KEYWORD():
            self.types[ctx] = "float"
        elif ctx.BOOL_KEYWORD():
            self.types[ctx] = "bool"
        elif ctx.CHAR_KEYWORD():
            self.types[ctx] = "char"
        else:
            self.types[ctx] = "string"