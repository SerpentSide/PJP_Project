grammar PLC_Lab8_expr;

program: statement+ ;

statement
    : primitiveType VARIABLE (',' VARIABLE)* ';'        # declaration
    | FILETYPE VARIABLE ';'                             # fileDeclaration
    | ';'                                               # empty
    | expr ';'                                          # expression
    | READ VARIABLE (',' VARIABLE)* ';'                 # read
    | WRITE expr (',' expr)* ';'                        # write
    | 'fopen' VARIABLE STRING';'                    # fopen
    | VARIABLE ('<<' expr)* ';'                      # addingFile
    | '{' statement* '}'                                # block
    | IF '(' expr ')' statement ('else' statement)?     # ifStatement
    | WHILE '(' expr ')' statement                      # whileStatement
    ;

expr  
    : '(' expr ')'                             # parens        // Úplně nejvíc (závorky)
    | SUB expr                                 # unaryMinus    // Unární mínus
    | NOT expr                                 # notExpr       // Logická negace
    | expr (MUL | DIV | MOD) expr              # mulExpr       // Násobení/Dělení
    | expr (ADD | SUB | DOT) expr              # addExpr       // Sčítání/Odčítání/Konkatenace
    | expr (LT | GT) expr                      # relExpr       // Relační operátory
    | expr (EQ | NEQ) expr                     # eqExpr        // Rovnost
    | expr AND expr                            # andExpr       // Logické AND
    | expr OR expr                             # orExpr        // Logické OR
    | <assoc=right> VARIABLE ASSIGN expr       # assignment    // NEJNIŽŠÍ PRIORITA
    | literal                                  # literalExpr
    | VARIABLE                                 # varExpr
    ;

literal
    : INT
    | FLOAT
    | BOOL
    | STRING
    ;

primitiveType
    : type=INT_KEYWORD
    | type=FLOAT_KEYWORD
    | type=BOOL_KEYWORD
    | type=STRING_KEYWORD
    ;

FILETYPE : 'FILE';

// ===== KEYWORDS =====
INT_KEYWORD    : 'int';
FLOAT_KEYWORD  : 'float';
BOOL_KEYWORD   : 'bool';
STRING_KEYWORD : 'string';

IF    : 'if';
ELSE  : 'else';
WHILE : 'while';
READ  : 'read';
WRITE : 'write';

// ===== OPERATORS =====
ASSIGN : '=';
OR  : '||';
AND : '&&';
EQ  : '==';
NEQ : '!=';
LT  : '<';
GT  : '>';

ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';
MOD : '%';
DOT : '.';
NOT : '!';

// ===== LITERALS =====
BOOL   : 'true' | 'false';
FLOAT  : [0-9]+ '.' [0-9]+ ;
INT    : [0-9]+ ; 

VARIABLE : [a-zA-Z][a-zA-Z0-9]* ;

STRING : '"' (~["\r\n])* '"' ;

// ===== WHITESPACE =====
WS : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ; // Přeskočí vše od // až do konce řádku