import scrapy

class AosFatosSpider(scrapy.Spider):
    name = 'aos_fatos'
    allowed_domains = ['aosfatos.org']
    start_urls = ['http://www.aosfatos.org']

    # check every category from menu
    def parse(self, response):
      links = response.xpath('//nav//ul//li/a[re:test(@href, "checamos")]/@href').getall()
      for link in links:
        yield scrapy.Request(
          response.urljoin(link),
          callback=self.parse_category
        )

    # check every card (news) from every category
    def parse_category(self, response):
      news = response.css('.card::attr(href)').getall()
      for new_url in news:
          yield scrapy.Request(
            response.urljoin(new_url),
            callback=self.parse_new
          )

      # after checking every card from a page, goes to the next page
      pages_url = response.css('.pagination a::atr(href)').getall()
      for page in pages_url:
        yield scrapy.Request(
          response.urljoin(page),
          callback=self.parse_category
        )

    # return dict with news scraped information
    def parse_new(self, response):
      title = response.css('article h1::text').get()
      date = ' '.join(response.css('p.publish_date::text').get().split())

      quotes = response.css('article blockquote p')
      for quote in quotes:
        quote_text = quote.css('::text').get()
        status = quote.xpath('./parent::blockquote/preceding-sibling::figure//figcaption//text').get()

        # if not status:
        #   continue

        yield {
          'title': title,
          'date': date,
          'quote_text': quote_text,
          'status': status,
          'url': response.url
        }
