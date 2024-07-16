# Generated from sql2spl/parser/Sql.g4 by ANTLR 4.13.1
from antlr4 import *

if "." in __name__:
    from .SqlParser import SqlParser
else:
    from SqlParser import SqlParser

# This class defines a complete generic visitor for a parse tree produced by SqlParser.


class SqlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SqlParser#queryStatement.
    def visitQueryStatement(self, ctx: SqlParser.QueryStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#unionOption.
    def visitUnionOption(self, ctx: SqlParser.UnionOptionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#querySpecification.
    def visitQuerySpecification(self, ctx: SqlParser.QuerySpecificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#selectList.
    def visitSelectList(self, ctx: SqlParser.SelectListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#selectItem.
    def visitSelectItem(self, ctx: SqlParser.SelectItemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#functionExpression.
    def visitFunctionExpression(self, ctx: SqlParser.FunctionExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#evalClause.
    def visitEvalClause(self, ctx: SqlParser.EvalClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#parameterList.
    def visitParameterList(self, ctx: SqlParser.ParameterListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#parameter.
    def visitParameter(self, ctx: SqlParser.ParameterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#selectOption.
    def visitSelectOption(self, ctx: SqlParser.SelectOptionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#simpleCol.
    def visitSimpleCol(self, ctx: SqlParser.SimpleColContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#functionID.
    def visitFunctionID(self, ctx: SqlParser.FunctionIDContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#asClause.
    def visitAsClause(self, ctx: SqlParser.AsClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#evalExpression.
    def visitEvalExpression(self, ctx: SqlParser.EvalExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#tableReference.
    def visitTableReference(self, ctx: SqlParser.TableReferenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#joinClause.
    def visitJoinClause(self, ctx: SqlParser.JoinClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#joinOption.
    def visitJoinOption(self, ctx: SqlParser.JoinOptionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#colComparison.
    def visitColComparison(self, ctx: SqlParser.ColComparisonContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#whereClause.
    def visitWhereClause(self, ctx: SqlParser.WhereClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#searchCondition.
    def visitSearchCondition(self, ctx: SqlParser.SearchConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#booleanTerm.
    def visitBooleanTerm(self, ctx: SqlParser.BooleanTermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#negativeBooleanFactor.
    def visitNegativeBooleanFactor(self, ctx: SqlParser.NegativeBooleanFactorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#positiveBooleanFactor.
    def visitPositiveBooleanFactor(self, ctx: SqlParser.PositiveBooleanFactorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#predicateBooleanTest.
    def visitPredicateBooleanTest(self, ctx: SqlParser.PredicateBooleanTestContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#parenthesisBooleanTest.
    def visitParenthesisBooleanTest(self, ctx: SqlParser.ParenthesisBooleanTestContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#predicate.
    def visitPredicate(self, ctx: SqlParser.PredicateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#containsExpression.
    def visitContainsExpression(self, ctx: SqlParser.ContainsExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#comparisonPredicate.
    def visitComparisonPredicate(self, ctx: SqlParser.ComparisonPredicateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#betweenPredicate.
    def visitBetweenPredicate(self, ctx: SqlParser.BetweenPredicateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#inPredicate.
    def visitInPredicate(self, ctx: SqlParser.InPredicateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#inValueList.
    def visitInValueList(self, ctx: SqlParser.InValueListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#valueExpression.
    def visitValueExpression(self, ctx: SqlParser.ValueExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#literal.
    def visitLiteral(self, ctx: SqlParser.LiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#generalLiteral.
    def visitGeneralLiteral(self, ctx: SqlParser.GeneralLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#characterStringLiteral.
    def visitCharacterStringLiteral(self, ctx: SqlParser.CharacterStringLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#signedNumericLiteral.
    def visitSignedNumericLiteral(self, ctx: SqlParser.SignedNumericLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#sign.
    def visitSign(self, ctx: SqlParser.SignContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#unsignedNumericLiteral.
    def visitUnsignedNumericLiteral(self, ctx: SqlParser.UnsignedNumericLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#exactNumericLiteral.
    def visitExactNumericLiteral(self, ctx: SqlParser.ExactNumericLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#groupByClause.
    def visitGroupByClause(self, ctx: SqlParser.GroupByClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#columnList.
    def visitColumnList(self, ctx: SqlParser.ColumnListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#orderByClause.
    def visitOrderByClause(self, ctx: SqlParser.OrderByClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#orderItem.
    def visitOrderItem(self, ctx: SqlParser.OrderItemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#orderOption.
    def visitOrderOption(self, ctx: SqlParser.OrderOptionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#timingByClause.
    def visitTimingByClause(self, ctx: SqlParser.TimingByClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#timeSpanUnit.
    def visitTimeSpanUnit(self, ctx: SqlParser.TimeSpanUnitContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SqlParser#limitClause.
    def visitLimitClause(self, ctx: SqlParser.LimitClauseContext):
        return self.visitChildren(ctx)


del SqlParser
