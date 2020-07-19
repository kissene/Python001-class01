# ****************************
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 11:35
# Author = kissene_xie
# @File    : homework
# ****************************
__author__ = 'kissene_xie'


import pandas as pd
import numpy as np


class TransformSQL(object):
    def __init__(self):
        self.data = pd.read_csv('data.csv', encoding='gbk')
        self.table1 = pd.read_csv('table1.csv')
        self.table2 = pd.read_csv('table2.csv')

    # SELECT * FROM data
    def select_all_data(self):
        print(self.data)

    # SELECT * FROM data LIMIT 10
    def select_limit_data(self, num):
        print(self.data.head(num))

    #  SELECT id FROM data
    def select_data_by_column_name(self, name):
        print(self.data[[name]])

    # SELECT COUNT(id) FROM data
    def count_data_by_column_name(self, name):
        count = self.data[[name]].count()
        print(count)

    # SELECT * FROM data WHERE id<1000 AND age>30;
    def select_data_by_condition(self):
        filtered_data = self.data[(self.data['id'] > 1000) & (self.data['age'] < 30)]
        print(filtered_data)

    # SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id
    def select_id_and_count_order_id(self):
        result = self.table1.groupby('id').aggregate({'order_id': 'count', })
        print(result)

    # SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id
    def inner_join_by_id(self):
        merged = self.table1.merge(self.table2, left_on='id', right_on='id')
        print(merged)

    # SELECT * FROM table1 UNION SELECT * FROM table2
    def union_select(self):
        c = pd.concat([self.table1, self.table2]).drop_duplicates()
        print(c)

    # DELETE FROM table1 WHERE id=10
    def delete_by_id(self):
        new_data = self.table1.loc[self.table1['id'] != 10]
        print(new_data)

    # ALTER TABLE table1 DROP COLUMN column_name
    def drop_column(self):
        new_data = self.table1.drop('order_id', axis=1)
        print(new_data)


def main():
    tf_sql = TransformSQL()
    print(20*'=')

    print('/SELECT * FROM data start/')
    tf_sql.select_all_data()
    print("/SELECT * FROM data end/")

    print("/SELECT * FROM data LIMIT 10 start/")
    tf_sql.select_limit_data(10)
    print("/SELECT * FROM data LIMIT 10 end/")

    print("/SELECT id FROM data start/")
    tf_sql.select_data_by_column_name('id')
    print("/SELECT id FROM data end/")

    print("/SELECT COUNT(id) FROM data start/")
    tf_sql.count_data_by_column_name('id')
    print("/SELECT COUNT(id) FROM data end/")

    print("/SELECT * FROM data WHERE id<1000 AND age>30 start/")
    tf_sql.select_data_by_condition()
    print("/SELECT * FROM data WHERE id<1000 AND age>30 end/")

    print("/SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id start/")
    tf_sql.select_id_and_count_order_id()
    print("/SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id end/")

    print("/SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id start/")
    tf_sql.inner_join_by_id()
    print("/SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id end/")

    print("/SELECT * FROM table1 UNION SELECT * FROM table2 start/")
    tf_sql.union_select()
    print("/SELECT * FROM table1 UNION SELECT * FROM table2 end/")

    print("/DELETE FROM table1 WHERE id=10 start/")
    tf_sql.delete_by_id()
    print("/DELETE FROM table1 WHERE id=10 end/")

    print("/ALTER TABLE table1 DROP COLUMN column_name start/")
    tf_sql.drop_column()
    print("/ALTER TABLE table1 DROP COLUMN column_name end/")


if __name__ == '__main__':
    main()
