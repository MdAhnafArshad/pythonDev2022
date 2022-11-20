


from statistics import mean

productPrice = [10, 32, 43, 23, 12, 42]
sizeOfList = len(productPrice)
avg = mean(productPrice)


print('List value is: ', productPrice)
print("list length is:",sizeOfList)
#use reverse function
productPrice.reverse()
print("Revars the list Number: ",productPrice)
print("avarage Number:", avg)