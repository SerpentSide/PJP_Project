from antlr4 import *
from PLC_Projekt_exprLexer import PLC_Projekt_exprLexer
from PLC_Projekt_exprParser import PLC_Projekt_exprParser

from TypeCheckVisitor import TypeCheckVisitor
from CompilerVisitor import CompilerVisitor

from VM import run_vm


def main():
    file_name = "input.txt"

    with open(file_name, "r", encoding="utf-8") as f:
        input_text = f.read()

    input_stream = InputStream(input_text)

    lexer = PLC_Projekt_exprLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = PLC_Projekt_exprParser(tokens)

    tree = parser.program()

    type_checker = TypeCheckVisitor()
    result = type_checker.visit(tree)

    print("\n--- SYMBOL TABLE ---")
    for name, typ in type_checker.memory.variables.items():
        print(f"{name}: {typ}")

    print("\n--- TYPE CHECK RESULT ---")
    print(result)

    if result == "error":
        print("\nCompilation stopped due to type errors.")
        return
    compiler = CompilerVisitor()
    code = compiler.visit(tree)

    print("\n--- GENERATED CODE ---")
    for instr in code:
        print(instr)

    print("\n--- VIRTUAL MACHINE ---")
    run_vm(code)


if __name__ == "__main__":
    main()