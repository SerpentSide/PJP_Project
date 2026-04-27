from PLC_Projekt_exprVisitor import PLC_Projekt_exprVisitor

class CompilerVisitor(PLC_Projekt_exprVisitor):
    def __init__(self):
        self.code = []
        self.symbol_table = {}
        self.label_counter = 0

    def get_new_label(self):
        self.label_counter += 1
        return self.label_counter

    def visitProgram(self, ctx):
        for st in ctx.statement():
            self.visit(st)
        return self.code

    def visitIfStmt(self, ctx):
        l_else = self.get_new_label()
        l_end = self.get_new_label()
        self.visit(ctx.condition)
        self.code.append(f"fjmp {l_else}")
        self.visit(ctx.trueStmt)
        self.code.append(f"jmp {l_end}")
        self.code.append(f"label {l_else}")
        if ctx.falseStmt:
            self.visit(ctx.falseStmt)
        self.code.append(f"label {l_end}")

    def visitWhileStmt(self, ctx):
        l_start = self.get_new_label()
        l_end = self.get_new_label()
        self.code.append(f"label {l_start}")
        self.visit(ctx.condition)
        self.code.append(f"fjmp {l_end}")
        self.visit(ctx.statement())
        self.code.append(f"jmp {l_start}")
        self.code.append(f"label {l_end}")

    def visitBlock(self, ctx):
        for st in ctx.statement():
            self.visit(st)

    def visitDeclaration(self, ctx):
        typ_str = ctx.primitiveType().getText()
        typ_map = {"int": "I", "float": "F", "string": "S", "bool": "B"}
        t = typ_map[typ_str]
        default_val = {"int": "0", "float": "0.0", "string": '""', "bool": "false"}
        for var in ctx.IDENTIFIER():
            name = var.getText()
            self.symbol_table[name] = typ_str
            self.code.append(f"push {t} {default_val[typ_str]}")
            self.code.append(f"save {name}")

    def visitWriteStmt(self, ctx):
        for e in ctx.expr():
            self.visit(e)
        self.code.append(f"print {len(ctx.expr())}")

    def visitReadStmt(self, ctx):
        for var in ctx.IDENTIFIER():
            name = var.getText()
            typ = self.symbol_table[name]
            t = "I" if typ == "int" else "F" if typ == "float" else "S" if typ == "string" else "B"
            self.code.append(f"read {t}")
            self.code.append(f"save {name}")

    def visitAssignment(self, ctx):
        name = ctx.IDENTIFIER().getText()
        var_type = self.symbol_table[name]
        rhs_type = self.visit(ctx.expr())
        if var_type == "float" and rhs_type == "int":
            self.code.append("itof")
        self.code.append(f"save {name}")
        self.code.append(f"load {name}")
        return var_type

    def visitAddExpr(self, ctx):
        left_type = self.visit(ctx.expr(0))
        idx_after_left = len(self.code) 
        right_type = self.visit(ctx.expr(1))
        op = "add" if ctx.op.text == "+" else "sub"
        if left_type == "int" and right_type == "int":
            self.code.append(f"{op} I")
            return "int"
        elif left_type == "float" and right_type == "float":
            self.code.append(f"{op} F")
            return "float"
        else:
            if left_type == "int":
                rhs_code = self.code[idx_after_left:]
                self.code = self.code[:idx_after_left] + ["itof"] + rhs_code
            else:
                self.code.append("itof")
            self.code.append(f"{op} F")
            return "float"

    def visitMulExpr(self, ctx):
        left_type = self.visit(ctx.expr(0))
        idx_after_left = len(self.code)
        right_type = self.visit(ctx.expr(1))
        op_text = ctx.op.text
        op = "mul" if op_text == "*" else "div" if op_text == "/" else "mod"
        if op == "mod":
            self.code.append("mod")
            return "int"
        if left_type == "int" and right_type == "int":
            self.code.append(f"{op} I")
            return "int"
        elif left_type == "float" and right_type == "float":
            self.code.append(f"{op} F")
            return "float"
        else:
            if left_type == "int":
                rhs_code = self.code[idx_after_left:]
                self.code = self.code[:idx_after_left] + ["itof"] + rhs_code
            else:
                self.code.append("itof")
            self.code.append(f"{op} F")
            return "float"

    def visitRelExpr(self, ctx):
        left_type = self.visit(ctx.expr(0))
        idx_after_left = len(self.code)
        right_type = self.visit(ctx.expr(1))
        op = "lt" if ctx.op.text == "<" else "gt"
        if left_type == "float" or right_type == "float":
            if left_type == "int":
                rhs_code = self.code[idx_after_left:]
                self.code = self.code[:idx_after_left] + ["itof"] + rhs_code
            elif right_type == "int":
                self.code.append("itof")
            self.code.append(f"{op} F")
        else:
            self.code.append(f"{op} I")
        return "bool"

    def visitEqExpr(self, ctx):
        t1 = self.visit(ctx.expr(0))
        t2 = self.visit(ctx.expr(1))
        s = "S" if t1 == "string" else "F" if (t1 == "float" or t2 == "float") else "I"
        self.code.append(f"eq {s}")
        if ctx.op.text == "!=": self.code.append("not")
        return "bool"

    def visitIntExpr(self, ctx):
        self.code.append(f"push I {ctx.getText()}")
        return "int"

    def visitFloatExpr(self, ctx):
        self.code.append(f"push F {ctx.getText()}")
        return "float"

    def visitBoolExpr(self, ctx):
        self.code.append(f"push B {ctx.getText()}")
        return "bool"

    def visitStringExpr(self, ctx):
        self.code.append(f"push S {ctx.getText()}")
        return "string"

    def visitIdExpr(self, ctx):
        name = ctx.getText()
        self.code.append(f"load {name}")
        return self.symbol_table[name]

    def visitExprStmt(self, ctx):
        self.visit(ctx.expr())
        self.code.append("pop")

    def visitNotExpr(self, ctx):
        self.visit(ctx.expr())
        self.code.append("not")
        return "bool"

    def visitUnaryMinus(self, ctx):
        t = self.visit(ctx.expr())
        self.code.append(f"uminus {'I' if t == 'int' else 'F'}")
        return t
    
    def visitConcat(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.code.append("concat")
        return "string"
    
    def visitAndExpr(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.code.append("and")
        return "bool"

    def visitOrExpr(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.code.append("or")
        return "bool"
    
    def visitParens(self, ctx):
        return self.visit(ctx.expr())