from antlr4 import *
from PLC_Lab7_exprLexer import PLC_Lab7_exprLexer
from PLC_Lab7_exprParser import PLC_Lab7_exprParser
from PLC_Lab7_exprVisitor import PLC_Lab7_exprVisitor
from PLC_Lab7_exprListener import PLC_Lab7_exprListener

def main():
    input_text = """012-10
2 * (0xff+5)
0x23e5-0x201
"""
    input_stream = InputStream(input_text)
    lexer = PLC_Lab7_exprLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = PLC_Lab7_exprParser(tokens)

    tree = parser.prog()
    visitor = PLC_Lab7_exprVisitor()
    results = visitor.visit(tree)
    #"""
    for r in results:
        print(r)
    """
    listener = PLC_Lab7_exprListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    for key, value in listener.values.items():
        print(f"{key}: {value}")
    """
if __name__ == '__main__':
    main()