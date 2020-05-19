# -*- coding: utf-8 -*-
import scrapy


class DescSpider(scrapy.Spider):
    name = 'desc'
    allowed_domains = ['https://item.taobao.com/item.htm?spm=a230r.7195193.1997079397.9.10636f2dsS7T1r&id=607568683404&abbucket=9']
    start_urls = ['https://item.taobao.com/item.htm?spm=a230r.7195193.1997079397.9.10636f2dsS7T1r&id=607568683404&abbucket=9']
    headers = {
        ':authority': 'item.taobao.com',
        ':method': 'GET',
        ':path': '/item.htm?spm=a1z10.1-c-s.w5003-21750019205.1.7164290dMuEs53&ft=t&id=613605312243&scene=taobao_shop',
        ':scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    def parse(self, response):
        desc_list = response.xpath("//ul[@class='attributes-list']")
        item = {}
        for i in desc_list:
            item['desc'] = i.xpath(".//li/text()").getall()
            print(item)
        pass
