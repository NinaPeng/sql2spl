grammar Sql;

/***************** 
 *  Parser Rules
 ******************/

queryStatement
    : querySpecification (unionOption querySpecification)*
    ;

unionOption
    : KW_UNION
    | KW_UNION KW_ALL
    ;

querySpecification
    : KW_SELECT selectList KW_FROM tableReference whereClause?
    ( groupByClause
    | groupByClause timingByClause
    | timingByClause
    | timingByClause groupByClause)?
    orderByClause? limitClause?
    ;

selectList
    : selectItem (COMMA selectItem)*
    ;

selectItem
    : ASTERISK
    | functionExpression asClause?
    | selectOption? simpleCol asClause?
    | selectOption? evalClause asClause?
    ;

functionExpression
    : functionID OPEN_PARENTHESIS (parameterList | evalClause) CLOSE_PARENTHESIS
    ;

evalClause
    : KW_EVAL OPEN_PARENTHESIS evalExpression CLOSE_PARENTHESIS
    ;

parameterList
    : parameter (COMMA parameter)*
    ;

parameter
    : IDENTIFIER
    | DOUBLE_QUOTE IDENTIFIER DOUBLE_QUOTE
    | literal
    ;

selectOption
    : KW_DISTINCT
    ;

simpleCol
    : IDENTIFIER (PERIOD IDENTIFIER)*
    ;

functionID
    : IDENTIFIER
    ;

asClause
    : KW_AS IDENTIFIER
    ;

evalExpression
    : ANY_STRING
    ;

tableReference
    : IDENTIFIER
    | OPEN_PARENTHESIS querySpecification CLOSE_PARENTHESIS
    | joinClause
    ;

joinClause
    : IDENTIFIER joinOption KW_JOIN IDENTIFIER (KW_ON colComparison*)?
    ;

joinOption
    : KW_LEFT
    | KW_INNER
    ;

colComparison
    : IDENTIFIER PERIOD simpleCol EQUALS IDENTIFIER PERIOD simpleCol
    ;

whereClause
    : KW_WHERE searchCondition
    ;

searchCondition
	: booleanTerm (KW_OR booleanTerm)*
	;

booleanTerm
	: booleanFactor (KW_AND booleanFactor)*
	;

booleanFactor
	: KW_NOT booleanTest        # negativeBooleanFactor
	| booleanTest               # positiveBooleanFactor
	;

booleanTest
	: predicate                                             # predicateBooleanTest
	| OPEN_PARENTHESIS searchCondition CLOSE_PARENTHESIS    # parenthesisBooleanTest
	;

predicate
	: containsExpression
    | comparisonPredicate
	| betweenPredicate
	| inPredicate
	| functionExpression
	;

containsExpression
    : KW_CONTAINS OPEN_PARENTHESIS ANY_STRING (COMMA ANY_STRING)* CLOSE_PARENTHESIS
    ;

comparisonPredicate
    : valueExpression COMP_OPERATOR literal
    | valueExpression EQUALS ( literal | ANY_STRING )
    ;

betweenPredicate
    : valueExpression (KW_NOT)? KW_BETWEEN valueExpression KW_AND valueExpression
    ;

inPredicate
    : valueExpression KW_IN OPEN_PARENTHESIS inValueList CLOSE_PARENTHESIS
    ;

inValueList
    : valueExpression (COMMA valueExpression)*
    ;

valueExpression
    : simpleCol
    | literal
    ;

literal
    : signedNumericLiteral
    | generalLiteral
    ;

generalLiteral
    : characterStringLiteral
    ;

characterStringLiteral
    : QUOTED_STRING
    ;

signedNumericLiteral
	: sign unsignedNumericLiteral
	| unsignedNumericLiteral
	;

sign
	: PLUS_SIGN
	| MINUS_SIGN
	;

unsignedNumericLiteral
	: exactNumericLiteral
	;

exactNumericLiteral
	: UNSIGNED_INTEGER PERIOD UNSIGNED_INTEGER
	| PERIOD UNSIGNED_INTEGER
	| UNSIGNED_INTEGER
	;

groupByClause
    : KW_GROUP KW_BY columnList
    ;

columnList
    : IDENTIFIER (COMMA IDENTIFIER)*
    ;

orderByClause
    : KW_ORDER KW_BY orderItem (COMMA orderItem)*
    ;

orderItem
    : IDENTIFIER orderOption?
    ;

orderOption
    : KW_DESC
    | KW_ASC
    ;

timingByClause
    : KW_TIMING KW_BY UNSIGNED_INTEGER timeSpanUnit
    ;

timeSpanUnit
    : SEC_TIME_UNIT
    | MIN_TIME_UNIT
    | HOUR_TIME_UNIT
    | DAY_TIME_UNIT
    | WEEK_TIME_UNIT
    | MONTH_TIME_UNIT
    | SUBSECONDS_TIME_UNIT
    ;

