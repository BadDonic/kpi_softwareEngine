import scrapy
from scrapy import Selector


class PetsSpider(scrapy.Spider):
    name = "pets"
    url = 'https://www.pettravel.com/forum/forumdisplay.php/2-Pet-Travel-International/page'

    def start_requests(self):
        for i in range(31):
            yield scrapy.Request(self.url + str(i + 1))

    def parse(self, response):
        topics = Selector(response).xpath("//a[contains(@id, 'thread_title_')]")
        for topic in topics:
            url = response.urljoin(topic.xpath(".//@href").extract_first())
            request = scrapy.Request(url, self.parse_thread_pages)
            request.meta['topic'] = topic.xpath('./text()').extract_first()
            yield request

    def parse_thread_pages(self, response):
        for post in response.xpath("//li[contains(@id, 'post_')]"):
            topic = response.meta['topic']
            message = post.css("blockquote::text").re(r"\r*\n*\s*(.+)")
            author = post.css("a strong::text").extract_first()
            date = post.css('span.date::text').extract_first() + post.css('span.time::text').extract_first()
            yield {
                'topic': topic,
                'author': author,
                'message': "".join(message),
                'date': date
            }
        next_page = response.css('span.prev_next a[rel="next"]::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse_thread_pages)
