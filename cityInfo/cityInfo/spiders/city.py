# -*- coding: utf-8 -*-
import scrapy
from cityInfo.items import CityinfoItem
import json
import pymysql

class CitySpider(scrapy.Spider):
    name = 'city'

    def __init__(self):
        self.connect = pymysql.connect(
            host = "127.0.0.1",
            port = 3306,
            db = "map_data",
            user = "root",
            passwd = "wenliang960213",
            charset = "utf8",
            use_unicode = True
            )
        self.cursor = self.connect.cursor()
        print("数据库连接成功...")

    def start_requests(self):
        city_list = ["北京","天津","河北","山西","内蒙古","河南","湖南","湖北","黑龙江","吉林","辽宁","四川","云南","重庆","贵州","西藏","新疆","陕西","甘肃","宁夏","青海","特别行政","广东","广西","海南","上海","江苏","浙江","福建","山东","江西","安徽"]
        city_list1 = ["北京","天津","河北","山西","内蒙古","河南","湖南","湖北","黑龙江","吉林","辽宁","四川","云南","重庆","贵州","西藏","新疆","陕西","甘肃","宁夏","青海"]
        city_list2 = ["特别行政","广东","广西","海南","上海","江苏","浙江","福建","山东","江西","安徽"]
        for city in city_list2:
            self.cursor.execute(
                "SELECT city,station FROM `mapbar` WHERE province = '{}';".format(city)
                )
            result = self.cursor.fetchall()
            for addr in result:
                address = addr[0]+addr[1]
                baidu_api = "https://restapi.amap.com/v3/geocode/geo?address={}&output=json&key=dc101d293ae2286387cfeb55893e87fa".format(address)
                yield scrapy.Request(baidu_api)

    def parse(self, response):
        item = CityinfoItem()
        content = json.loads(response.text)
        try:
            data = content["geocodes"][0]
            level = data["level"]
            if not level in "省市区":
                address = data["formatted_address"]
                province = data["province"]
                citycode = data["citycode"]
                city = data["city"]
                adcode = data["adcode"]
                location = data["location"]
                district = data["district"]
                item["address"] = address
                item["province"] = province
                item["citycode"] = citycode
                item["city"] = city
                item["adcode"] = adcode
                item["location"] = location
                item["level"] = level
                item["district"] = district
                yield item
            else:
                raise parseError()
        except:
            with open("error.txt","a") as f:
                f.write(response.url + "\n")