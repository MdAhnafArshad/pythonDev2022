


from statistics import mean

productPrice = [10, 32, 43, 23, 12, 42]
sizeOfList = len(productPrice)
avg = mean(productPrice)


print('List = ', productPrice)
print(sizeOfList)
productPrice.reverse()
print(productPrice)
print(avg)