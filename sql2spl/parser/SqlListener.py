# Generated from sql2spl/parser/Sql.g4 by ANTLR 4.13.1
from antlr4 import *

if "." in __name__:
    from .SqlParser import SqlParser
else:
    from SqlParser import SqlParser


# This class defines a complete listener for a parse tree produced by SqlParser.
class SqlListener(ParseTreeListener):

    # Enter a parse tree produced by SqlParser#queryStatement.
    def enterQueryStatement(self, ctx: SqlParser.QueryStatementContext):
        pass

    # Exit a parse tree produced by SqlParser#queryStatement.
    def exitQueryStatement(self, ctx: SqlParser.QueryStatementContext):
        pass

    # Enter a parse tree produced by SqlParser#unionOption.
    def enterUnionOption(self, ctx: SqlParser.UnionOptionContext):
        pass

    # Exit a parse tree produced by SqlParser#unionOption.
    def exitUnionOption(self, ctx: SqlParser.UnionOptionContext):
        pass

    # Enter a parse tree produced by SqlParser#querySpecification.
    def enterQuerySpecification(self, ctx: SqlParser.QuerySpecificationContext):
        pass

    # Exit a parse tree produced by SqlParser#querySpecification.
    def exitQuerySpecification(self, ctx: SqlParser.QuerySpecificationContext):
        pass

    # Enter a parse tree produced by SqlParser#selectList.
    def enterSelectList(self, ctx: SqlParser.SelectListContext):
        pass

    # Exit a parse tree produced by SqlParser#selectList.
    def exitSelectList(self, ctx: SqlParser.SelectListContext):
        pass

    # Enter a parse tree produced by SqlParser#selectItem.
    def enterSelectItem(self, ctx: SqlParser.SelectItemContext):
        pass

    # Exit a parse tree produced by SqlParser#selectItem.
    def exitSelectItem(self, ctx: SqlParser.SelectItemContext):
        pass

    # Enter a parse tree produced by SqlParser#functionExpression.
    def enterFunctionExpression(self, ctx: SqlParser.FunctionExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#functionExpression.
    def exitFunctionExpression(self, ctx: SqlParser.FunctionExpressionContext):
        pass

    # Enter a parse tree produced by SqlParser#evalClause.
    def enterEvalClause(self, ctx: SqlParser.EvalClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#evalClause.
    def exitEvalClause(self, ctx: SqlParser.EvalClauseContext):
        pass

    # Enter a parse tree produced by SqlParser#parameterList.
    def enterParameterList(self, ctx: SqlParser.ParameterListContext):
        pass

    # Exit a parse tree produced by SqlParser#parameterList.
    def exitParameterList(self, ctx: SqlParser.ParameterListContext):
        pass

    # Enter a parse tree produced by SqlParser#parameter.
    def enterParameter(self, ctx: SqlParser.ParameterContext):
        pass

    # Exit a parse tree produced by SqlParser#parameter.
    def exitParameter(self, ctx: SqlParser.ParameterContext):
        pass

    # Enter a parse tree produced by SqlParser#selectOption.
    def enterSelectOption(self, ctx: SqlParser.SelectOptionContext):
        pass

    # Exit a parse tree produced by SqlParser#selectOption.
    def exitSelectOption(self, ctx: SqlParser.SelectOptionContext):
        pass

    # Enter a parse tree produced by SqlParser#simpleCol.
    def enterSimpleCol(self, ctx: SqlParser.SimpleColContext):
        pass

    # Exit a parse tree produced by SqlParser#simpleCol.
    def exitSimpleCol(self, ctx: SqlParser.SimpleColContext):
        pass

    # Enter a parse tree produced by SqlParser#functionID.
    def enterFunctionID(self, ctx: SqlParser.FunctionIDContext):
        pass

    # Exit a parse tree produced by SqlParser#functionID.
    def exitFunctionID(self, ctx: SqlParser.FunctionIDContext):
        pass

    # Enter a parse tree produced by SqlParser#asClause.
    def enterAsClause(self, ctx: SqlParser.AsClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#asClause.
    def exitAsClause(self, ctx: SqlParser.AsClauseContext):
        pass

    # Enter a parse tree produced by SqlParser#evalExpression.
    def enterEvalExpression(self, ctx: SqlParser.EvalExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#evalExpression.
    def exitEvalExpression(self, ctx: SqlParser.EvalExpressionContext):
        pass

    # Enter a parse tree produced by SqlParser#tableReference.
    def enterTableReference(self, ctx: SqlParser.TableReferenceContext):
        pass

    # Exit a parse tree produced by SqlParser#tableReference.
    def exitTableReference(self, ctx: SqlParser.TableReferenceContext):
        pass

    # Enter a parse tree produced by SqlParser#joinClause.
    def enterJoinClause(self, ctx: SqlParser.JoinClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#joinClause.
    def exitJoinClause(self, ctx: SqlParser.JoinClauseContext):
        pass

    # Enter a parse tree produced by SqlParser#joinOption.
    def enterJoinOption(self, ctx: SqlParser.JoinOptionContext):
        pass

    # Exit a parse tree produced by SqlParser#joinOption.
    def exitJoinOption(self, ctx: SqlParser.JoinOptionContext):
        pass

    # Enter a parse tree produced by SqlParser#colComparison.
    def enterColComparison(self, ctx: SqlParser.ColComparisonContext):
        pass

    # Exit a parse tree produced by SqlParser#colComparison.
    def exitColComparison(self, ctx: SqlParser.ColComparisonContext):
        pass

    # Enter a parse tree produced by SqlParser#whereClause.
    def enterWhereClause(self, ctx: SqlParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#whereClause.
    def exitWhereClause(self, ctx: SqlParser.WhereClauseContext):
        pass

    # Enter a parse tree produced by SqlParser#searchCondition.
    def enterSearchCondition(self, ctx: SqlParser.SearchConditionContext):
        pass

    # Exit a parse tree produced by SqlParser#searchCondition.
    def exitSearchCondition(self, ctx: SqlParser.SearchConditionContext):
        pass

    # Enter a parse tree produced by SqlParser#booleanTerm.
    def enterBooleanTerm(self, ctx: SqlParser.BooleanTermContext):
        pass

    # Exit a parse tree produced by SqlParser#booleanTerm.
    def exitBooleanTerm(self, ctx: SqlParser.BooleanTermContext):
        pass

    # Enter a parse tree produced by SqlParser#negativeBooleanFactor.
    def enterNegativeBooleanFactor(self, ctx: SqlParser.NegativeBooleanFactorContext):
        pass

    # Exit a parse tree produced by SqlParser#negativeBooleanFactor.
    def exitNegativeBooleanFactor(self, ctx: SqlParser.NegativeBooleanFactorContext):
        pass

    # Enter a parse tree produced by SqlParser#positiveBooleanFactor.
    def enterPositiveBooleanFactor(self, ctx: SqlParser.PositiveBooleanFactorContext):
        pass

    # Exit a parse tree produced by SqlParser#positiveBooleanFactor.
    def exitPositiveBooleanFactor(self, ctx: SqlParser.PositiveBooleanFactorContext):
        pass

    # Enter a parse tree produced by SqlParser#predicateBooleanTest.
    def enterPredicateBooleanTest(self, ctx: SqlParser.PredicateBooleanTestContext):
        pass

    # Exit a parse tree produced by SqlParser#predicateBooleanTest.
    def exitPredicateBooleanTest(self, ctx: SqlParser.PredicateBooleanTestContext):
        pass

    # Enter a parse tree produced by SqlParser#parenthesisBooleanTest.
    def enterParenthesisBooleanTest(self, ctx: SqlParser.ParenthesisBooleanTestContext):
        pass

    # Exit a parse tree produced by SqlParser#parenthesisBooleanTest.
    def exitParenthesisBooleanTest(self, ctx: SqlParser.ParenthesisBooleanTestContext):
        pass

    # Enter a parse tree produced by SqlParser#predicate.
    def enterPredicate(self, ctx: SqlParser.PredicateContext):
        pass

    # Exit a parse tree produced by SqlParser#predicate.
    def exitPredicate(self, ctx: SqlParser.PredicateContext):
        pass

    # Enter a parse tree produced by SqlParser#containsExpression.
    def enterContainsExpression(self, ctx: SqlParser.ContainsExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#containsExpression.
    def exitContainsExpression(self, ctx: SqlParser.ContainsExpressionContext):
        pass

    # Enter a parse tree produced by SqlParser#comparisonPredicate.
    def enterComparisonPredicate(self, ctx: SqlParser.ComparisonPredicateContext):
        pass

    # Exit a parse tree produced by SqlParser#comparisonPredicate.
    def exitComparisonPredicate(self, ctx: SqlParser.ComparisonPredicateContext):
        pass

    # Enter a parse tree produced by SqlParser#betweenPredicate.
    def enterBetweenPredicate(self, ctx: SqlParser.BetweenPredicateContext):
        pass

    # Exit a parse tree produced by SqlParser#betweenPredicate.
    def exitBetweenPredicate(self, ctx: SqlParser.BetweenPredicateContext):
        pass

    # Enter a parse tree produced by SqlParser#inPredicate.
    def enterInPredicate(self, ctx: SqlParser.InPredicateContext):
        pass

    # Exit a parse tree produced by SqlParser#inPredicate.
    def exitInPredicate(self, ctx: SqlParser.InPredicateContext):
        pass

    # Enter a parse tree produced by SqlParser#inValueList.
    def enterInValueList(self, ctx: SqlParser.InValueListContext):
        pass

    # Exit a parse tree produced by SqlParser#inValueList.
    def exitInValueList(self, ctx: SqlParser.InValueListContext):
        pass

    # Enter a parse tree produced by SqlParser#valueExpression.
    def enterValueExpression(self, ctx: SqlParser.ValueExpressionContext):
        pass

    # Exit a parse tree produced by SqlParser#valueExpression.
    def exitValueExpression(self, ctx: SqlParser.ValueExpressionContext):
        pass

    # Enter a parse tree produced by SqlParser#literal.
    def enterLiteral(self, ctx: SqlParser.LiteralContext):
        pass

    # Exit a parse tree produced by SqlParser#literal.
    def exitLiteral(self, ctx: SqlParser.LiteralContext):
        pass

    # Enter a parse tree produced by SqlParser#generalLiteral.
    def enterGeneralLiteral(self, ctx: SqlParser.GeneralLiteralContext):
        pass

    # Exit a parse tree produced by SqlParser#generalLiteral.
    def exitGeneralLiteral(self, ctx: SqlParser.GeneralLiteralContext):
        pass

    # Enter a parse tree produced by SqlParser#characterStringLiteral.
    def enterCharacterStringLiteral(self, ctx: SqlParser.CharacterStringLiteralContext):
        pass

    # Exit a parse tree produced by SqlParser#characterStringLiteral.
    def exitCharacterStringLiteral(self, ctx: SqlParser.CharacterStringLiteralContext):
        pass

    # Enter a parse tree produced by SqlParser#signedNumericLiteral.
    def enterSignedNumericLiteral(self, ctx: SqlParser.SignedNumericLiteralContext):
        pass

    # Exit a parse tree produced by SqlParser#signedNumericLiteral.
    def exitSignedNumericLiteral(self, ctx: SqlParser.SignedNumericLiteralContext):
        pass

    # Enter a parse tree produced by SqlParser#sign.
    def enterSign(self, ctx: SqlParser.SignContext):
        pass

    # Exit a parse tree produced by SqlParser#sign.
    def exitSign(self, ctx: SqlParser.SignContext):
        pass

    # Enter a parse tree produced by SqlParser#unsignedNumericLiteral.
    def enterUnsignedNumericLiteral(self, ctx: SqlParser.UnsignedNumericLiteralContext):
        pass

    # Exit a parse tree produced by SqlParser#unsignedNumericLiteral.
    def exitUnsignedNumericLiteral(self, ctx: SqlParser.UnsignedNumericLiteralContext):
        pass

    # Enter a parse tree produced by SqlParser#exactNumericLiteral.
    def enterExactNumericLiteral(self, ctx: SqlParser.ExactNumericLiteralContext):
        pass

    # Exit a parse tree produced by SqlParser#exactNumericLiteral.
    def exitExactNumericLiteral(self, ctx: SqlParser.ExactNumericLiteralContext):
        pass

    # Enter a parse tree produced by SqlParser#groupByClause.
    def enterGroupByClause(self, ctx: SqlParser.GroupByClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#groupByClause.
    def exitGroupByClause(self, ctx: SqlParser.GroupByClauseContext):
        pass

    # Enter a parse tree produced by SqlParser#columnList.
    def enterColumnList(self, ctx: SqlParser.ColumnListContext):
        pass

    # Exit a parse tree produced by SqlParser#columnList.
    def exitColumnList(self, ctx: SqlParser.ColumnListContext):
        pass

    # Enter a parse tree produced by SqlParser#orderByClause.
    def enterOrderByClause(self, ctx: SqlParser.OrderByClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#orderByClause.
    def exitOrderByClause(self, ctx: SqlParser.OrderByClauseContext):
        pass

    # Enter a parse tree produced by SqlParser#orderItem.
    def enterOrderItem(self, ctx: SqlParser.OrderItemContext):
        pass

    # Exit a parse tree produced by SqlParser#orderItem.
    def exitOrderItem(self, ctx: SqlParser.OrderItemContext):
        pass

    # Enter a parse tree produced by SqlParser#orderOption.
    def enterOrderOption(self, ctx: SqlParser.OrderOptionContext):
        pass

    # Exit a parse tree produced by SqlParser#orderOption.
    def exitOrderOption(self, ctx: SqlParser.OrderOptionContext):
        pass

    # Enter a parse tree produced by SqlParser#timingByClause.
    def enterTimingByClause(self, ctx: SqlParser.TimingByClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#timingByClause.
    def exitTimingByClause(self, ctx: SqlParser.TimingByClauseContext):
        pass

    # Enter a parse tree produced by SqlParser#timeSpanUnit.
    def enterTimeSpanUnit(self, ctx: SqlParser.TimeSpanUnitContext):
        pass

    # Exit a parse tree produced by SqlParser#timeSpanUnit.
    def exitTimeSpanUnit(self, ctx: SqlParser.TimeSpanUnitContext):
        pass

    # Enter a parse tree produced by SqlParser#limitClause.
    def enterLimitClause(self, ctx: SqlParser.LimitClauseContext):
        pass

    # Exit a parse tree produced by SqlParser#limitClause.
    def exitLimitClause(self, ctx: SqlParser.LimitClauseContext):
        pass


del SqlParser
