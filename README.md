# sql2spl
This is a simple tool to convert SQL queries to SPL queries.

## Generate Antlr Parser and Visitor (commited)
`parser/Sql.g4` is the grammar file of SQL. You can modify it to support more SQL syntax.

**NOTED: IT IS NOT A STANDARD SQL GRAMMAR FILE, IT ONLY SUPPORTS A PART OF SQL SYNTAX AND CONTAINS SOME NEW SYNTAX.**

```
poetry run antlr4 -Dlanguage=Python3 -visitor sql2spl/parser/Sql.g4
```
This step will generate files:
- parser/Sql.interp
- parser/Sql.tokens
- parser/SqlLexer.interp
- parser/SqlLexer.py
- parser/SqlLexer.tokens
- parser/SqlListener.py
- parser/SqlParser.py
- parser/SqlVisitor.py

You need to execute this command When you change `Sql.g4`. And change `queryTranslatorVisitor.py` related method.

## Build
```
just all
```

## Test
```
just test

```

## CLI Usage
```
just run
```
demo:
```
Input > select * from main
Output >  index=main | fields *
Input > select avg(aaa) from main group by bbb
Output >  index=main | stats avg(aaa) by bbb
Input > select distinct col_a, col_b, distinct col_c from db
Output >  index=db | fields col_a, col_b, col_c | dedup col_a, col_c
```