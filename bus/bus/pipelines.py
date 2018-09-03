# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class BusPipeline(object):
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
        self.cursor.execute(
            """replace into mapbar(province, city, station) value(%s, %s, %s)""",
                (item["province"],
                item["city"],
                item["station"]
                )
            )
        self.connect.commit()
        return item

    def close_spider(self, spider):
        self.connect.close()

# CREATE TABLE mapbar (
#     auto_id INT NOT NULL primary key AUTO_INCREMENT,
#     province VARCHAR(20),
#     city VARCHAR(20),
#     station VARCHAR(50));