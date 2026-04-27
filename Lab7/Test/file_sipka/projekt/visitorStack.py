from PLC_Lab8_exprVisitor import PLC_Lab8_exprVisitor
from PLC_Lab8_exprParser import PLC_Lab8_exprParser
from symbol_table import SymbolTable

class VisitorStack(PLC_Lab8_exprVisitor):

    def __init__(self, types):
        self.symbols = SymbolTable()
        self.types = types
        self.code = []
        self.label_id = -1

    def new_label(self):
        self.label_id += 1
        return self.label_id

   
   
    def _handle_itof(self, left_ctx, right_ctx):
        left_t = self.types[left_ctx]
        right_t = self.types[right_ctx]
        
       
       
        self.visit(left_ctx)
        if left_t == "int" and right_t == "float":
            self.code.append("itof")
            
       
        self.visit(right_ctx)
        if left_t == "float" and right_t == "int":
            self.code.append("itof")
            
        return left_t, right_t

  
    def visitFileDeclaration(self, ctx):
       pass
       
       
    
    def visitFopen(self, ctx):
        string = ctx.STRING().getText()

        self.code.append(f"push S {string}")
        self.code.append("fopen")

        name = ctx.VARIABLE().getText()
        self.code.append(f"save {name}")
       
    
    def visitAddingFile(self, ctx):
        name = ctx.VARIABLE().getText()
        self.code.append(f"load {name}")
        
        for expr in ctx.expr():
            self.visit(expr)
            self.code.append("fappend")
        self.code.append("pop")

    def visitProgram(self, ctx):
        return self.visitChildren(ctx)

    def visitDeclaration(self, ctx):
        var_type = ctx.primitiveType().getText()
        for var in ctx.VARIABLE():
            name = var.getText()
            self.symbols[name] = var_type
            if var_type == "int":
                self.code.append("push I 0")
            elif var_type == "float":
                self.code.append("push F 0.0")
            elif var_type == "string":
                self.code.append('push S ""')
            else:
                self.code.append("push B false")
            self.code.append(f"save {name}")

    def visitExpression(self, ctx):
        self.visit(ctx.expr())
        self.code.append("pop")

    def visitRead(self, ctx):
        for var in ctx.VARIABLE():
            name = var.getText()
            t = self.symbols[name]
            mapping = {"int": "I", "float": "F", "string": "S", "bool": "B"}
            self.code.append(f"read {mapping[t]}")
            self.code.append(f"save {name}")

    def visitWrite(self, ctx):
        for expr in ctx.expr():
            self.visit(expr)
        self.code.append(f"print {len(ctx.expr())}")

    def visitBlock(self, ctx):
        self.symbols.enter_scope()
        self.visitChildren(ctx)
        self.symbols.exit_scope()

    def visitIfStatement(self, ctx):
        else_label = self.new_label()
        end_label = self.new_label()

        self.visit(ctx.expr())
        self.code.append(f"fjmp {else_label}")

        self.visit(ctx.statement(0))
        self.code.append(f"jmp {end_label}") 
        self.code.append(f"label {else_label}")

        if ctx.statement(1): 
            self.visit(ctx.statement(1))
        
        self.code.append(f"label {end_label}")

    def visitWhileStatement(self, ctx):
        start_label = self.new_label()
        end_label = self.new_label()

        self.code.append(f"label {start_label}")
        self.visit(ctx.expr())
        self.code.append(f"fjmp {end_label}")
        
        self.visit(ctx.statement())
        
        self.code.append(f"jmp {start_label}")
        self.code.append(f"label {end_label}")

   

    def visitAssignment(self, ctx):
        name = ctx.VARIABLE().getText()
        var_type = self.symbols[name]
        
        
        self.visit(ctx.expr()) 
        
        expr_type = self.types[ctx.expr()]
        if var_type == "float" and expr_type == "int":
            self.code.append("itof")
            
        # vrchol zasobniku ulozit
        self.code.append(f"save {name}")
        
        #pro a=b=1
        self.code.append(f"load {name}")

    def visitAddExpr(self, ctx):
        if ctx.DOT():
            self.visit(ctx.expr(0))
            self.visit(ctx.expr(1))
            self.code.append("concat")
            return

        l_t, r_t = self._handle_itof(ctx.expr(0), ctx.expr(1))
        t = "F" if "float" in (l_t, r_t) else "I"
        op = "add" if ctx.ADD() else "sub"
        self.code.append(f"{op} {t}")

    def visitMulExpr(self, ctx):
        if ctx.MOD():
            self.visit(ctx.expr(0))
            self.visit(ctx.expr(1))
            self.code.append("mod")
            return

        l_t, r_t = self._handle_itof(ctx.expr(0), ctx.expr(1))
        t = "F" if "float" in (l_t, r_t) else "I"
        op = "mul" if ctx.MUL() else "div"
        self.code.append(f"{op} {t}")

    def visitRelExpr(self, ctx):
        l_t, r_t = self._handle_itof(ctx.expr(0), ctx.expr(1))
        t = "F" if "float" in (l_t, r_t) else "I"
        op = "gt" if ctx.GT() else "lt"
        self.code.append(f"{op} {t}")

    def visitEqExpr(self, ctx):
        l_t, r_t = self._handle_itof(ctx.expr(0), ctx.expr(1))
        t = "F" if "float" in (l_t, r_t) else "I" if l_t != "string" else "S"
        self.code.append(f"eq {t}")
        if ctx.NEQ():
            self.code.append("not")

    def visitVarExpr(self, ctx):
        name = ctx.VARIABLE().getText()
        self.code.append(f"load {name}")

    def visitLiteralExpr(self, ctx):
        text = ctx.getText()
        lit = ctx.literal()
        if lit.INT():
            self.code.append(f"push I {text}")
        elif lit.FLOAT():
            self.code.append(f"push F {text}")
        elif lit.BOOL():
            self.code.append(f"push B {text}")
        else:
            self.code.append(f"push S {text}")

    def visitUnaryMinus(self, ctx):
        self.visit(ctx.expr())
        t = self.types[ctx.expr()]
        self.code.append(f"uminus {'F' if t == 'float' else 'I'}")

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitOrExpr(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.code.append("or")

    def visitAndExpr(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.code.append("and")

    def visitNotExpr(self, ctx):
        self.visit(ctx.expr())
        self.code.append("not")