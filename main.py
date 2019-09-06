import psycopg2
import time


if __name__ == '__main__':

    db = psycopg2.connect(dbname="news", user="", password="")
    cur = db.cursor()
    #TASK 1
    cur.execute("""
        SELECT title, COUNT (title) FROM ARTICLES
        LEFT JOIN LOG ON LOG.PATH like '%'  || ARTICLES.SLUG
        GROUP BY title
        ORDER BY COUNT (title) DESC
        LIMIT 3
    """)
    res = cur.fetchall()
    print("1. What are the most popular three articles of all time?:")
    for i in res:
        print("{name} - {views} views".format(name = i[0], views = i[1]))
    #TASK 2
    cur.execute("""
        SELECT  COUNT (title), author, authors.name FROM ARTICLES
        LEFT JOIN LOG ON LOG.PATH like '%'  || ARTICLES.SLUG
        LEFT JOIN authors ON authors.id = ARTICLES.author
        GROUP BY  author,authors.name
        ORDER BY COUNT (title) DESC;
    """)
    res = cur.fetchall()
    print
    print("2. Who are the most popular authors of all times?:")
    for i in res:
        print("{name} - {views} views".format(name = i[0], views = i[2]))
    #TASK 3
    cur.execute("""
        SELECT TO_CHAR(date_trunc, 'Mon DD, YYYY'), round(errorpercentage,1)  from (
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
    """)
    print
    print("3.  On which days did more than 1% of requests lead to errors:")
    res = cur.fetchall()
    for i in res:
        print("{date} - {errorpercentage} views".format(date = i[0], errorpercentage = i[1]))
