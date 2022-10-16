dic = { "product" : ["fan", "Tv", "lamp", "computer"],
             "price" : [200, 500, 100, 700],
             "quantity" : [2, 3, 1, 4] }
for x in dic["product"]:
  n = dic["product"].index(x)
  print(x + str(dic["price"][n] * dic["quantity"][n]))