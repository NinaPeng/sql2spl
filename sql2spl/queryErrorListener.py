from antlr4.Token import Token
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import (
    RecognitionException,
    NoViableAltException,
    InputMismatchException,
    FailedPredicateException,
)


class QueryException(Exception):
    pass


class queryErrorListener(ErrorListener):
    symbolicNames = [
        "<INVALID>",
        '"select"',
        '"as"',
        '"from"',
        '"where"',
        '"or"',
        '"and"',
        '"not"',
        '"between"',
        '"in"',
        '"all"',
        '"distinct"',
        '"union"',
        '"by"',
        '"left"',
        '"inner"',
        '"join"',
        '"eval"',
        '"on"',
        '"order"',
        '"desc"',
        '"asc"',
        '"timing"',
        '"limit"',
        '"group"',
        '"contains"',
        "*",
        ",",
        ".",
        "+",
        "-",
        "/",
        '"s"',
        '"min"',
        '"ns"',
        '"hour"',
        '"day"',
        '"mon"',
        '"w"',
        "<identifier>",
        "(",
        ")",
        "=",
        "<comparison operator>",
        "<integer>",
        "<quoted string>",
        "'",
        '"',
        '\\"',
        "<string or expression>",
        "WHITESPACE",
    ]

    def handleNoViableAltException(self, recognizer, offendingSymbol, line, column, msg, e):
        tokens = recognizer.getTokenStream()
        if tokens is not None:
            if e.startToken.type == Token.EOF:
                input_string = "<EOF>"
            else:
                input_string = tokens.getText(e.startToken, e.offendingToken)
        else:
            input_string = "<unknown input>"
        msg = "Syntax Error: can not recoginize at line %s:%s '%s'" % (line, column, input_string)
        raise QueryException(msg)

    def handleInputMismatchException(self, recognizer, offendingSymbol, line, column, msg, e):
        if offendingSymbol is None:
            input_string = "<None>"
        input_string = offendingSymbol.text
        if input_string is None:
            if offendingSymbol.type == Token.EOF:
                input_string = "<EOF>"
            else:
                input_string = "<" + str(offendingSymbol.type) + ">"
        ruleName = recognizer.ruleNames[recognizer._ctx.getRuleIndex()]
        msg = "Syntax Error: missing input at line %s:%s '%s', expecting '%s'" % (
            line,
            column,
            input_string,
            e.getExpectedTokens().toString(recognizer.literalNames, self.symbolicNames),
        )
        raise QueryException(msg)

    def handleFailedPredicateException(self, recognizer, offendingSymbol, line, column, msg, e):
        ruleName = recognizer.ruleNames[recognizer._ctx.getRuleIndex()]
        msg = "ANTLR4 Parse Error: rule %s %s" % (ruleName, msg)
        raise QueryException(msg)

    def handleOtherException(self, recognizer, offendingSymbol, line, column, msg, e):
        if offendingSymbol is None:
            input_string = "<None>"
        input_string = offendingSymbol.text
        if input_string is None:
            if offendingSymbol.type == Token.EOF:
                input_string = "<EOF>"
            else:
                input_string = "<" + str(offendingSymbol.type) + ">"
        try:
            msg = "Syntax Error: near '%s' expecting %s" % (
                input_string,
                recognizer.getExpectedTokens().toString(recognizer.literalNames, self.symbolicNames),
            )
        except:
            msg = "Syntax Error: near '%s'" % (input_string)
        raise QueryException(msg)

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if isinstance(e, NoViableAltException):
            self.handleNoViableAltException(recognizer, offendingSymbol, line, column, msg, e)
        elif isinstance(e, InputMismatchException):
            self.handleInputMismatchException(recognizer, offendingSymbol, line, column, msg, e)
        elif isinstance(e, FailedPredicateException):
            self.handleFailedPredicateException(recognizer, offendingSymbol, line, column, msg, e)
        else:
            self.handleOtherException(recognizer, offendingSymbol, line, column, msg, e)
