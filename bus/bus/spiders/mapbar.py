# -*- coding: utf-8 -*-
import scrapy
import re
from bus.items import BusItem

class MapbarSpider(scrapy.Spider):
    name = 'mapbar'
    start_urls = ['http://bus.mapbar.com/city/change/']

    def parse(self, response):
        #每个城市公交信息
        city_url = response.xpath("//td//a/@href").extract()
        for station_urls in city_url:
            #产生A-Z的字符列表
            A_Z = [chr(i) for i in range(ord("A"),ord("Z")+1)]
            for i in A_Z:
                #http://bus.mapbar.com/beijing/poi_Z/表示北京市地名以Z开头的站点
                station_url = station_urls + "poi_" + i
                yield scrapy.Request(station_url, callback=self.parse_station)

    def parse_station(self, response):
        item = BusItem()
        text = response.text
        #省
        province = re.findall(r'province=(.*?);',text)[0]
        #城市
        city = re.findall(r'city=(.*?);',text)[0]
        #公交站列表
        station_list = re.findall(r'title=".*" target="_blank">(.*?)</a>',text)
        for station in station_list:
            item["province"] = province
            item["city"] = city
            item["station"] = station
            yield item
