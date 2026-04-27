# Generated from ./PLC_Projekt_expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,130,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,
        0,10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,24,8,1,10,1,12,
        1,27,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,38,8,1,10,1,12,
        1,41,9,1,1,1,1,1,1,1,1,1,1,1,5,1,48,8,1,10,1,12,1,51,9,1,1,1,1,1,
        1,1,1,1,5,1,57,8,1,10,1,12,1,60,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,70,8,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,78,8,1,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,94,8,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,5,2,117,8,2,10,2,12,2,120,9,2,1,3,1,3,1,3,1,3,3,3,126,8,
        3,1,4,1,4,1,4,0,1,4,5,0,2,4,6,8,0,5,1,0,18,20,1,0,21,22,1,0,27,28,
        1,0,25,26,1,0,8,11,152,0,13,1,0,0,0,2,77,1,0,0,0,4,93,1,0,0,0,6,
        125,1,0,0,0,8,127,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,
        0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,
        5,0,0,1,17,1,1,0,0,0,18,78,5,1,0,0,19,20,3,8,4,0,20,25,5,31,0,0,
        21,22,5,2,0,0,22,24,5,31,0,0,23,21,1,0,0,0,24,27,1,0,0,0,25,23,1,
        0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,29,5,1,0,0,29,
        78,1,0,0,0,30,31,3,4,2,0,31,32,5,1,0,0,32,78,1,0,0,0,33,34,5,12,
        0,0,34,39,5,31,0,0,35,36,5,2,0,0,36,38,5,31,0,0,37,35,1,0,0,0,38,
        41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,1,0,0,0,41,39,1,0,0,
        0,42,78,5,1,0,0,43,44,5,13,0,0,44,49,3,4,2,0,45,46,5,2,0,0,46,48,
        3,4,2,0,47,45,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,
        50,52,1,0,0,0,51,49,1,0,0,0,52,53,5,1,0,0,53,78,1,0,0,0,54,58,5,
        3,0,0,55,57,3,2,1,0,56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,
        59,1,0,0,0,59,61,1,0,0,0,60,58,1,0,0,0,61,78,5,4,0,0,62,63,5,14,
        0,0,63,64,5,5,0,0,64,65,3,4,2,0,65,66,5,6,0,0,66,69,3,2,1,0,67,68,
        5,15,0,0,68,70,3,2,1,0,69,67,1,0,0,0,69,70,1,0,0,0,70,78,1,0,0,0,
        71,72,5,16,0,0,72,73,5,5,0,0,73,74,3,4,2,0,74,75,5,6,0,0,75,76,3,
        2,1,0,76,78,1,0,0,0,77,18,1,0,0,0,77,19,1,0,0,0,77,30,1,0,0,0,77,
        33,1,0,0,0,77,43,1,0,0,0,77,54,1,0,0,0,77,62,1,0,0,0,77,71,1,0,0,
        0,78,3,1,0,0,0,79,80,6,2,-1,0,80,81,5,22,0,0,81,94,3,4,2,13,82,83,
        5,30,0,0,83,94,3,4,2,12,84,85,5,31,0,0,85,86,5,29,0,0,86,94,3,4,
        2,4,87,88,5,5,0,0,88,89,3,4,2,0,89,90,5,6,0,0,90,94,1,0,0,0,91,94,
        3,6,3,0,92,94,5,31,0,0,93,79,1,0,0,0,93,82,1,0,0,0,93,84,1,0,0,0,
        93,87,1,0,0,0,93,91,1,0,0,0,93,92,1,0,0,0,94,118,1,0,0,0,95,96,10,
        11,0,0,96,97,7,0,0,0,97,117,3,4,2,12,98,99,10,10,0,0,99,100,7,1,
        0,0,100,117,3,4,2,11,101,102,10,9,0,0,102,103,5,7,0,0,103,117,3,
        4,2,10,104,105,10,8,0,0,105,106,7,2,0,0,106,117,3,4,2,9,107,108,
        10,7,0,0,108,109,7,3,0,0,109,117,3,4,2,8,110,111,10,6,0,0,111,112,
        5,24,0,0,112,117,3,4,2,7,113,114,10,5,0,0,114,115,5,23,0,0,115,117,
        3,4,2,6,116,95,1,0,0,0,116,98,1,0,0,0,116,101,1,0,0,0,116,104,1,
        0,0,0,116,107,1,0,0,0,116,110,1,0,0,0,116,113,1,0,0,0,117,120,1,
        0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,5,1,0,0,0,120,118,1,0,
        0,0,121,126,5,33,0,0,122,126,5,32,0,0,123,126,5,17,0,0,124,126,5,
        34,0,0,125,121,1,0,0,0,125,122,1,0,0,0,125,123,1,0,0,0,125,124,1,
        0,0,0,126,7,1,0,0,0,127,128,7,4,0,0,128,9,1,0,0,0,11,13,25,39,49,
        58,69,77,93,116,118,125
    ]

