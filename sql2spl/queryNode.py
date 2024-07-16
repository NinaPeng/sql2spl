class basicItem:
    @property
    def distinct(self):
        return self._distinct

    @distinct.setter
    def distinct(self, value):
        self._distinct = True if value else False

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        self._alias = value

    def getFieldsQuery(self):
        return None

    def getDedupQuery(self):
        return None

    def getRenameQuery(self):
        return None

    def getEvalQuery(self):
        return None

    def getStatsQuery(self):
        return None


class fieldItem(basicItem):
    def __init__(self, name, distinct=False, alias=None):
        self._name = name
        self._distinct = distinct
        self._alias = alias

    def getFieldsQuery(self):
        return self._name

    def getDedupQuery(self):
        if self._distinct:
            return self._name
        else:
            return None

    def getRenameQuery(self):
        if self._alias:
            return "%s as %s" % (self._name, self._alias)
        else:
            return None

    def __str__(self):
        return self._name


class evalItem(basicItem):
    def __init__(self, expr, distinct=False, alias=None):
        self._expr = expr
        self._distinct = distinct
        self._alias = alias

    @property
    def expr(self):
        return self._expr

    # eval alias=expr
    # eval "expr"=expr
    def getEvalQuery(self):
        if self._alias:
            return "%s=%s" % (self._alias, self._expr)
        else:
            return '"%s"=%s' % (self._expr, self._expr)

    # fields alias
    # fields "expr"
    # def getFieldsQuery(self):
    #     return "\"%s\""%self._expr if not self._alias else None

    # dedup alias
    # dedup "expr"
    def getDedupQuery(self):
        if self._distinct:
            return self._alias if self._alias else '"%s"' % self._expr
        else:
            return None

    def __str__(self):
        return self._expr


class statsItem(basicItem):
    def __init__(self, func, para: basicItem, distinct=False, alias=None):
        self._func = func
        self._para = para
        self._distinct = distinct
        self._alias = alias

    # eval "para.expr" = para.expr
    def getEvalQuery(self):
        if type(self._para) == evalItem:
            return '"%s"=%s' % (self._para, self._para)
        else:
            return None

    # para:fieldItem -> stats func(para) (as alias)
    # para:evalItem -> stats func("para") (as alias)
    def getStatsQuery(self):
        if type(self._para) == fieldItem:
            res = "%s(%s)" % (self._func, self._para)
        if type(self._para) == evalItem:
            res = '%s("%s")' % (self._func, self._para)
        if self._alias:
            res = "%s as %s" % (res, self._alias)
        return res

    def __str__(self):
        return "%s(%s)" % (self._func, self._para)


class sortField:
    def __init__(self, name, desc=""):
        self._name = name
        self._desc = ""
        if desc.upper() == "DESC":
            self._desc = "-"

    def __str__(self):
        return "%s%s" % (self._desc, self._name)


class joinedField:
    def __init__(self, table1, table2, field1: fieldItem, field2: fieldItem):
        self._table1 = table1
        self._table2 = table2
        self._field1 = field1
        self._field2 = field2

    def getJoinedField(self, leftTable, rightTable):
        if self._table1 == leftTable and self._table2 == rightTable:
            if str(self._field1) != str(self._field2):
                return str(self._field1), "%s as %s" % (self._field2, self._field1)
            else:
                return str(self._field1), None
        if self._table2 == leftTable and self._table1 == rightTable:
            if str(self._field1) != str(self._field2):
                return str(self._field2), "%s as %s" % (self._field1, self._field2)
            else:
                return str(self._field2), None
        return None, None
