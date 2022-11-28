import scrapy
import csv
import os
import tarfile
from os import path
import time
from scrapy import signals


basepath = path.dirname(__file__)

os.makedirs(path.abspath(path.join(basepath,"..","..",f'archive')), exist_ok=True)                      #archive directory


class task1Spider(scrapy.Spider):
    name = "task1"


    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(task1Spider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signals.spider_closed)
        return spider

    def start_requests(self):
        with open('urls.csv', newline='') as csvfile:
            urls = csv.reader(csvfile, delimiter=' ', quotechar='|')                                    #open input file
            for url in urls:
                yield scrapy.Request(url=str(*url),callback=self.parse) 
            
                                                                                                        # save all htmls to archive
            

# callbackfunc
    def parse(self, response):
        page = '__'.join(response.url.split('/')[2:])
        
        filename = path.abspath(path.join(basepath,"..","..",f'archive',f'{page}.html'))
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        for crumb in response.css('.breadcrumbs-carousel'):                                                 #selectors
            yield {
                'crumbs': response.css('.breadcrumbs-carousel').css('a ::text').getall()+
                crumb.xpath('normalize-space(.//div[@class="breadcrumbs-carousel--nolink"])').extract(),
                'brands':response.css('.ProductGrid_product-grid__Ph0C3').css('.title_title__brand__UX8j9').css('span ::text').getall(),
                'url':response.url

            }
    def spider_closed(self, spider):
        print('Closing {} spider'.format(spider.name))
        tar = tarfile.open(path.abspath(path.join(basepath,"..","..",f'archive.tar.gz')), "w:gz")
        tar.add(path.abspath(path.join(basepath,"..","..",f'archive')), arcname="htmls")
        tar.close()
        print("htmls saved to archive folder and into archive.tar.gz")
            
            
        
        