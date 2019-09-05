
import psycopg2
import time

if __name__ == '__main__':

    db = psycopg2.connect(dbname="news", user="", password="")
    cur = db.cursor()

    cur.execute("""
        SELECT title, COUNT (title) FROM ARTICLES
        LEFT JOIN LOG ON LOG.PATH like '%'  || ARTICLES.SLUG
        GROUP BY title
        ORDER BY COUNT (title) DESC
        LIMIT 3
    """)
    res = cur.fetchall()
    print()
    print("1. What are the most popular three articles of all time?:")
    for i in res:
        print("{name} - {views} views".format(name = i[0], views = i[1]))
