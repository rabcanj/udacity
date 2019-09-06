# Logs Analysis project

The script uses python 2.7 and postgre database. You can use VM machine configuration available here: [vagrant](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip), where everything is installed.

- download the [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
- import data file (newsdata.sql) into the postgre database
```sh
$ psql -f newsdata.sql -d news
```
Execute script:
```sh
$ python main.py
```
# Example

```sh
$ python main.py
1. What are the most popular three articles of all time?:
Candidate is jerk, alleges rival - 338647 views
Bears love berries, alleges bear - 253801 views
Bad things gone, say good people - 170098 views

2. Who are the most popular authors of all times?:
507594 - Ursula La Multa views
423457 - Rudolf von Treppenwitz views
170098 - Anonymous Contributor views
84557 - Markoff Chaney views

3.  On which days did more than 1% of requests lead to errors:
Jul 17, 2016 - 2.3 %
```
