# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
import re

def cleanhtml(html):
  cleanr = re.compile('<.*?>')
  html.encode('ascii','ignore')
  cleantext = re.sub(cleanr, '', html)
  cleantext=cleantext.strip()
  cleantext=re.sub('\s+',' ',cleantext)
  return cleantext

class AdidasSpider(CrawlSpider):
    name = 'adidas'
    def __init__(self, product='apple', domain=None, *args, **kwargs):
        super(AdidasSpider, self).__init__(*args, **kwargs)
        self.product_name=product.lower()
        self.product_name=re.sub("[^ a-zA-Z0-9]+", "", self.product_name)
        self.search_url='https://www.adidas.com/us/samba-og-shoes/HP7898.html='+self.product_name

        self.allowed_domains = ['www.adidas.com/us']
        self.start_urls = [self.search_url]

    rules = (
          Rule(LinkExtractor(allow=(), tags=('a'),attrs=('href'),restrict_css=('.pagnNext',)),
               callback="parse_items",
               follow=True),)

    def parse_start_url(self,response):
        request=Request("https://www.adidas.com/us/samba-og-shoes/HP7898.html=", callback=self.parse_items)
        return request

    def parse_items(self, response):
       print ('Processing...',response.url)
       title=[]
       image=[]
       price=[]
       url=[]
       for item in response.css('ul li div.s-item-container'):

         item_title=item.css('h2.s-access-title::text').extract_first()
         item_image=item.css('img.s-access-image::attr(src)').extract_first()
         item_price=item.css('span.a-color-price').extract_first()
         item_url=item.css('a.s-access-detail-page::attr(href)').extract_first()
         if(item_title and item_image and item_price and item_url):
          title.append(cleanhtml(item_title))
          image.append(cleanhtml(item_image))
          price.append('Rs. '+ cleanhtml(item_price))
          url.append(cleanhtml(item_url))
       print ('Result Counts: ',len(title))
       
       for item in zip(title,price,image,url):
           scraped_info = {
               'product_name' : item[0],
               'price' : item[1],
               'image_url' : item[2],
               'product_url': item[3],
               'source': 'https://www.adidas.com/us' 
               }
           yield scraped_info