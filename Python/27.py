dic = { "product" : ["fan", "Tv", "lamp", "computer"],
             "price" : [200, 500, 100, 700],
             "quantity" : [2, 3, 1, 4] }
s = []
for x in dic["product"]:
  n = dic["product"].index(x)
  s.append(dic["price"][n] * dic["quantity"][n])
  dic.update({"sum": s})
print(dic)