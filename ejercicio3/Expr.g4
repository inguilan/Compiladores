grammar Expr;
root : expr EOF;
expr : expr MAS expr
	| NUM
	;
NUM : [0-9]+;
MAS : '+';
WS: [\n]+ -> skip;