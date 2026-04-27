from antlr4 import *
from PLC_Lab8_exprLexer import PLC_Lab8_exprLexer
from PLC_Lab8_exprParser import PLC_Lab8_exprParser
from PLC_Lab8_exprVisitor import PLC_Lab8_exprVisitor
from PLC_Lab8_exprListener import PLC_Lab8_exprListener

def main():
    input_text = """int a,b;
a = b = 15;
a + b;
a % b;
float c;
c = a + b;
c + a;
c = a;
c + 1.1;
10 % a;
"""

    input_stream = InputStream(input_text)
    lexer = PLC_Lab8_exprLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = PLC_Lab8_exprParser(tokens)

    tree = parser.program()

    listener = PLC_Lab8_exprListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    print("\n--- SYMBOL TABLE ---")
    for key, value in listener.memory.variables.items():
        print(f"{key}: {value}")

if __name__ == '__main__':
    main()