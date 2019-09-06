#!/usr/bin/env python
import psycopg2
import time


def db_connect(schema="news"):
    """
    Create and return a database connection and cursor.
    The functions creates and returns a database connection and cursor to the
    database defined by DBNAME.
    Returns:
        db, c - a tuple. The first element is a connection to the database.
                The second element is a cursor for the database.
    """
    db = psycopg2.connect(dbname=schema, user="", password="")
    cur = db.cursor()
    return (db, cur)


def execute_query(query):
    """
    execute_query returns the results of an SQL query.
    execute_query takes an SQL query as a parameter,
    executes the query and returns the results as a list of tuples.
    args:
    query - an SQL query statement to be executed.

    returns:
    A list of tuples containing the results of the query.
    """
    cur = db_connect()[1]
    cur.execute(query)
    return cur.fetchall()


def print_top_articles():
    """Print out the top 3 articles of all time."""
    query = """
        SELECT title, COUNT (title) FROM ARTICLES
        LEFT JOIN LOG ON log.path = '/article/' || articles.slug
        GROUP BY title
        ORDER BY COUNT (title) DESC
        LIMIT 3
    """
    results = execute_query(query)
    print("1. What are the most popular three articles of all time?:")
    for i in results:
        print("\"{name}\" - {views} views".format(name=i[0], views=i[1]))


def print_top_authors():
    """Print a list of authors ranked by article views."""
    query = """
        SELECT  COUNT (title), author, authors.name FROM ARTICLES
        LEFT JOIN LOG ON log.path = '/article/' || articles.slug
        LEFT JOIN authors ON authors.id = ARTICLES.author
        GROUP BY  author,authors.name
        ORDER BY COUNT (title) DESC;
    """
    results = execute_query(query)
    print
    print("2. Who are the most popular authors of all times?:")
    for i in results:
        print("{name} - {views} views".format(name=i[2], views=i[0]))


def print_errors_over_one():
    """Print out the error report.
    This function prints out the days and that day's error percentage where
    more than 1% of logged access requests were errors.
    """
    query = """
        SELECT TO_CHAR(date_trunc, 'Mon DD, YYYY'),
        round(errorpercentage,1)  FROM (
            SELECT
             date_trunc('day',time),
             STATUS,
             count(status),
             LOG2.total,
            (count(status)::numeric*100)/LOG2.total::numeric as errorpercentage
            FROM LOG
            LEFT JOIN (
                SELECT date_trunc('day',time) as day_, count(status) as total
                FROM LOG GROUP BY
                date_trunc('day',time)
            ) as LOG2 on date_trunc('day',time) = LOG2.day_
            GROUP BY date_trunc('day',time), STATUS, LOG2.TOTAL
            HAVING (LOG2.TOTAL::numeric/100) < count(status)::numeric
            AND status = '404 NOT FOUND'
        ) as foo;
    """
    results = execute_query(query)
    print
    print("3.  On which days did more than 1% of requests lead to errors:")
    for i in results:
        print("{} - {} % errors".format(i[0], i[1]))


if __name__ == '__main__':
    print_top_articles()
    print_top_authors()
    print_errors_over_one()
