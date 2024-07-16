# Generated from sql.g4 by ANTLR 4.8
from antlr4 import *
from sql2spl.queryNode import fieldItem, evalItem, statsItem, sortField, joinedField
from sql2spl.parser.sqlParser import SqlParser

# This class defines a complete generic visitor for a parse tree produced by SqlParser.


class sqlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SqlParser#queryStatement.
    def visitQueryStatement(self, ctx: SqlParser.QueryStatementContext):
        queryCount = (ctx.getChildCount() + 1) // 2
        res = self.visit(ctx.querySpecification(0))
        for i in range(1, queryCount):
            res = "%s | append [search %s]" % (res, self.visit(ctx.querySpecification(i)))
        return res

    # Visit a parse tree produced by SqlParser#unionOption.
    def visitUnionOption(self, ctx: SqlParser.UnionOptionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#querySpecification.
    def visitQuerySpecification(self, ctx: SqlParser.QuerySpecificationContext):
        tableReference = self.visit(ctx.tableReference())
        headClause = self.visit(ctx.limitClause()) if ctx.limitClause() else ""
        sortClause = self.visit(ctx.orderByClause()) if ctx.orderByClause() else ""
        groupbyClause = self.visit(ctx.groupByClause()) if ctx.groupByClause() else ""
        timeSpanClause = self.visit(ctx.timingByClause()) if ctx.timingByClause() else ""
        whereClause = self.visit(ctx.whereClause()) if ctx.whereClause() else ""
        evalClause, statsClause, fieldsClause, renameClause, dedupClause = (
            self.visit(ctx.selectList()) if ctx.selectList() else ""
        )

        if timeSpanClause:
            if groupbyClause:
                groupbyClause = groupbyClause.replace("by ", "by _time, ")
            else:
                groupbyClause = "by _time"

        return "%s%s%s%s%s%s%s%s%s%s%s" % (
            tableReference,
            whereClause,
            evalClause,
            timeSpanClause,
            statsClause,
            groupbyClause,
            fieldsClause,
            renameClause,
            dedupClause,
            sortClause,
            headClause,
        )

    # Visit a parse tree produced by SqlParser#selectList.
    def visitSelectList(self, ctx: SqlParser.SelectListContext):
        selectItemCount = (ctx.getChildCount() + 1) // 2

        fieldsQuery = []
        evalQuery = []
        renameQuery = []
        dedupQuery = []
        statsQuery = []
        for i in range(selectItemCount):
            item = self.visit(ctx.selectItem(i))
            if item.getFieldsQuery():
                fieldsQuery.append(item.getFieldsQuery())
            if item.getEvalQuery():
                evalQuery.append(item.getEvalQuery())
            if item.getDedupQuery():
                dedupQuery.append(item.getDedupQuery())
            if item.getRenameQuery():
                renameQuery.append(item.getRenameQuery())
            if item.getStatsQuery():
                statsQuery.append(item.getStatsQuery())
        fieldsQueryString = "" if fieldsQuery == [] else " | fields %s" % (", ".join(fieldsQuery))
        evalQueryString = "" if evalQuery == [] else " | eval %s" % (", ".join(evalQuery))
        dedupQueryString = "" if dedupQuery == [] else " | dedup %s" % (", ".join(dedupQuery))
        renameQueryString = "" if renameQuery == [] else " | rename %s" % (", ".join(renameQuery))
        statsQueryString = "" if statsQuery == [] else " | stats %s" % (", ".join(statsQuery))

        return evalQueryString, statsQueryString, fieldsQueryString, renameQueryString, dedupQueryString

    # Visit a parse tree produced by SqlParser#selectItem.
    def visitSelectItem(self, ctx: SqlParser.SelectItemContext):
        if ctx.simpleCol():
            item = self.visit(ctx.simpleCol())
        elif ctx.evalClause():
            item = self.visit(ctx.evalClause())
        elif ctx.functionExpression():
            item = self.visit(ctx.functionExpression())
        elif ctx.ASTERISK():
            item = fieldItem("*")
        else:
            raise Exception("Select Item should be column/function expression/eval expression")
        if ctx.selectOption():
            item.distinct = self.visit(ctx.selectOption())
        if ctx.asClause():
            item.alias = self.visit(ctx.asClause())

        return item

    # Visit a parse tree produced by SqlParser#functionExpression.
    def visitFunctionExpression(self, ctx: SqlParser.FunctionExpressionContext):
        func = self.visit(ctx.functionID())
        para = self.visit(ctx.parameterList()) if ctx.parameterList() else self.visit(ctx.evalClause())
        return statsItem(func, para)

    # Visit a parse tree produced by SqlParser#evalClause.
    def visitEvalClause(self, ctx: SqlParser.EvalClauseContext):
        expr = self.visit(ctx.evalExpression())
        return evalItem(expr)

    # Visit a parse tree produced by SqlParser#parameterList.
    def visitParameterList(self, ctx: SqlParser.ParameterListContext):
        return fieldItem(ctx.getText())

    # Visit a parse tree produced by SqlParser#parameter.
    def visitParameter(self, ctx: SqlParser.ParameterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#selectOption.
    def visitSelectOption(self, ctx: SqlParser.SelectOptionContext):
        return ctx.getText()

    # Visit a parse tree produced by SqlParser#simpleCol.
    def visitSimpleCol(self, ctx: SqlParser.SimpleColContext):
        return fieldItem(ctx.getText())

    # Visit a parse tree produced by SqlParser#functionID.
    def visitFunctionID(self, ctx: SqlParser.FunctionIDContext):
        return ctx.getText()

    # Visit a parse tree produced by SqlParser#asClause.
    def visitAsClause(self, ctx: SqlParser.AsClauseContext):
        return str(ctx.IDENTIFIER())

    # Visit a parse tree produced by SqlParser#evalExpression.
    def visitEvalExpression(self, ctx: SqlParser.EvalExpressionContext):
        return ctx.getText()[1:-1]

    # Visit a parse tree produced by SqlParser#tableReference.
    def visitTableReference(self, ctx: SqlParser.TableReferenceContext):
        if ctx.IDENTIFIER():
            return "index=%s" % ctx.IDENTIFIER()
        if ctx.joinClause():
            return self.visit(ctx.joinClause())
        if ctx.querySpecification():
            return self.visit(ctx.querySpecification())

    # Visit a parse tree produced by SqlParser#joinClause.
    def visitJoinClause(self, ctx: SqlParser.JoinClauseContext):
        table1 = str(ctx.IDENTIFIER(0))
        table2 = str(ctx.IDENTIFIER(1))
        joinOption = self.visit(ctx.joinOption())
        joinFieldsCount = (ctx.getChildCount() - 4) // 2
        joinFields = []
        renameFields = []
        for i in range(joinFieldsCount):
            joinedFieldItem = self.visit(ctx.colComparison(i))
            joinF, renameF = joinedFieldItem.getJoinedField(table1, table2)
            if joinF:
                joinFields.append(joinF)
            if renameF:
                renameFields.append(renameF)
        joinFieldsQuery = " %s" % (" ".join(joinFields))
        renameFieldsQuery = " | rename %s" % (", ".join(renameFields)) if renameFields != [] else ""

        res = "index=%s | join type=%s%s [SEARCH index=%s%s]" % (
            table1,
            joinOption,
            joinFieldsQuery,
            table2,
            renameFieldsQuery,
        )
        return res

    # Visit a parse tree produced by SqlParser#joinOption.
    def visitJoinOption(self, ctx: SqlParser.JoinOptionContext):
        return ctx.getText()

    # Visit a parse tree produced by SqlParser#colComparison.
    def visitColComparison(self, ctx: SqlParser.ColComparisonContext):
        table1 = str(ctx.IDENTIFIER(0))
        table2 = str(ctx.IDENTIFIER(1))
        field1 = self.visit(ctx.simpleCol(0))
        field2 = self.visit(ctx.simpleCol(1))
        return joinedField(table1, table2, field1, field2)

    # Visit a parse tree produced by SqlParser#whereClause.
    def visitWhereClause(self, ctx: SqlParser.WhereClauseContext):
        return " | search %s" % self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#searchCondition.
    def visitSearchCondition(self, ctx: SqlParser.SearchConditionContext):
        booleanTermCount = (ctx.getChildCount() + 1) // 2
        res = self.visit(ctx.booleanTerm(0))
        for i in range(1, booleanTermCount):
            res = "%s OR %s" % (res, self.visit(ctx.booleanTerm(i)))
        return res

    # Visit a parse tree produced by SqlParser#booleanTerm.
    def visitBooleanTerm(self, ctx: SqlParser.BooleanTermContext):
        booleanFactorCount = (ctx.getChildCount() + 1) // 2
        res = self.visit(ctx.booleanFactor(0))
        for i in range(1, booleanFactorCount):
            res = "%s AND %s" % (res, self.visit(ctx.booleanFactor(i)))
        return res

    # Visit a parse tree produced by SqlParser#negativeBooleanFactor.
    def visitNegativeBooleanFactor(self, ctx: SqlParser.NegativeBooleanFactorContext):
        return "NOT %s" % self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#positiveBooleanFactor.
    def visitPositiveBooleanFactor(self, ctx: SqlParser.PositiveBooleanFactorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#predicateBooleanTest.
    def visitPredicateBooleanTest(self, ctx: SqlParser.PredicateBooleanTestContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#parenthesisBooleanTest.
    def visitParenthesisBooleanTest(self, ctx: SqlParser.ParenthesisBooleanTestContext):
        return "(%s)" % self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#predicate.
    def visitPredicate(self, ctx: SqlParser.PredicateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#containsExpression.
    def visitContainsExpression(self, ctx: SqlParser.ContainsExpressionContext):
        string_count = (ctx.getChildCount() - 2) // 2
        res = str(ctx.ANY_STRING(0))
        if not res.isdigit() and not res.islower():
            res = "CASE(%s)" % (res)
        for i in range(1, string_count):
            tmp = str(ctx.ANY_STRING(i))
            if not tmp.islower():
                res = "%s CASE(%s)" % (res, tmp)
            else:
                res = "%s %s" % (res, tmp)
        return res

    # Visit a parse tree produced by SqlParser#comparisonPredicate.
    def visitComparisonPredicate(self, ctx: SqlParser.ComparisonPredicateContext):
        return ctx.getText()

    # Visit a parse tree produced by SqlParser#betweenPredicate.
    def visitBetweenPredicate(self, ctx: SqlParser.BetweenPredicateContext):
        expr1 = self.visit(ctx.valueExpression(0))
        expr2 = self.visit(ctx.valueExpression(1))
        expr3 = self.visit(ctx.valueExpression(2))
        if ctx.KW_NOT():
            return "%s<=%s AND %s>=%s" % (expr1, expr2, expr1, expr3)
        else:
            return "%s>%s AND %s<%s" % (expr1, expr2, expr1, expr3)

    # Visit a parse tree produced by SqlParser#inPredicate.
    def visitInPredicate(self, ctx: SqlParser.InPredicateContext):
        expr = self.visit(ctx.valueExpression())
        inValueList = self.visit(ctx.inValueList())
        return "%s IN (%s)" % (expr, inValueList)

    # Visit a parse tree produced by SqlParser#inValueList.
    def visitInValueList(self, ctx: SqlParser.InValueListContext):
        return ctx.getText()

    # Visit a parse tree produced by SqlParser#valueExpression.
    def visitValueExpression(self, ctx: SqlParser.ValueExpressionContext):
        return ctx.getText()

    # Visit a parse tree produced by SqlParser#literal.
    def visitLiteral(self, ctx: SqlParser.LiteralContext):
        return ctx.getText()

    # Visit a parse tree produced by SqlParser#generalLiteral.
    def visitGeneralLiteral(self, ctx: SqlParser.GeneralLiteralContext):
        return ctx.getText()

    # Visit a parse tree produced by SqlParser#characterStringLiteral.
    def visitCharacterStringLiteral(self, ctx: SqlParser.CharacterStringLiteralContext):
        return ctx.getText()

    # Visit a parse tree produced by SqlParser#signedNumericLiteral.
    def visitSignedNumericLiteral(self, ctx: SqlParser.SignedNumericLiteralContext):
        return ctx.getText()

    # Visit a parse tree produced by SqlParser#sign.
    def visitSign(self, ctx: SqlParser.SignContext):
        return ctx.getText()

    # Visit a parse tree produced by SqlParser#unsignedNumericLiteral.
    def visitUnsignedNumericLiteral(self, ctx: SqlParser.UnsignedNumericLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#exactNumericLiteral.
    def visitExactNumericLiteral(self, ctx: SqlParser.ExactNumericLiteralContext):
        return ctx.getText()

    # Visit a parse tree produced by SqlParser#groupByClause.
    def visitGroupByClause(self, ctx: SqlParser.GroupByClauseContext):
        return " by %s" % self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#columnList.
    def visitColumnList(self, ctx: SqlParser.ColumnListContext):
        res = ", ".join(ctx.getText().split(","))
        return res

    # Visit a parse tree produced by SqlParser#orderByClause.
    def visitOrderByClause(self, ctx: SqlParser.OrderByClauseContext):
        orderItemCount = (ctx.getChildCount() - 1) // 2
        res = str(self.visit(ctx.orderItem(0)))
        for i in range(1, orderItemCount):
            res = "%s, %s" % (res, self.visit(ctx.orderItem(i)))
        return " | sort %s" % res

    # Visit a parse tree produced by SqlParser#orderItem.
    def visitOrderItem(self, ctx: SqlParser.OrderItemContext):
        orderOption = self.visit(ctx.orderOption()) if ctx.orderOption() else ""
        orderItem = str(ctx.IDENTIFIER())
        return sortField(orderItem, orderOption)

    # Visit a parse tree produced by SqlParser#orderOption.
    def visitOrderOption(self, ctx: SqlParser.OrderOptionContext):
        return ctx.getText()

    # Visit a parse tree produced by SqlParser#timingByClause.
    def visitTimingByClause(self, ctx: SqlParser.TimingByClauseContext):
        # print("timing by text: ", ctx.getText())
        timeNum = ctx.UNSIGNED_INTEGER()
        timeUnit = self.visit(ctx.timeSpanUnit())
        return " | bin _time span=%s%s" % (timeNum, timeUnit)

    # Visit a parse tree produced by SqlParser#timeSpanUnit.
    def visitTimeSpanUnit(self, ctx: SqlParser.TimeSpanUnitContext):
        return ctx.getText()

    # Visit a parse tree produced by SqlParser#limitClause.
    def visitLimitClause(self, ctx: SqlParser.LimitClauseContext):
        return " | head %s" % (ctx.UNSIGNED_INTEGER())


del SqlParser
