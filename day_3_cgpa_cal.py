#hsc cgpa calculator 

print('Bangla_1:')
Bangla_1 = int(input())

print('***********************************')
print('Bangla_2:')
Bangla_2 = int(input())

print('***********************************')
print('English_1:')
English_1 = int(input())

print('***********************************')
print('English_2:')
English_2 = int(input())

print('***********************************')
print('Math:')
Math = int(input())

print('***********************************')
print('Physics:')
Physics = int(input())

print('***********************************')
print('Chemistry:')
Chemistry = int(input())

print('***********************************')
print('Social:')
Social = int(input())

print('***********************************')
print('Religion:')
Religion = int(input())


total_average = (Bangla_1+Bangla_2+English_1+English_2+Math+Physics+Chemistry+Social+Religion)/9
print("your average number is : ", total_average)


#apply the condition

if total_average<=32:
 print("F")
elif total_average<=39:
 print("D") 
elif total_average<=49:
 print("C") 
elif total_average<=59:
 print("B") 
elif total_average<=69:
 print("A-") 
elif total_average<=79:
 print("A") 
elif total_average<=100:
 print("A+") 
 





