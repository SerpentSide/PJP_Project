class VM:

    def __init__(self):
        self.stack = []
        self.memory = {}
        self.labels = {}
        self.files = {}
        self.current_file = "f"

    def run(self, lines):
        pc = 0

        #labely  {1:10,2:15} label 1 na radku 10
        for i, line in enumerate(lines):
            parts = line.strip().split()
            if parts and parts[0] == "label":
                self.labels[int(parts[1])] = i

        #dokud je pocitadlo aktualni instrukce mensi nez radky
        while pc < len(lines):
            parts = lines[pc].strip().split()

            if not parts:
                pc += 1
                continue

            instr = parts[0]

            if instr == "push":
                typ = parts[1]
                val = " ".join(parts[2:])

                if typ == "I":
                    self.stack.append(int(val))
                elif typ == "F":
                    self.stack.append(float(val))
                elif typ == "B":
                    self.stack.append(val == "true")
                else:
                    self.stack.append(val.strip('"'))

            elif instr == "pop":
                self.stack.pop()

            elif instr == "load":
                var = parts[1]
                self.stack.append(self.memory[var])

            elif instr == "save":
                var = parts[1]
                val = self.stack.pop()
                self.memory[var] = val

            elif instr == "add":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)

            elif instr == "sub":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a - b)

            elif instr == "mul":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a * b)

            elif instr == "div":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a / b)

            elif instr == "mod":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a % b)

            elif instr == "uminus":
                a = self.stack.pop()
                self.stack.append(-a)

            elif instr == "concat":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)

            elif instr == "and":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a and b)

            elif instr == "or":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a or b)

            elif instr == "not":
                a = self.stack.pop()
                self.stack.append(not a)

            elif instr == "gt":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a > b)

            elif instr == "lt":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a < b)

            elif instr == "eq":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a == b)

            elif instr == "itof":
                a = self.stack.pop()
                self.stack.append(float(a))

            elif instr == "label":
                pass

            elif instr == "jmp":
                pc = self.labels[int(parts[1])]
                continue

            elif instr == "fjmp":
                cond = self.stack.pop()
                if not cond:
                    pc = self.labels[int(parts[1])]
                    continue

            elif instr == "print":
                n = int(parts[1])
                output_parts = []
                for _ in range(n):
                    output_parts.append(str(self.stack.pop()))
                output_parts.reverse()
                print(", ".join(output_parts)) # Spojí vše do jednoho řádku

            elif instr == "read":
                typ = parts[1]
                val = input()

                if typ == "I":
                    self.stack.append(int(val))
                elif typ == "F":
                    self.stack.append(float(val))
                elif typ == "B":
                    self.stack.append(val == "true")
                else:
                    self.stack.append(val)
            elif instr == "fopen":
                filename = self.stack.pop()
                f = open(filename, "w")
                self.stack.append(f)

            elif instr == "fappend":
                val = self.stack.pop()
                f = self.stack.pop()

                f.write(str(val) + "\n")

                self.stack.append(f)   # důležité!

            pc += 1