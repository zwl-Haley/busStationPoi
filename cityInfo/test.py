# -*- coding: utf-8 -*-


# import pymysql
# class BusPipeline(object):
#     def __init__(self):
#         self.connect = pymysql.connect(
#             host = "127.0.0.1",
#             port = 3306,
#             db = "map_data",
#             user = "root",
#             passwd = "wenliang960213",
#             charset = "utf8",
#             use_unicode = True
#             )
#         self.cursor = self.connect.cursor()
#         print("数据库连接成功...")

#     def process_item(self):
#         city_list = ["北京","天津","河北","山西","内蒙古","河南","湖南","湖北","黑龙江","吉林","辽宁","四川","云南","重庆","贵州","西藏","新疆","陕西","甘肃","宁夏","青海","特别行政","广东","广西","海南","上海","江苏","浙江","福建","山东","江西","安徽"]
#         self.cursor.execute(
#             "SELECT city,station FROM `mapbar` WHERE province = '北京';"
#             )
#         result = self.cursor.fetchall()
#         print(len(result))
#         # for i in result:
#         #     print(i[0]+i[1])
#         # self.connect.commit()


#     def close_spider(self):
#         self.connect.close()

# exe = BusPipeline()
# exe.process_item()
# exe.close_spider()

import requests
# s = requests.Session()
# headers = {"User-Agent":"Mozilla/5.0"}
# s.get("http://javeth.com",headers=headers)
# r = s.post("https://www.fembed.com/api/sources/1lv625k-l95",headers=headers)
# print(r.text)
# with open("a.png","wb") as f:
#     f.write(r.content)

# a = input("shuru:")
# code = s.get("http://kns.cnki.net/kns/brief/vericode.aspx?rurl=%2fkns%2fbrief%2fbrief.aspx%3fcurpage%3d15%26RecordsPerPage%3d20%26QueryID%3d8%26ID%3d%26turnpage%3d1%26tpagemode%3dL%26dbPrefix%3dSCDB%26Fields%3d%26DisplayMode%3dlistmode%26PageName%3dASP.brief_default_result_aspx&vericode={}".format(a),headers=headers)
"http://javeth.com/video/dandy-612-the-shy-wife-of-a-part-adopted-because-it-is-a-big-tits-is-a-nice-crest-of-sexual-harassment-manager-manager-when-two-people-alone-vol-1/"
r = requests.post("https://www.fembed.com/api/sources/6mo2z0dkdor",headers={"User-Agent":"Mozilla/5.0"})
print(r.text)