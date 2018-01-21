import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        'https://readhub.me/',
    ]

    def parse(self, response):
        for news in response.css('div.topicItem___3YVLI'):
            # summary = news.css('h2.topicTitle___1M353').css('span.content___2vSS6::text').extract_first()
            title = news.xpath('h2/span/text()').extract_first()
            text = news.xpath('div/div/text()').extract_first()
            yield {
                'title': title,
                'text': text
            }