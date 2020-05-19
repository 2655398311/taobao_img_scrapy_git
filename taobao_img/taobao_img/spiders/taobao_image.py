# -*- coding: utf-8 -*-
import scrapy


class TaobaoImageSpider(scrapy.Spider):
    name = 'taobao_image'
    allowed_domains = ['https://detail.tmall.com/item.htm']
    aa = ['588716552280']
    #,'600815644588'
    start_urls = ['https://detail.tmall.com/item.htm?id=613252867568&spm=a220o.1000855.1998099587.7.760140a9yQ3pfj']

    def start_requests(self):
        # url = "https://detail.tmall.com/item.htm?id={id}&spm=a220o.1000855.1998099587.7.760140a9yQ3pfj"
        url = 'https://item.taobao.com/item.htm?ft=t&id={id}&spm=a220o.1000855.1998099587.7.760140a9yQ3pfj'
        for i in self.aa:
            yield scrapy.Request(url.format(id=i), dont_filter=True)

    def parse(self, response):
        item={}
        item['img_one'] = response.xpath("//ul[@class='tb-thumb tb-clearfix']//li//div//a//@data-src")
        print(item['img_one'])
        # if item['img_one'] is None:
        #     item['img_two'] = response.xpath("//div[@class='tb-thumb-content']//ul/li[5]//a//@src").getall()
        #     print(item['img_two'])
