


from statistics import mean

productPrice = [10, 32, 43, 23, 12, 42]
sizeofList = len(productPrice)
avg = mean(productPrice)


print('List = ', productPrice)
print(sizeofList)
productPrice.reverse()
print(productPrice)
print(avg)