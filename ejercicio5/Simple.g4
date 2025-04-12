grammar Simple;

prog: classDef+ ;

classDef
    : 'class' ID '{' member+ '}' 
    ;

member
    : 'int' ID ';'
    | 'int' ID '(' ID ')' '{' stat '}' 
    ;

stat
    : expr ';'
    | ID '=' expr ';'
    ;

expr
    : expr ('+' | '-') expr   # AddSub   // Suma y Resta
    | expr ('*' | '/') expr   # MulDiv   // Multiplicación y División
    | INT                     # Int      // Número entero
    | ID '(' INT ')'           # FuncCall // Llamada a función
    | ID                       # Var      // Identificador (Variable)
    | '(' expr ')'             # Parens   // Expresión entre paréntesis
    ;


INT : [0-9]+ ;
ID  : [a-zA-Z]+ ;
WS  : [ \t\r\n]+ -> skip ;