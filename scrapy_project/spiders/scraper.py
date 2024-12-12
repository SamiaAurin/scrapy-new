import scrapy
from scrapy_project.items import ScrapyProjectItem

class ScraperSpider(scrapy.Spider):
    name = "scraper"
    # allowed_domains = ["www.scrapingcourse.com"]
    start_urls = ["https://www.scrapingcourse.com/ecommerce/"] # Replace with your target URL

    def parse(self, response):
        # Get all HTML product elements
        products = response.css(".product")
        
        # Iterate over the list of products
        for product in products:
            price_text_elements = product.css(".price *::text").getall()
            price = "".join(price_text_elements)
            
            # Yield data
            yield ScrapyProjectItem(
                Url=product.css("a").attrib["href"],
                Image=product.css("img").attrib["src"],
                Name=product.css("h2::text").get(),
                Price=price
            )
