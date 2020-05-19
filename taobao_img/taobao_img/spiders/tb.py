# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils.response import open_in_browser
from taobao_img.settings import MONGODB_HOST
class TbSpider(scrapy.Spider):
    name = 'tb'
    # allowed_domains = ['https://detail.tmall.com/item.htm?']
    start_urls = ['https://item.taobao.com/item.htm?spm=a1z10.1-c-s.w5003-21750019205.1.7164290dMuEs53&ft=t&id=613605312243&scene=taobao_shop']
    aa = ['613605312243','591562254705']
    #,'600687505853','602595736048'
    headers = {
            ':authority': 'item.taobao.com',
            ':method': 'GET',
            ':path': '/item.htm?spm=a1z10.1-c-s.w5003-21750019205.1.7164290dMuEs53&ft=t&id=613605312243&scene=taobao_shop',
            ':scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}

    def start_requests(self):
        for i in self.aa:
            url = "https://item.taobao.com/item.htm?spm=a1z10.1-c-s.w5003-21750019205.1.7164290dMuEs53&ft=t&id={}&scene=taobao_shop".format(i)
            yield scrapy.Request(url, dont_filter=True, cb_kwargs={'user_id': i})

    def parse(self, response, user_id):
        # print(dict(response.request.headers))
        # open_in_browser(response)
        #//img/@data-src
        url_list = response.xpath("//*[@class='tb-pic tb-s50']")
        for a in url_list:
            aac = a.xpath('.//img/@data-src').getall()
            for list_item in aac:
                item = {'url':'http'+list_item,'goods_id':user_id}
                # item['goods_id'] = user_id
                # print(item['url'])
                yield item
            # print(item['url'])
        # urls = [response.urljoin(i) for i in url_list]

