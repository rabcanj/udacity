# Logs Analysis
### How to run me
The script uses python 2.7 and postgre database. You can use VM machine configuration available here: [vagrant](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip), where everything is installed.

- download the [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
- unzip and import data into the postgre database
```sh
$ psql -f newsdata.sql -d news
```
Execute script:
```sh
$ python3 main.py
```
