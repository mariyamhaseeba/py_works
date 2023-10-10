items=[
    {"id":1,"name":"sugar","price":40,"avl_qty":10},
    {"id":2,"name":"milk","price":28,"avl_qty":40},
    {"id":3,"name":"teapowder","price":230,"avl_qty":100},
    {"id":4,"name":"tomatto","price":120,"avl_qty":5},
    {"id":5,"name":"potatto","price":45,"avl_qty":70},
    {"id":6,"name":"carrot","price":80,"avl_qty":0},
    {"id":7,"name":"oreo","price":45,"avl_qty":0},
    {"id":8,"name":"hideandseek","price":50,"avl_qty":50},
    
]

# total num of item
# print all product names
# print all in stock product names
# print product names avaialble under rs 50
# print all product names avilable in ranage of 20 to 50




# print(len(items))
# for i in items:
    # print(i.get("name"))

# for i in items:
#     if i.get("avl_qty")>0:
#         print(i.get("name"))


# for i in items:
#     if i.get("price")<50:
#         print(i.get("name"))

for i in items:
    if i.get("price")<50 and i.get("price")>30:
        print(i.get("name"))