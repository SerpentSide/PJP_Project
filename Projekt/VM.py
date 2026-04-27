def run_vm(codes):
    def cast(value, type_):
        if type_ == "I":
            return int(value)
        elif type_ == "F":
            return float(value)
        elif type_ == "S":
            return value.strip('"')
        elif type_ == "B":
            return value == "true"
        else:
            raise Exception(f"Unknown type {type_}")

    stack = []
    vars = {}
    labels = {}
    for i, line in enumerate(codes):
        parts = line.split(maxsplit=2)
        if parts[0] == "label":
            labels[int(parts[1])] = i
    ip = 0
    while ip < len(codes):
        parts = codes[ip].split(maxsplit=2)
        op = parts[0]
        if op == "push":
            stack.append(cast(parts[2], parts[1]))

        elif op == "load":
            stack.append(vars[parts[1]])

        elif op == "save":
            vars[parts[1]] = stack.pop()

        elif op == "pop":
            stack.pop()
        elif op == "print":
            count = int(parts[1])
            vals = [stack.pop() for _ in range(count)]
            print(*reversed(vals))
        elif op == "read":
            val = input()
            stack.append(cast(val, parts[1]))
        elif op in ["add", "sub", "mul", "div"]:
            b = stack.pop()
            a = stack.pop()
            if op == "add":
                stack.append(a + b)
            elif op == "sub":
                stack.append(a - b)
            elif op == "mul":
                stack.append(a * b)
            elif op == "div":
                if len(parts) > 1 and parts[1] == "I":
                    stack.append(a // b)
                else:
                    stack.append(a / b)

        elif op == "mod":
            b = stack.pop()
            a = stack.pop()
            stack.append(a % b)

        elif op == "uminus":
            stack.append(-stack.pop())

        elif op == "itof":
            stack.append(float(stack.pop()))

        # --- POROVNÁNÍ ---
        elif op == "lt":
            b = stack.pop()
            a = stack.pop()
            stack.append(a < b)

        elif op == "gt":
            b = stack.pop()
            a = stack.pop()
            stack.append(a > b)

        elif op == "eq":
            b = stack.pop()
            a = stack.pop()
            stack.append(a == b)

        elif op == "and":
            b = stack.pop()
            a = stack.pop()
            stack.append(a and b)

        elif op == "or":
            b = stack.pop()
            a = stack.pop()
            stack.append(a or b)

        elif op == "not":
            stack.append(not stack.pop())

        elif op == "concat":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)

        elif op == "label":
            pass

        elif op == "jmp":
            ip = labels[int(parts[1])]
            continue

        elif op == "fjmp":
            cond = stack.pop()
            if not cond:
                ip = labels[int(parts[1])]
                continue

        else:
            raise Exception(f"Unknown instruction: {op}")

        ip += 1