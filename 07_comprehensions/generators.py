sales = [12,4,3,6,8,12,13,10]

totalSales = sum(sale for sale in sales if sales > 8)
print(totalSales)