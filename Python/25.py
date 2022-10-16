dic = { "product" : ["fan", "Tv", "lamp", "computer"],
             "price" : [200, 500, 100, 700],
             "quantity" : [2, 3, 1, 4] }
for x in dic["product"]:
  n = dic["product"].index(x)
  print("ชื่อ " + x + " ราคา " + str(dic["price"][n]) + " จำนวนสินค้า " + str(dic["quantity"][n]))