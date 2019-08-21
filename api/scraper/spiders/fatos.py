# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class FatosSpider(CrawlSpider):
    name = 'fatos'
    allowed_domains = ['aosfatos.org']
    start_urls = ['http://aosfatos.org/']

    rules = (
      Rule(
        LinkExtractor(
          restrict_xpaths=('//li[contains(text(), "Checamos")]//ul//li')
        )
      ),
      Rule(
        LinkExtractor(
          restrict_css=('.pagination a')
        )
      ),
      Rule(
        LinkExtractor(
          restrict_css=('a.card')
        ),
        callback='parse_new'
      )
    )

    # return dict with news scraped information
    def parse_new(self, response):
      title = response.css('article h1::text').get()
      date = ' '.join(response.css('p.publish_date::text').get().split())

      quotes = response.css('article blockquote p')
      for quote in quotes:
        quote_text = quote.css('::text').get()
        status = quote.xpath('./parent::blockquote/preceding-sibling::figure//figcaption//text()').get()

        yield {
          'title': title,
          'date': date,
          'quote_text': quote_text,
          'status': status,
          'url': response.url
        }
