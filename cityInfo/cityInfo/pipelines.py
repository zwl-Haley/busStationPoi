# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql

class CityinfoPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host = "127.0.0.1",
            port = 3306,
            db = "map_data",
            user = "root",
            passwd = "",
            charset = "utf8",
            use_unicode = True
            )
        self.cursor = self.connect.cursor()
        print("数据库连接成功...")

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """replace into city_info(province, city, citycode, district, address, adcode, location, level) value(%s, %s, %s, %s, %s, %s, %s, %s)""",
                    (item["province"],
                    item["city"],
                    item["citycode"],
                    item["district"],
                    item["address"],
                    item["adcode"],
                    item["location"],
                    item["level"]
                    )
                )
            self.connect.commit()
            return item
        except:
            with open("error.txt","a") as f:
                f.write(response.url + "\n")

    def close_spider(self, spider):
        self.connect.close()


# CREATE TABLE city_info (
#     auto_id INT NOT NULL primary key AUTO_INCREMENT,
#     province VARCHAR(20),
#     city VARCHAR(20),
#     citycode VARCHAR(20),
#     district VARCHAR(20),
#     address VARCHAR(100),
#     adcode VARCHAR(20),
#     location VARCHAR(20),
#     level VARCHAR(20));

