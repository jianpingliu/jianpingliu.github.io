import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        'https://readhub.me/',
    ]

    def parse(self, response):
        for news in response.css('div.topicItem___3YVLI'):
            title = news.xpath('h2/span/text()').extract_first()
            text = news.xpath('div/div/text()').extract_first()
            yield {
                'title': title,
                'text': text
            }
