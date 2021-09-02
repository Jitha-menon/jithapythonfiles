products=[
    {"p_name":"complan","mrp":230,"avl_qty":50},
    {"p_name": "horlicks", "mrp": 250, "avl_qty": 10},
    {"p_name": "bournvita", "mrp": 220, "avl_qty": 0},
    {"p_name": "nutricharge", "mrp": 200, "avl_qty": 100},
    {"p_name": "mylo", "mrp": 100, "avl_qty": 0},

]
#print all product names

prod_name=list(map(lambda item:item['p_name'],products))
print(prod_name)

#print all products availabl in shop

products=list(filter(lambda item:item['avl_qty']>0,products))
print(products)

#print out of stock products

out=list(filter(lambda item:item['avl_qty']==0,products))
print(out)

#print max of prices

prices=list(map(lambda product:product['mrp'],products))
print(max(prices))
