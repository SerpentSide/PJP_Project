grammar PLC_Projekt_expr;

//Multiple statements   
program: statement* EOF;

//Statement
statement
    : ';'                                              # emptyStmt
    | primitiveType IDENTIFIER (',' IDENTIFIER)* ';'   # declaration
    | expr ';'                                         # exprStmt
    | READ IDENTIFIER (',' IDENTIFIER)* ';'          # readStmt
    | WRITE expr (',' expr)* ';'                     # writeStmt
    | '{' statement* '}'                               # block
    | IF '(' condition=expr ')' trueStmt=statement (ELSE falseStmt=statement)?  # ifStmt
    | WHILE '(' condition=expr ')' statement                   # whileStmt
    ;

//Expresions    
expr

    : SUB expr                                         # unaryMinus
    | NOT expr                                         # notExpr
    | expr op=(MUL | DIV | MOD) expr                      # mulExpr
    | expr op=(ADD | SUB) expr                            # addExpr
    | expr '.' expr                                       # concat
    | expr op=(LT | GT) expr                            # relExpr
    | expr op=(EQ | NEQ) expr                          # eqExpr
    | expr AND expr                                   # andExpr
    | expr OR expr                                   # orExpr
    | <assoc=right> IDENTIFIER ASSIGN expr                # assignment
    | '(' expr ')'                                     # parens
    | literal                                          # literalExpr
    | IDENTIFIER                                       # idExpr
    ;

//Literals
literal
    : INT       # intExpr
    | FLOAT     # floatExpr
    | BOOL      # boolExpr
    | STRING    # stringExpr
    ;

//Types
primitiveType
    : 'int'
    | 'float'
    | 'bool'
    | 'string'
    ;

//Keywords
READ : 'read';
WRITE : 'write';
IF : 'if';
ELSE : 'else';
WHILE : 'while';
BOOL : 'true' | 'false';
MUL : '*' ; 
DIV : '/' ;
MOD : '%' ;
ADD : '+' ;
SUB : '-' ;
OR : '||' ;
AND : '&&' ;
EQ : '==' ;
NEQ : '!=' ;
LT : '<' ;
GT : '>' ;
ASSIGN : '=' ;
NOT : '!' ;
IDENTIFIER : [a-zA-Z][a-zA-Z0-9]*;
FLOAT : [0-9]+ '.' [0-9]+;
INT : [0-9]+;
STRING : '"' (~["\r\n])* '"';

WS : [ \t\r\n]+ -> skip;
LINE_COMMENT : '//' ~[\r\n]* -> skip;
