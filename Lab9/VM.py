def run_vm(codes):
    def cast(value, type):
        if type == "I":
            return int(value)
        elif type == "F":
            return float(value)
        else: raise Exception

    stack = []
    vars = {}
    for str2 in codes:
        str = str2.split()
        print(str)
        op = str[0]
        if op == "PUSH":
            stack.append(cast(str[2],str[1]))
        elif op == "LOAD":
            stack.append(vars[str[1]])
        elif op == "SAVE":
            value = stack.pop()
            vars[str[2]] = cast(value, str[1])
        elif op == "ADD":
            value1 = stack.pop()
            value2 = stack.pop()
            stack.append(value1 + value2)
        elif op == "SUB":
            value1 = stack.pop()
            value2 = stack.pop()
            stack.append(value1 - value2)
        elif op == "MUL":
            value1 = stack.pop()
            value2 = stack.pop()
            stack.append(value1 * value2)
        elif op == "DIV":
            value1 = stack.pop()
            value2 = stack.pop()
            stack.append(value1 / value2)
        elif op == "MOD":
            value1 = stack.pop()
            value2 = stack.pop()
            stack.append(value1 % value2)
        elif op == "PRINT":
            #print("PRINT: ")
            value = stack.pop()
            if str[1] == "I":
                print(int(value))
            elif str[1] == "F":
                print(float(value))