class PLC_Projekt_exprParser ( Parser ):

    grammarFileName = "PLC_Projekt_expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'{'", "'}'", "'('", "')'", 
                     "'.'", "'int'", "'float'", "'bool'", "'string'", "'read'", 
                     "'write'", "'if'", "'else'", "'while'", "<INVALID>", 
                     "'*'", "'/'", "'%'", "'+'", "'-'", "'||'", "'&&'", 
                     "'=='", "'!='", "'<'", "'>'", "'='", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "READ", "WRITE", "IF", "ELSE", "WHILE", "BOOL", "MUL", 
                      "DIV", "MOD", "ADD", "SUB", "OR", "AND", "EQ", "NEQ", 
                      "LT", "GT", "ASSIGN", "NOT", "IDENTIFIER", "FLOAT", 
                      "INT", "STRING", "WS", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_literal = 3
    RULE_primitiveType = 4

    ruleNames =  [ "program", "statement", "expr", "literal", "primitiveType" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    READ=12
    WRITE=13
    IF=14
    ELSE=15
    WHILE=16
    BOOL=17
    MUL=18
    DIV=19
    MOD=20
    ADD=21
    SUB=22
    OR=23
    AND=24
    EQ=25
    NEQ=26
    LT=27
    GT=28
    ASSIGN=29
    NOT=30
    IDENTIFIER=31
    FLOAT=32
    INT=33
    STRING=34
    WS=35
    LINE_COMMENT=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PLC_Projekt_exprParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_Projekt_exprParser.StatementContext)
            else:
                return self.getTypedRuleContext(PLC_Projekt_exprParser.StatementContext,i)


        def getRuleIndex(self):
            return PLC_Projekt_exprParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PLC_Projekt_exprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33290420010) != 0):
                self.state = 10
                self.statement()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(PLC_Projekt_exprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PLC_Projekt_exprParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PLC_Projekt_exprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStmt" ):
                listener.enterExprStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStmt" ):
                listener.exitExprStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)


    class WhileStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.StatementContext
            super().__init__(parser)
            self.condition = None # ExprContext
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(PLC_Projekt_exprParser.WHILE, 0)
        def statement(self):
            return self.getTypedRuleContext(PLC_Projekt_exprParser.StatementContext,0)

        def expr(self):
            return self.getTypedRuleContext(PLC_Projekt_exprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)


    class ReadStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(PLC_Projekt_exprParser.READ, 0)
        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PLC_Projekt_exprParser.IDENTIFIER)
            else:
                return self.getToken(PLC_Projekt_exprParser.IDENTIFIER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStmt" ):
                listener.enterReadStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStmt" ):
                listener.exitReadStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStmt" ):
                return visitor.visitReadStmt(self)
            else:
                return visitor.visitChildren(self)


    class IfStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.StatementContext
            super().__init__(parser)
            self.condition = None # ExprContext
            self.trueStmt = None # StatementContext
            self.falseStmt = None # StatementContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(PLC_Projekt_exprParser.IF, 0)
        def expr(self):
            return self.getTypedRuleContext(PLC_Projekt_exprParser.ExprContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_Projekt_exprParser.StatementContext)
            else:
                return self.getTypedRuleContext(PLC_Projekt_exprParser.StatementContext,i)

        def ELSE(self):
            return self.getToken(PLC_Projekt_exprParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)


    class EmptyStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStmt" ):
                listener.enterEmptyStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStmt" ):
                listener.exitEmptyStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyStmt" ):
                return visitor.visitEmptyStmt(self)
            else:
                return visitor.visitChildren(self)


    class BlockContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_Projekt_exprParser.StatementContext)
            else:
                return self.getTypedRuleContext(PLC_Projekt_exprParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)


    class WriteStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE(self):
            return self.getToken(PLC_Projekt_exprParser.WRITE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_Projekt_exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(PLC_Projekt_exprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStmt" ):
                listener.enterWriteStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStmt" ):
                listener.exitWriteStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStmt" ):
                return visitor.visitWriteStmt(self)
            else:
                return visitor.visitChildren(self)


    class DeclarationContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primitiveType(self):
            return self.getTypedRuleContext(PLC_Projekt_exprParser.PrimitiveTypeContext,0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PLC_Projekt_exprParser.IDENTIFIER)
            else:
                return self.getToken(PLC_Projekt_exprParser.IDENTIFIER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = PLC_Projekt_exprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = PLC_Projekt_exprParser.EmptyStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(PLC_Projekt_exprParser.T__0)
                pass
            elif token in [8, 9, 10, 11]:
                localctx = PLC_Projekt_exprParser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.primitiveType()
                self.state = 20
                self.match(PLC_Projekt_exprParser.IDENTIFIER)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 21
                    self.match(PLC_Projekt_exprParser.T__1)
                    self.state = 22
                    self.match(PLC_Projekt_exprParser.IDENTIFIER)
                    self.state = 27
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 28
                self.match(PLC_Projekt_exprParser.T__0)
                pass
            elif token in [5, 17, 22, 30, 31, 32, 33, 34]:
                localctx = PLC_Projekt_exprParser.ExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.expr(0)
                self.state = 31
                self.match(PLC_Projekt_exprParser.T__0)
                pass
            elif token in [12]:
                localctx = PLC_Projekt_exprParser.ReadStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.match(PLC_Projekt_exprParser.READ)
                self.state = 34
                self.match(PLC_Projekt_exprParser.IDENTIFIER)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 35
                    self.match(PLC_Projekt_exprParser.T__1)
                    self.state = 36
                    self.match(PLC_Projekt_exprParser.IDENTIFIER)
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 42
                self.match(PLC_Projekt_exprParser.T__0)
                pass
            elif token in [13]:
                localctx = PLC_Projekt_exprParser.WriteStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 43
                self.match(PLC_Projekt_exprParser.WRITE)
                self.state = 44
                self.expr(0)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 45
                    self.match(PLC_Projekt_exprParser.T__1)
                    self.state = 46
                    self.expr(0)
                    self.state = 51
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 52
                self.match(PLC_Projekt_exprParser.T__0)
                pass
            elif token in [3]:
                localctx = PLC_Projekt_exprParser.BlockContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 54
                self.match(PLC_Projekt_exprParser.T__2)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33290420010) != 0):
                    self.state = 55
                    self.statement()
                    self.state = 60
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 61
                self.match(PLC_Projekt_exprParser.T__3)
                pass
            elif token in [14]:
                localctx = PLC_Projekt_exprParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 62
                self.match(PLC_Projekt_exprParser.IF)
                self.state = 63
                self.match(PLC_Projekt_exprParser.T__4)
                self.state = 64
                localctx.condition = self.expr(0)
                self.state = 65
                self.match(PLC_Projekt_exprParser.T__5)
                self.state = 66
                localctx.trueStmt = self.statement()
                self.state = 69
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 67
                    self.match(PLC_Projekt_exprParser.ELSE)
                    self.state = 68
                    localctx.falseStmt = self.statement()


                pass
            elif token in [16]:
                localctx = PLC_Projekt_exprParser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 71
                self.match(PLC_Projekt_exprParser.WHILE)
                self.state = 72
                self.match(PLC_Projekt_exprParser.T__4)
                self.state = 73
                localctx.condition = self.expr(0)
                self.state = 74
                self.match(PLC_Projekt_exprParser.T__5)
                self.state = 75
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PLC_Projekt_exprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PLC_Projekt_exprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(PLC_Projekt_exprParser.IDENTIFIER, 0)
        def ASSIGN(self):
            return self.getToken(PLC_Projekt_exprParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(PLC_Projekt_exprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_Projekt_exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(PLC_Projekt_exprParser.ExprContext,i)

        def OR(self):
            return self.getToken(PLC_Projekt_exprParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class ConcatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_Projekt_exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(PLC_Projekt_exprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcat" ):
                listener.enterConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcat" ):
                listener.exitConcat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat" ):
                return visitor.visitConcat(self)
            else:
                return visitor.visitChildren(self)


    class EqExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_Projekt_exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(PLC_Projekt_exprParser.ExprContext,i)

        def EQ(self):
            return self.getToken(PLC_Projekt_exprParser.EQ, 0)
        def NEQ(self):
            return self.getToken(PLC_Projekt_exprParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqExpr" ):
                listener.enterEqExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqExpr" ):
                listener.exitEqExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqExpr" ):
                return visitor.visitEqExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(PLC_Projekt_exprParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(PLC_Projekt_exprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_Projekt_exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(PLC_Projekt_exprParser.ExprContext,i)

        def ADD(self):
            return self.getToken(PLC_Projekt_exprParser.ADD, 0)
        def SUB(self):
            return self.getToken(PLC_Projekt_exprParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class LiteralExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(PLC_Projekt_exprParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralExpr" ):
                listener.enterLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralExpr" ):
                listener.exitLiteralExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralExpr" ):
                return visitor.visitLiteralExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(PLC_Projekt_exprParser.SUB, 0)
        def expr(self):
            return self.getTypedRuleContext(PLC_Projekt_exprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class MulExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_Projekt_exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(PLC_Projekt_exprParser.ExprContext,i)

        def MUL(self):
            return self.getToken(PLC_Projekt_exprParser.MUL, 0)
        def DIV(self):
            return self.getToken(PLC_Projekt_exprParser.DIV, 0)
        def MOD(self):
            return self.getToken(PLC_Projekt_exprParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpr" ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpr" ):
                listener.exitMulExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_Projekt_exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(PLC_Projekt_exprParser.ExprContext,i)

        def LT(self):
            return self.getToken(PLC_Projekt_exprParser.LT, 0)
        def GT(self):
            return self.getToken(PLC_Projekt_exprParser.GT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelExpr" ):
                listener.enterRelExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelExpr" ):
                listener.exitRelExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelExpr" ):
                return visitor.visitRelExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(PLC_Projekt_exprParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_Projekt_exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(PLC_Projekt_exprParser.ExprContext,i)

        def AND(self):
            return self.getToken(PLC_Projekt_exprParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PLC_Projekt_exprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = PLC_Projekt_exprParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 80
                self.match(PLC_Projekt_exprParser.SUB)
                self.state = 81
                self.expr(13)
                pass

            elif la_ == 2:
                localctx = PLC_Projekt_exprParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 82
                self.match(PLC_Projekt_exprParser.NOT)
                self.state = 83
                self.expr(12)
                pass

            elif la_ == 3:
                localctx = PLC_Projekt_exprParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 84
                self.match(PLC_Projekt_exprParser.IDENTIFIER)
                self.state = 85
                self.match(PLC_Projekt_exprParser.ASSIGN)
                self.state = 86
                self.expr(4)
                pass

            elif la_ == 4:
                localctx = PLC_Projekt_exprParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 87
                self.match(PLC_Projekt_exprParser.T__4)
                self.state = 88
                self.expr(0)
                self.state = 89
                self.match(PLC_Projekt_exprParser.T__5)
                pass

            elif la_ == 5:
                localctx = PLC_Projekt_exprParser.LiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 91
                self.literal()
                pass

            elif la_ == 6:
                localctx = PLC_Projekt_exprParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 92
                self.match(PLC_Projekt_exprParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 116
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = PLC_Projekt_exprParser.MulExprContext(self, PLC_Projekt_exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 95
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 96
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1835008) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 97
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = PLC_Projekt_exprParser.AddExprContext(self, PLC_Projekt_exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 98
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 99
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 100
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = PLC_Projekt_exprParser.ConcatContext(self, PLC_Projekt_exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 101
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 102
                        self.match(PLC_Projekt_exprParser.T__6)
                        self.state = 103
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = PLC_Projekt_exprParser.RelExprContext(self, PLC_Projekt_exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 104
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 105
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==27 or _la==28):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 106
                        self.expr(9)
                        pass

                    elif la_ == 5:
                        localctx = PLC_Projekt_exprParser.EqExprContext(self, PLC_Projekt_exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 107
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 108
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==26):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 109
                        self.expr(8)
                        pass

                    elif la_ == 6:
                        localctx = PLC_Projekt_exprParser.AndExprContext(self, PLC_Projekt_exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 110
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 111
                        self.match(PLC_Projekt_exprParser.AND)
                        self.state = 112
                        self.expr(7)
                        pass

                    elif la_ == 7:
                        localctx = PLC_Projekt_exprParser.OrExprContext(self, PLC_Projekt_exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 113
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 114
                        self.match(PLC_Projekt_exprParser.OR)
                        self.state = 115
                        self.expr(6)
                        pass

             
                self.state = 120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PLC_Projekt_exprParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringExprContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(PLC_Projekt_exprParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class FloatExprContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(PLC_Projekt_exprParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatExpr" ):
                listener.enterFloatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatExpr" ):
                listener.exitFloatExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatExpr" ):
                return visitor.visitFloatExpr(self)
            else:
                return visitor.visitChildren(self)


    class IntExprContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(PLC_Projekt_exprParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntExpr" ):
                listener.enterIntExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntExpr" ):
                listener.exitIntExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpr" ):
                return visitor.visitIntExpr(self)
            else:
                return visitor.visitChildren(self)


    class BoolExprContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLC_Projekt_exprParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(PLC_Projekt_exprParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpr" ):
                listener.enterBoolExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpr" ):
                listener.exitBoolExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpr" ):
                return visitor.visitBoolExpr(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = PLC_Projekt_exprParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_literal)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                localctx = PLC_Projekt_exprParser.IntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.match(PLC_Projekt_exprParser.INT)
                pass
            elif token in [32]:
                localctx = PLC_Projekt_exprParser.FloatExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.match(PLC_Projekt_exprParser.FLOAT)
                pass
            elif token in [17]:
                localctx = PLC_Projekt_exprParser.BoolExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                self.match(PLC_Projekt_exprParser.BOOL)
                pass
            elif token in [34]:
                localctx = PLC_Projekt_exprParser.StringExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 124
                self.match(PLC_Projekt_exprParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PLC_Projekt_exprParser.RULE_primitiveType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveType" ):
                listener.enterPrimitiveType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveType" ):
                listener.exitPrimitiveType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = PLC_Projekt_exprParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 5)
         




