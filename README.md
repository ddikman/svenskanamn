# svenskanamn

Parser for scraping Swedish names.

## usage

```shell
scrapy runspider scrape_names.py -a gender=pojknamn -o pojknamn.csv -t csv
scrapy runspider scrape_names.py -a gender=flicknamn -o flicknamn.csv -t csv
```

## dependencies

Built using [scrapy](https://scrapy.org/):

```shell
pip install scrapy
```

## disclaimer

Please not that accordding to the rules of directory protection ([Katalogskydd](https://sv.wikipedia.org/wiki/Katalogskydd)) the automatic collection and reuse of any directory information may make scraping the included or any other similar sites illegal. Please do not utilize this library to collect and use information without the permission of the owner of the data.

This code snippet is only meant to provide an example of scraping.