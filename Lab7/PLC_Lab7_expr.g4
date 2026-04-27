grammar PLC_Lab7_expr;

/** The start rule; begin parsing here. */
prog: stat+;

stat: expr ';'NEWLINE         
	| ID '=' expr ';'NEWLINE  
    | NEWLINE              
    ;

expr: expr op=('*'|'/') expr  # mulDiv
    | expr op=('+'|'-') expr  # addSub
    | INT                   # int    
    | OCT                   # oct
    | HEX                   # hex              
    | ID                    # id
    | '(' expr ')'          # parens
    ;

ID : [a-zA-Z]+ ;        // match identifiers
INT : [1-9][0-9]* ;     // match integers
OCT : '0'[0-7]+ ;       //match oct
HEX : '0x'[0-9a-fA-F]+ ;//match hex
NEWLINE:'\r'? '\n' ;    // return newlines to parser (is end-statement signal)
WS : [ \t]+ -> skip ;   // toss out whitespace