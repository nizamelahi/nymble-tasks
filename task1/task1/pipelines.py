# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re

class Task1Pipeline:
    def process_item(self, item, spider):

        crumbstr=""
        duplicateremove={}
        brandstr=""
        item['data']=item['url']

        if 'crumbs' in item:                                    #crumb formatting and duplicate removal
            del item['crumbs'][0]                               #homepage crumb removal
            for x in item['crumbs']:   
                duplicateremove[x]=1
            crumbstr='/'.join(list(duplicateremove.keys()))
            del item['crumbs']
            item['data']+=(re.sub(r'\d+', '',","+crumbstr))

        duplicateremove.clear()

        if 'brands' in item:                                    #brand formatting and duplicate removal
            for x in item['brands']:   
                duplicateremove[x]=1
            brandstr=','.join(list(duplicateremove.keys()))
            print(brandstr)
            del item['brands']
            item['data']+=(","+brandstr)
        
        del item['url']
        
        
        

        return item
 