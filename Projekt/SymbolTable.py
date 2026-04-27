class SymbolTable:
    def __init__(self):
        self.variables = {}

    def __setitem__(self, key, value):
        if key in self.variables:
            print(f"Value {key} already declared")
        else:
            self.variables[key] = value
        pass
    def __getitem__(self, key):
        if not key in self.variables:
            #print(f"Miising variable '{key}' not declared")
            return "error"
        else:
            return self.variables[key]
        pass
    def __contains__(self, key):
        return key in self.variables
        pass
    def __str__(self):
        if not self.variables:
            return "SymbolTable:"
        lines = ["SymbolTable:"]
        for name, typ in self.variables.items():
            lines.append(f"  {name} : {typ}")
        return "\n".join(lines)