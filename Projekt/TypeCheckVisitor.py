from PLC_Projekt_exprVisitor import PLC_Projekt_exprVisitor
from SymbolTable import SymbolTable
class TypeCheckVisitor(PLC_Projekt_exprVisitor):
    def __init__(self):
        self.memory = SymbolTable()
 #Declaration   
    def visitDeclaration(self, ctx):
        type = ctx.primitiveType().getText()
        for id in ctx.IDENTIFIER():
            name = id.getText()
            if name in self.memory:
                print(f"Variable {name} already declared")
                return "error"
            else:
                self.memory[name] = type

#Types
    def visitIntExpr(self, ctx):
        return "int"
    def visitFloatExpr(self, ctx):
        return "float"
    def visitStringExpr(self, ctx):
        return "string"
    def visitBoolExpr(self, ctx):
        return "bool"

    def visitIdExpr(self, ctx):
        name = ctx.getText()
        if name not in self.memory:
            print(f"Variable {name} not declared")
            return "error"
        return self.memory[name]
#Expresions
    def visitMulExpr(self, ctx):
        operator = ctx.op.text
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left == "error" or right == "error":
            return "error"
        if left in ["int", "float"] and right in ["int", "float"]:
            if left == "float" or right == "float":
                if operator == "%":
                    print(f"Float is not compatible with '%'")
                    return "error"
                return "float"
            return "int"
        print(f"Incompatible type {left} and {right}")
        return "error"
    
    def visitAddExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left == "error" or right == "error":
            return "error"
        if left in ["int", "float"] and right in ["int", "float"]:
            if left == "float" or right == "float":
                return "float"
            return "int"
        print(f"Incompatible type {left} and {right}")
        return "error"
    
    def visitUnaryMinus(self, ctx):
        exp = self.visit(ctx.expr())
        if exp in ["float", "int"]:
            return exp
        print(f"Cannot assign '-' to {exp}")
        return "error"
    
    def visitNotExpr(self, ctx):
        exp = self.visit(ctx.expr())
        if exp == "bool":
            return "bool"
        print(f"Cannot assign '!' to {exp}")
        return "error"

    def visitConcat(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left == "error" or right == "error":
            return "error"
        if left == "string" and right == "string":
            return "string"
        print(f"Cannot assign '.' to {left} and {right}")
        return "error"

    def  visitRelExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left == "error" or right == "error":
            return "error"
        if left in ["int", "float"] and right in ["int", "float"]:
            return "bool"
        print(f"Cannot compare {left} and {right}")
        return "error"

    def visitEqExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left == "error" or right == "error":
            return "error"
        if left in ["int", "float", "string"] and right in ["int", "float", "string"]:
            return "bool"
        print(f"Cannot check equality for {left} and {right}")
        return "error"
    
    def visitOrExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left == "error" or right == "error":
            return "error"
        if left == "bool" and right == "bool":
            return "bool"
        print(f"Cannot apply || on {left} and {right}")
        return "error"

    def visitAndExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left == "error" or right == "error":
            return "error"
        if left == "bool" and right == "bool":
            return "bool"
        print(f"Cannot apply && on {left} and {right}")
        return "error"

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitAssignment(self, ctx):
        name = ctx.IDENTIFIER().getText()
        if name not in self.memory:
            print(f"Undeclared variable {name}")
            return "error"
        var_type = self.memory[name]
        expr_type = self.visit(ctx.expr())
        if expr_type == "error":
            return "error"
        if var_type == "float" and expr_type == "int":
            return "float"
        if var_type != expr_type:
            print(f"Cannot assign {expr_type} to {var_type}")
            return "error"
        return var_type
#Statements
    def visitExprStmt(self, ctx):
        return self.visit(ctx.expr())
    
    def visitReadStmt(self, ctx):
        for id in ctx.IDENTIFIER():
            name = id.getText()
            if name not in self.memory:
                print(f"Undeclared variable {name}")
                return "error"
        return None
    
    def visitWriteStmt(self, ctx):
        for exp in ctx.expr():
            type = self.visit(exp)
            if type == "error":
                return "error"
            
    def visitBlock(self, ctx):
        for st in ctx.statement():
            if self.visit(st) == "error":
                return "error"
            
    def visitIfStmt(self, ctx):
        cond = self.visit(ctx.expr())
        if cond != "bool":
            print(f"If condition must be bool, got {cond}")
            return "error"
        if self.visit(ctx.statement(0)) == "error":
            return "error"
        if ctx.statement(1):
            if self.visit(ctx.statement(1)) == "error":
                return "error"
        return None
        
    def visitWhileStmt(self, ctx):
        cond = self.visit(ctx.expr())
        if cond != "bool":
            print(f"While condition must be bool, got {cond}")
            return "error"
        if self.visit(ctx.statement()) == "error":
            return "error"
        return None