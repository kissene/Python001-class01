import scrapy
from week02.proxy_crawler.proxy_crawler.items import ProxyCrawlerItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        item = ProxyCrawlerItem()
        print(response.text)
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for movie in movies[0:10]:
            name = movie.xpath('./div[1]/span[1]/text()')
            m_type = movie.xpath('./div[2]/text()')
            time = movie.xpath('./div[4]/text()')

            item['name'] = name.extract_first()
            item['type'] = m_type.extract()[1].split('\n')[1].strip()
            item['time'] = time[1].extract().split('\n')[1].strip()
            yield item


if __name__ == '__main__':
    from scrapy import cmdline
    args = "scrapy crawl maoyan".split()
    cmdline.execute(args)