from sql2spl.queryTranslator import queryTranslator

import pytest


def test_select():
    in_query = "select * from db_name"
    assert queryTranslator(in_query) == "index=db_name | fields *"


def test_dedup_rename():
    in_query = "select distinct col_a as col_b from db"
    assert queryTranslator(in_query) == "index=db | fields col_a | rename col_a as col_b | dedup col_a"


def test_columns():
    in_query = "select col_a, col_b, col_c from db_name"
    assert queryTranslator(in_query) == "index=db_name | fields col_a, col_b, col_c"


def test_spath():
    in_query = "select col_a.sub, col_b.sub from db_name"
    assert queryTranslator(in_query) == "index=db_name | fields col_a.sub, col_b.sub"


def test_sort_limit():
    in_query = "select * from db_name order by col limit 5"
    assert queryTranslator(in_query) == "index=db_name | fields * | sort col | head 5"


def test_sort_desc():
    in_query = "select * from db_name order by col_a DESC, col_b, col_c DESC limit 5"
    assert queryTranslator(in_query) == "index=db_name | fields * | sort -col_a, col_b, -col_c | head 5"


def test_func():
    in_query = "select avg(col_a) from db_name"
    assert queryTranslator(in_query) == "index=db_name | stats avg(col_a)"


def test_multi_func():
    in_query = "select avg(col_a), dc(col_b) from db_name group by col_c"
    assert queryTranslator(in_query) == "index=db_name | stats avg(col_a), dc(col_b) by col_c"


def test_eval():
    in_query = 'select eval("col_a*100") as col_a_percent from db_name'
    assert queryTranslator(in_query) == "index=db_name | eval col_a_percent=col_a*100"


def test_func_eval():
    in_query = 'select avg(eval("col_a*100")) as avg_col_a_percent from db_name group by col_b'
    assert (
        queryTranslator(in_query)
        == 'index=db_name | eval "col_a*100"=col_a*100 | stats avg("col_a*100") as avg_col_a_percent by col_b'
    )


def test_select_nest():
    in_query = 'select avg(col_new) from (select eval("col_a*100") as col_new from db_name) group by col_c'
    assert queryTranslator(in_query) == "index=db_name | eval col_new=col_a*100 | stats avg(col_new) by col_c"


def test_contains():
    in_query = 'select * from db_name where contains("get")'
    assert queryTranslator(in_query) == 'index=db_name | search "get" | fields *'


def test_join_different_field_name():
    in_query = "select * from db_name1 inner join db_name2 on db_name1.col_a=db_name2.col_b"
    assert (
        queryTranslator(in_query)
        == "index=db_name1 | join type=inner col_a [SEARCH index=db_name2 | rename col_b as col_a] | fields *"
    )


def test_join_same_field_name():
    in_query = "select * from db_name1 inner join db_name2 on db_name1.col_a=db_name2.col_a"
    assert queryTranslator(in_query) == "index=db_name1 | join type=inner col_a [SEARCH index=db_name2] | fields *"


def test_timing_by():
    in_query = "select avg(col_a) from db_name timing by 1h"
    assert queryTranslator(in_query) == "index=db_name | bin _time span=1h | stats avg(col_a)by _time"


def test_timing_by_with_group():
    in_query = "select avg(col_a) from db_name group by col_b timing by 5m"
    assert queryTranslator(in_query) == "index=db_name | bin _time span=5m | stats avg(col_a) by _time, col_b"


def test_where_clause():
    in_query = 'select * from db_name where col_a="*abc" AND contains("test") OR col_b>3'
    assert queryTranslator(in_query) == 'index=db_name | search col_a="*abc" AND "test" OR col_b>3 | fields *'


def test_distinct():
    in_query = "select distinct col_a, col_b, distinct col_c from db"
    assert queryTranslator(in_query) == "index=db | fields col_a, col_b, col_c | dedup col_a, col_c"


def test_where_complex_clause():
    in_query = 'select * from db where contains("any_string_+_12_\\"\\"_()_._*_any_signal")'
    assert queryTranslator(in_query) == 'index=db | search "any_string_+_12_\\"\\"_()_._*_any_signal" | fields *'


def test_where_complex_clause2():
    in_query = 'select * from db where col_a="*abd" AND col_b=123'
    assert queryTranslator(in_query) == 'index=db | search col_a="*abd" AND col_b=123 | fields *'


def test_head_stats():
    in_query = "select avg(col_c) as col_b from (select * from db limit 100) group by col_a"
    assert queryTranslator(in_query) == "index=db | fields * | head 100 | stats avg(col_c) as col_b by col_a"


def test_():
    in_query = "select avg(col_c) as col_b from (select * from db limit 100) group by col_a limit 5"
    assert queryTranslator(in_query) == "index=db | fields * | head 100 | stats avg(col_c) as col_b by col_a | head 5"


def test_time_by_and_group_by1s():
    in_query = "select avg(col_a) from db timing by 5m group by col_b"
    assert queryTranslator(in_query) == "index=db | bin _time span=5m | stats avg(col_a) by _time, col_b"


def test_time_by_and_group_by2():
    in_query = "select avg(col_a) from db group by col_b timing by 5m"
    assert queryTranslator(in_query) == "index=db | bin _time span=5m | stats avg(col_a) by _time, col_b"
