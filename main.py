
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
