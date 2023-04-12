grammar Expr;

root : stat EOF ;

stat : asign | comp | expr | condicional | whileCondition | func | callfunc | blocop
    ;

expr : expr ('*'|'/'|'%') expr # MulDivMod
    | expr('+'|'-') expr # SumaResta
    | NUM # Valor
    | VAR # Variable
    ;

comp : expr ('>'|'<'|'>='|'<='|'='|'!=') expr # Compar;

asign : VAR '<-' expr # Assig;

func: FUNCNAME VAR* blocop #Function;

callfunc : FUNCNAME expr* #CallFunc;

condicional : 'if' comp blocop ('else' blocop)? # Ifcondition;

whileCondition : 'while' comp blocop # Whileoperation;

blocop : '{' stat+ '}' #Bloc;

NUM : [0-9]+ ;

FUNCNAME : [A-Z][a-z]* ;

VAR : [a-z]+ ;

WS : [ \n]+ -> skip ;
