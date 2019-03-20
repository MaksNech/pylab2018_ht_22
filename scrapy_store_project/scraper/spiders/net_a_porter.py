import scrapy
import re
import json
from ..items import ScraperItem
from scrapy_redis.spiders import RedisSpider


class NetAPorterBagsSpider(RedisSpider):
    name = 'net_a_porter_bags'

    allowed_domains = [
        'net-a-porter.com',
    ]

    custom_settings = {
        'DOWNLOAD_DELAY': 2,
    }

    def get_pages_count(self, response):
        count_of_pages = response.xpath('//div[@class="pagination-links"]/@data-lastpage').extract_first()
        return int(count_of_pages)


    def parse(self, response):

        pagination_next_page_href = response.xpath("//a[@class='next-page']/@href").extract_first()

        if pagination_next_page_href:
            products_hrefs_list = response.xpath("//div[@class='product-image']/a/@href").extract()

            if products_hrefs_list:

                for href in products_hrefs_list:
                    variety_div = response.xpath("//div[contains(@class,'product-colour-swatches')]").extract_first()

                    if variety_div:
                        variety_hrefs_list = response.xpath(
                            "//div[contains(@class,'product-colour-swatches')]/nap-product-swatch-collector/nap-product\
                            -swatch/div[contains(@class,'product-swatch')]/a/@href").extract()
                        if variety_hrefs_list:
                            for href in variety_hrefs_list:
                                yield scrapy.Request(url=response.urljoin(href), callback=self.parse_bag_page)
                    else:
                        yield scrapy.Request(url=response.urljoin(href), callback=self.parse_bag_page)

            pagination_next_page_href = response.urljoin(pagination_next_page_href)
            yield scrapy.Request(url=pagination_next_page_href, callback=self.parse)

    def get_brand(self, response):
        brand = response.xpath("//a[@class='designer-name']/span/text()").extract_first()
        brand = ''.join(brand)
        return brand

    def get_title(self, response):
        title = response.xpath("//h2[@class='product-name']/text()").extract_first()
        title = ''.join(title)
        return title

    def get_description(self, response):
        desc_p = response.xpath(
            "//div[@class='product-details']/widget-show-hide[@id='accordion-2']/div[@class='show-hide-content']/div\
            [@class='wrapper']/p/text()[1]").extract_first()
        desc_ul = response.xpath("//div[@class='product-details']/widget-show-hide[@id='accordion-2']/div\
            [@class='show-hide-content']/div[@class='wrapper']/ul/li/text()").extract()

        desc_ul = '\n'.join(desc_ul)

        desc_p = re.sub(r'\s', ' ', desc_p)

        return desc_p + '\n' + desc_ul

    def get_size(self, response):
        size_ul = response.xpath(
            "//div[@class='product-details']/widget-show-hide[@id='accordion-1']/div[@class='show-hide-content']/div\
            [@class='wrapper']/ul/li/text()").extract()

        size_ul = '\n'.join(size_ul)

        return size_ul

    def get_price(self, response):
        price = response.xpath(
            "//div[@id='main-product']/div[@class='container-title']/nap-price/@price").extract_first()
        price = json.loads(price)
        currency = price['currency']
        amount = int(price['amount']) / int(price['divisor'])

        return '{} {}'.format(amount, currency)

    def get_images(self, response):
        images_sources_list = response.xpath(
            "//ul[contains(@class,'swiper-wrapper')]/li/img[contains(@class,'product-image') and contains\
            (@class,'first-image')]/@src|//div[@class='product-image']/img/@src").extract()

        images_sources_list = list(dict.fromkeys(images_sources_list))
        main_image_src = ''
        for src in images_sources_list:
            if 'in_xs' in src:
                main_image_src = src.replace('in_xs', 'in_pp')

        return response.urljoin(main_image_src)



    def parse_bag_page(self, response):
        item = ScraperItem()
        item['brand'] = self.get_brand(response)
        item['title'] = self.get_title(response)
        item['price'] = self.get_price(response)
        item['description'] = self.get_description(response)
        item['size'] = self.get_size(response)
        item['image'] = self.get_images(response)
        return item
