# coding=utf-8

import MySQLdb as db
from contextlib import contextmanager
from tcp_logger.file_logger import api_logger as logger

@contextmanager
def open_cursor(db_host, db_port, db_name, user, passwd):

    conn = db.connect(host=db_host,
                      port=db_port,
                      db=db_name,
                      user=user,
                      passwd=passwd,
                      autocommit=True)
    c = conn.cursor()
    try:
        yield c
    finally:
        c.close()


def getAll(cursor, sql, **kwargs):
    cursor.execute(sql, kwargs)
    rows = __dictfetchall(cursor)
    if not rows:
        return None
    return rows


def get(cursor, sql, **kwargs):
    cursor.execute(sql, kwargs)
    rows = __dictfetchall(cursor)
    if not rows:
        return None
    return rows[0]


def list(cursor, sql, **kwargs):
    # print sql
    cursor.execute(sql, kwargs)
    return __dictfetchall(cursor)


def insert(cursor, table, **kwargs):
    columns = ', '.join(kwargs.keys())
    variables = ', '.join(['%({})s'.format(k) for k in kwargs.keys()])
    sql = ''.join(['INSERT INTO ', table, '(', columns, ') VALUES (', variables, ')'])
    try:
        cursor.execute(sql, kwargs)
        return cursor.lastrowid
    except Exception, e:
        logger.exception('insert failed, sql=>%s' % cursor._last_executed)
        raise



def execute(cursor, sql, **kwargs):
    try:
        cursor.execute(sql, kwargs)
        return cursor.rowcount
    except Exception, e:
        logger.exception('execute failed, sql=>%s' % cursor._last_executed)
        raise


def __dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
