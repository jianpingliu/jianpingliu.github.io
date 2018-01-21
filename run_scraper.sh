#!/usr/bin/env bash

rm -rf data/news.json
scrapy runspider scraper/readhub.py -o data/news.json