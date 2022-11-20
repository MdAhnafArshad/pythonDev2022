#I have only one cake recode solve out becouse there are  same methode technic for  each on cake.
# solve out  the cake problem
#question1:
#Different type of cakes flavour name
cake1  = "Black Forest"
cake2 = "Vanilla Cake"
cake3 = "Red Velvet"
cake4 = "Lemon Sponge"
cake5 = "Chocklet"
print('Different type of cake flavours name: ')
print(cake1,',', cake2,',', cake3,',', cake4,',', cake5)

#question2

#cake1
BFc_materialCost = 180
transportationCost = 150
utilityCost = ((BFc_materialCost+transportationCost)*3)/100
spaceCost = 50
staffCost = 60
inventoryCost = (BFc_materialCost+transportationCost+utilityCost+spaceCost+staffCost)
print(cake1,"Inventory cost is: ",inventoryCost,'Tk')

#question3 after discount each pound
cake1SellingPriceEP= 780
print(cake1SellingPriceEP)

#question4 Before discount each pound

Beforecake1SellingPriceEP = (cake1SellingPriceEP-((cake1SellingPriceEP*5)/100))
print('Discount Price: ',Beforecake1SellingPriceEP,'TK')

#END