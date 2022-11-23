import scrapy
import csv
import os
import tarfile

class task1Spider(scrapy.Spider):
    name = "task1"
    def start_requests(self):
        with open('urls.csv', newline='') as csvfile:
            urls = csv.reader(csvfile, delimiter=' ', quotechar='|')                                    #open input file
            for url in urls:
                yield scrapy.Request(url=str(*url),callback=self.parse) 
            
                                                                                                        # save all htmls to archive
            tar = tarfile.open(os.path.join("/media/nizam/OS/work/task1/",f'archive.tar.gz'), "w:gz")
            tar.add("/media/nizam/OS/work/task1/archive", arcname="htmls")
            tar.close()

# callbackfunc
    def parse(self, response):
        page = '__'.join(response.url.split('/')[2:])
        
        os.makedirs("/media/nizam/OS/work/task1/archive", exist_ok=True)
        filename = os.path.join("/media/nizam/OS/work/task1/archive",f'{page}.html')
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
            
            
        
        