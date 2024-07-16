import sys
from antlr4 import *
from sql2spl.parser.sqlLexer import SqlLexer
from sql2spl.parser.sqlParser import SqlParser
from sql2spl.queryTranslatorVisitor import sqlVisitor
from sql2spl.queryErrorListener import queryErrorListener


def queryTranslator(input_string):
    text = InputStream(input_string)
    lexer = SqlLexer(text)
    stream = CommonTokenStream(lexer)
    parser = SqlParser(stream)
    tree = parser.queryStatement()
    output_string = sqlVisitor().visit(tree)
    return output_string


def main():
    while True:
        text = input("Input > ")
        if text == "q":
            exit(0)
        text = text.strip()
        text = text.strip("\r\n")
        if not text:
            continue
        text = InputStream(text)
        lexer = SqlLexer(text)
        stream = CommonTokenStream(lexer)
        parser = SqlParser(stream)
        parser.addErrorListener(queryErrorListener())
        try:
            tree = parser.queryStatement()
        except Exception as e:
            print("Exception: %s" % str(e))
            continue
        res = sqlVisitor().visit(tree)
        print("Output > ", res)


if __name__ == "__main__":
    main()
