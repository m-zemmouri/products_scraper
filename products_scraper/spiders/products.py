import scrapy
from products_scraper.items import ProductItem
from scrapy_playwright.page import PageMethod

class ProductSpider(scrapy.Spider):
    name = 'products'

    def start_requests(self):
        url = "https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/"
        yield scrapy.Request(url, meta=dict(
                playwright = True,
                playwright_include_page = True,
                playwright_page_methods =[PageMethod('wait_for_selector', 'shared-grid.ng-star-inserted')],
                errback=self.errback,
            ))

    async def parse(self, response):
        page = response.meta["playwright_page"]
        await page.close()

        # file = open("woolworths.html","w")
        # file.write(response.text)
        # file.close()

        for product in response.css('section.product-tile-v2'):
            product_item = ProductItem()
            product_item['name'] = product.css('a.product-title-link::text').get()
            product_item['price'] = product.css('div.primary::text').get().replace('$', '')
            yield product_item

        # next_page = response.css('a.paging-next::attr(href)').get()

        # if next_page is not None:
        #     url = 'https://www.woolworths.com.au/' + next_page
        #     yield scrapy.Request(url, meta=dict(
        #         playwright = True,
        #         playwright_include_page = True,
        #         playwright_page_methods =[PageMethod('wait_for_selector', 'shared-grid.ng-star-inserted')],
        #         errback=self.errback,
        #     ))

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
