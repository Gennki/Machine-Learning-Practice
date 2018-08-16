import pymongo

# 创建数据库,如果数据库已经存在的话,则不会再被创建,collection(集群)同样如此
myClient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myClient["test"]  # 创建数据库,当创建collection并插入数据后才会真正创建
col = db['table1']  # 创建当创建collection并插入数据后才会真正创建,当插入数据后才会真正创建

# # =============================================插入一条数据=============================================
# dict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
# result = col.insert_one(dict)  # 插入数据
# print(result.inserted_id)  # 插入数据后返回的id
#
# # =============================================插入多条数据=============================================
# dict = [
#     {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
#     {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
#     {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
#     {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
#     {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
# ]
# result = col.insert_many(dict)
# print(result.inserted_ids)
#
# # =============================================插入指定id的数据=============================================
# dict = [
#     {"_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
#     {"_id": 2, "name": "Google", "address": "Google 搜索"},
#     {"_id": 3, "name": "Facebook", "address": "脸书"},
#     {"_id": 4, "name": "Taobao", "address": "淘宝"},
#     {"_id": 5, "name": "Zhihu", "address": "知乎"}
# ]
#
# x = col.insert_many(dict)
# # 输出插入的所有文档对应的 _id 值
# print(x.inserted_ids)

# # =============================================查找一条记录=============================================
# result = col.find_one()
# print(result)
#
# # =============================================查找所有记录=============================================
# for result in col.find():
#     print(result)
#
# # =============================================查询指定字段的数据=============================================
# # 除了 _id 你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。
# for result in col.find({}, {"_id": 0, 'name': 1, 'alexa': 1}):
#     print(result)
#
# # =============================================根据指定条件查询=============================================
# query = {"name": "RUNOOB"}
# for result in col.find(query):
#     print(result)
#
# # ===============================高级查询,查找 name 字段中第一个字母 ASCII 值大于 "H" 的数据========================
# query = {"name": {"$gt": "H"}}
# for result in col.find(query):
#     print(result)
#
# # ===============================使用正则表达式查询,查询 name 字段中第一个字母为 "R" 的数据===============================
# query = {"name": {"$regex": "^R"}}
# for result in col.find(query):
#     print(result)
#
# # ===============================分页查找===============================
# for result in col.find().limit(3).skip(1):
#     print(result)

# # ===============================修改一条记录===============================
# query = {"alexa": "10000"}
# newValues = {"$set": {"alexa": "12345"}}
# col.update_one(query, newValues)
# # ===============================修改多条记录===============================
# query = {"name": {"$regex": "^F"}}
# newValues = {"$set": {"alexa": "123"}}
# x = col.update_many(query, newValues)
# print(x.modified_count, "文档已修改")


# ===============================删除一条记录===============================
query = {"name": "Taobao"}
col.delete_one(query)

# ===============================删除多条记录===============================
query = {"name": {"$regex": "^F"}}
result = col.delete_many(query)
print(result.deleted_count, "个文档已删除")

# ===============================删除所有记录===============================
result = col.delete_many({})
print(result.deleted_count, "个文档已删除")

# ===============================删除collection(集群)===============================
col.drop()  # 如果删除成功 drop() 返回 true，如果删除失败(集合不存在)则返回 false。