limitClause
    : KW_LIMIT UNSIGNED_INTEGER 
    ;


/*****************
 *  Lexer Rules
 ******************/
KW_SELECT
    : S E L E C T
    ;

KW_AS
    : A S
    ;

KW_FROM
    : F R O M
    ;

KW_WHERE
    : W H E R E
    ;

KW_OR
    : O R
    ;

KW_AND
    : A N D
    ;

KW_NOT
    : N O T
    ;

KW_BETWEEN
    : B E T W E E N
    ;

KW_IN
    : I N
    ;

KW_ALL
    : A L L
    ;

KW_DISTINCT
    : D I S T I N C T
    ;

KW_UNION
    : U N I O N 
    ;

KW_BY
    : B Y 
    ;
KW_LEFT
    : L E F T 
    ;

KW_INNER
    : I N N E R 
    ;

KW_JOIN
    : J O I N 
    ;

KW_EVAL
    : E V A L 
    ;

KW_ON 
    : O N 
    ;

KW_ORDER 
    : O R D E R 
    ;

KW_DESC 
    : D E S C 
    ;

KW_ASC 
    : A S C 
    ;

KW_TIMING 
    : T I M I N G 
    ;

KW_LIMIT
    : L I M I T 
    ;

KW_GROUP
    : G R O U P 
    ;

KW_CONTAINS
    : C O N T A I N S 
    ;

ASTERISK
    : '*'
    ;

COMMA
    : ','
    ;

PERIOD
    : '.'
    ;

PLUS_SIGN
    : '+'
    ;

MINUS_SIGN
    : '-'
    ;

DIV_SIGN
    : '/'
    ;

SEC_TIME_UNIT
    : S
    | S E C 
    | S E C S 
    | S E C O N D 
    | S E C O N D S
    ;

MIN_TIME_UNIT
    : M 
    | M I N 
    | M I N S 
    | M I N U T E 
    | M I N U T E S
    ;

SUBSECONDS_TIME_UNIT
    : U S
    | M S 
    | C S 
    | D S 
    ;

HOUR_TIME_UNIT
    : H 
    | H R 
    | H R S 
    | H O U R 
    | H O U R S
    ;

DAY_TIME_UNIT
    : D 
    | D A Y 
    | D A Y S
    ;

MONTH_TIME_UNIT
    : M O N 
    | M O N T H 
    | M O N T H S 
    ;

WEEK_TIME_UNIT
    : W 
    | W E E K 
    | W E E K S
    ;

// the first character must be simple latin or underscore so that it will not be ambiguous with a sign integer like 100/-29
IDENTIFIER
    : (SIMPLE_LATIN | UNDERSCORE)+ (ATTRIBUTE_NAME_CHAR)*
    ;

OPEN_PARENTHESIS
	: '('
	;

CLOSE_PARENTHESIS
	: ')'
	;

EQUALS
    : '='
    ;

COMP_OPERATOR
	: '<>'
	| '<'
	| '<='
	| '>'
	| '>='
	;

UNSIGNED_INTEGER
	: (DIGIT)+
	;

QUOTED_STRING
    : QUOTE (CHAR_REPRESENTATION)* QUOTE
    ;

QUOTE
    : '\''
    ;

DOUBLE_QUOTE
    : '"'
    ;

ESCAPED_DOUBLE_QUOTE
    : '\\"'
    ;

ANY_STRING 
    : '"' ( STRING_ESCAPE_SEQ | ~[\\\r\n\f"] )* '"'
    | '\'' ( STRING_ESCAPE_SEQ | ~[\\\r\n\f'] )* '\''
    ;

fragment 
STRING_ESCAPE_SEQ
    : '\\' .
    ;

fragment
CHAR_REPRESENTATION
    : NON_QUOTE_CHAR
    | QUOTE_SYMBOL
    ;

fragment
NON_QUOTE_CHAR
    : '\u0000' .. '\u0026'
    | '\u0028' .. '\ufffe'
    ;

fragment
// escaped quote symbol in string literal
QUOTE_SYMBOL
    : '\'\''
    ;

fragment
ATTRIBUTE_NAME_CHAR
    : SIMPLE_LATIN
    | MINUS_SIGN
    | DIGIT
    | UNDERSCORE
    ;

fragment
DIGIT
    : [0-9]
    ;

fragment
UNDERSCORE
    : '_'
    ;

fragment
SIMPLE_LATIN
    : 'A' .. 'Z'
    | 'a' .. 'z'
    ;

WHITESPACE
    : [ \t\n\r]+ -> skip
    ;

// case insensitive matching keywords
fragment A : [aA]; // match either an 'a' or 'A'
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];
