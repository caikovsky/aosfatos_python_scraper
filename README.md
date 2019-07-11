# Python Webscraper

This is a python project which scrapes every news reported into [Aos Fatos website](https://aosfatos.org/) using [Scrapy](https://scrapy.org/) and outputs the data into a CSV file.


## Run project

1. Start Pipenv environment with `$ pipenv shell`

2. Run aos_fatos scrapy project:
`$ scrapy crawl fatos -s HTTPCACHE_ENABLED=1`, and to generate a file with all the scraped data (as a CSV, for example), use `-o {filename}.csv` flag.