# QQS bilan mahsulot narxini hisoblash (15%)

price = float(input("Mahsulot narxini kirting: "))
qqs = round(price/100*15)
result = price + qqs

print(f"Mahsulot narxi: {price}\nQQS bilan: {result}")
