from antlr4 import *
from PLC_Lab8_exprLexer import PLC_Lab8_exprLexer
from PLC_Lab8_exprParser import PLC_Lab8_exprParser
from PLC_Lab8_exprVisitor import PLC_Lab8_exprVisitor
from PLC_Lab8_exprListener import PLC_Lab8_exprListener
from listenerType import ListenerType
from visitorStack import VisitorStack
from vm import VM
import sys


def compare_codes(my_file, teacher_file):
    print(f"--- Comparing {my_file} vs {teacher_file} ---")
    
    try:
        with open(my_file, 'r') as f1, open(teacher_file, 'r') as f2:
            my_lines = [line.strip() for line in f1.readlines() if line.strip()]
            teacher_lines = [line.strip() for line in f2.readlines() if line.strip()]

        max_lines = max(len(my_lines), len(teacher_lines))
        errors = 0

        print(f"{'Line':<5} | {'Your Code':<20} | {'Teacher Code':<20} | {'Status'}")
        print("-" * 65)

        for i in range(max_lines):
            mine = my_lines[i] if i < len(my_lines) else "MISSING"
            teacher = teacher_lines[i] if i < len(teacher_lines) else "MISSING"
            
            status = "OK" if mine == teacher else "!! DIFF !!"
            if status != "OK":
                errors += 1
            
            print(f"{i+1:<5} | {mine:<20} | {teacher:<20} | {status}")

        print("-" * 65)
        if errors == 0:
            print("SHODA! Tvůj kód generuje přesně to samé co vzor.")
        else:
            print(f"❌ Nalezeno {errors} rozdílů. Zkontroluj pořadí instrukcí.")

    except FileNotFoundError:
        print("Chyba: Jeden ze souborů nebyl nalezen. Nejdřív spusť kompilátor.")

def run_compiler(input_text):
    input_stream = InputStream(input_text)
    lexer = PLC_Lab8_exprLexer(input_stream)
    
    
    tokens = CommonTokenStream(lexer)
    parser = PLC_Lab8_exprParser(tokens)
    
    tree = parser.program()
    
    
    if parser.getNumberOfSyntaxErrors() > 0:
        print("SYNTAX ERROR: Stop.")
        return

    
    type_listener = ListenerType()
    walker = ParseTreeWalker()
    try:
        walker.walk(type_listener, tree)
    except Exception as e:
        print(f"TYPE ERROR: {e}")
        return

    
    visitor = VisitorStack(type_listener.types)
    visitor.visit(tree)
    
   
    with open("target_code.txt", "w") as f:
        for line in visitor.code:
            f.write(str(line) + "\n")
    
    print("=== code generated (target_code.txt) ===")

    
    print("\n=== INTERPRETER OUTPUT ===")
    vm = VM()
    try:
        vm.run(visitor.code)
    except Exception as e:
        print(f"RUNTIME ERROR: {e}")
    

def main():
    
    input_sample = """
                    FILE f;
                    fopen f "test.txt";
                    f << 1 << 2 << "abc";
                    """
   
    
    
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            code_to_run = f.read()
    else:
        code_to_run = input_sample

    run_compiler(code_to_run)
    #compare_codes("target_code.txt", "result.txt")

if __name__ == '__main__':
    main()
