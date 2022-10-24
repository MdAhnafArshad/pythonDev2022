#Bangla
print("Bangla_1Paper")
bangla_1stPaper = 70
bangla_2ndPaper = 90
overall_bangla = (bangla_1stPaper+bangla_2ndPaper)/2

#English
english_1stPaper = 75
english_2ndPaper = 75
overall_english = (english_1stPaper+english_2ndPaper)/2

#Mathematice
mathematice = 80


#science
T=(75*33)/100
P= (25*33)/100


#higher_math
higher_math_T = (43*33)/100
higher_math_P = (17*33)/100
higher_math_number1 = 43
higher_math_number2 = 17
higher_math_total = higher_math_number1+higher_math_number2


#biology_07
biology_T = (43*33)/100
biology_P = (17*33)/100
biology_number1 = 57
biology_number2 = 20
biology_total = biology_number1+biology_number2


#Physics_08
Physics_T = (43*33)/100
Physics_P = (17*33)/100
Physics_number1 = 70
Physics_number2 = 5
Physics_total = Physics_number1+Physics_number2


#chemistry_09
chemistry_T = (43*33)/100
chemistry_P = (17*33)/100
chemistry_number1 = 70
chemistry_number2 = 25
chemistry_total = chemistry_number1+chemistry_number2



#Religion_10
Religion = 90



#social_science_11
social_science = 65


#bangla_1stPaper_01
if bangla_1stPaper <= 32 or bangla_2ndPaper <= 32: 
    print("Bangla_1st paper = F")
elif bangla_1stPaper <=39:
    print("Bangla_1st paper = D")
elif bangla_1stPaper <= 49:
    print("Bangla_1st paper = C")
elif bangla_1stPaper <= 59:
    print("Bangla_1st paper = B")
elif bangla_1stPaper <= 69:
    print("Bangla_1st paper = A-")
elif bangla_1stPaper <= 79:
    print("Bangla_1st paper = A")
elif bangla_1stPaper <= 100:
    print("Bangla_1st paper = A+")

#bangla_2ndPaper_02
if bangla_1stPaper <= 32 or bangla_2ndPaper <= 32: 
    print("Bangla_2nd paper = F")
elif bangla_2ndPaper <=39:
    print("Bangla_2nd paper = D")
elif bangla_2ndPaper <= 49:
    print("Bangla_2nd paper = C")
elif bangla_2ndPaper <= 59:
    print("Bangla_2nd paper = B")
elif bangla_2ndPaper <= 69:
    print("Bangla_2nd paper = A-")
elif bangla_2ndPaper <= 79:
    print("Bangla_2nd paper = A")
elif bangla_2ndPaper <= 100:
    print("Bangla_2nd paper = A+")


print("Bangla_overall: ", overall_bangla)


#english_1stPaper_03
if english_1stPaper <= 32 or english_2ndPaper <= 32: 
    print("English_1st paper = F")
elif english_1stPaper <=39:
    print("English_1st paper = D")
elif english_1stPaper <= 49:
    print("English_1st paper = C")
elif english_1stPaper <= 59:
    print("English_1st paper = B")
elif english_1stPaper <= 69:
    print("English_1st paper = A-")
elif english_1stPaper <= 79:
    print("English_1st paper = A")
elif english_1stPaper <= 100:
    print("English_1st paper = A+") 

#english_2ndPaper_04
if english_1stPaper <= 32 or english_2ndPaper <= 32: 
    print("Englsih_2nd paper = F")
elif english_2ndPaper <=39:
    print("Englsih_2nd paper = D")
elif english_2ndPaper <= 49:
    print("Englsih_2nd paper = C")
elif english_2ndPaper <= 59:
    print("Englsih_2nd paper = B")
elif english_2ndPaper <= 69:
    print("Englsih_2nd paper = A-")
elif english_2ndPaper <= 79:
    print("Englsih_2nd paper = A")
elif english_2ndPaper <= 100:
    print("Englsih_2nd paper = A+")

print("ovarall_english: ", overall_english)

#mathematice_05
if mathematice <= 32: 
    print("Mathematic = F")
elif mathematice <=39:
    print("Mathematic = D")
elif mathematice <= 49:
    print("Mathematic = C")
elif mathematice <= 59:
    print("Mathematic = B")
elif mathematice <= 69:
    print("Mathematic = A-")
elif mathematice <= 79:
    print("Mathematic = A")
elif mathematice <= 100:
    print("Mathematic = A+")



#higher_math_06
if higher_math_T < T or higher_math_P < P: 
    print("Higher_Math = F")
else:
    if higher_math_total <= 32: 
        print("Higher_Math = F")
    elif higher_math_total  <= 39:
        print("Higher_Math = D")
    elif higher_math_total  <= 49:
        print("Higher_Math = C")
    elif higher_math_total  <= 59:
        print("Higher_Math = B")
    elif higher_math_total  <= 69:
        print("Higher_Math = A-")
    elif higher_math_total  <= 79:
        print("Higher_Math = A")
    elif higher_math_total  <= 100:
        print("Higher_Math = A+")


#biology_07
if biology_T < T or biology_P < P: 
        print("biology_total = F")
else:
    if biology_total <= 32: 
        print("biology_total = F")
    elif biology_total  <= 39:
        print("biology_total = D")
    elif biology_total  <= 49:
        print("biology_total = C")
    elif biology_total  <= 59:
        print("biology_total = B")
    elif biology_total  <= 69:
        print("biology_total = A-")
    elif biology_total  <= 79:
        print("biology_total = A")
    elif biology_total  <= 100:
        print("biology_total = A+")

#Physics_08
if Physics_T < T or Physics_P < P: 
        print("Physics_total = F")
else:
    if  Physics_total <= 32: 
        print("Physics_total = F")
    elif Physics_total  <= 39:
        print("Physics_total = D")
    elif Physics_total  <= 49:
        print("Physics_total = C")
    elif Physics_total  <= 59:
        print("Physics_total = B")
    elif chemistry_total  <= 69:
        print("Physics_total = A-")
    elif Physics_total  <= 79:
        print("Physics_total = A")
    elif Physics_total  <= 100:
        print("Physics_total = A+")



#chemistry_09
if chemistry_T < T or chemistry_P < P: 
        print("Chemistry_total = F")
else:
    if  chemistry_total <= 32: 
        print("Chemistry_total = F")
    elif chemistry_total  <= 39:
        print("Chemistry_total = D")
    elif chemistry_total  <= 49:
        print("Chemistry_total = C")
    elif chemistry_total  <= 59:
        print("Chemistry_total = B")
    elif chemistry_total  <= 69:
        print("Chemistry_total = A-")
    elif chemistry_total  <= 79:
        print("Chemistry_total = A")
    elif chemistry_total  <= 100:
        print("Chemistry_total = A+")



#Religion_10
if Religion <= 32: 
    print("Religion = F")
elif Religion <=39:
    print("Religion = D")
elif Religion <= 49:
    print("Religion = C")
elif Religion <= 59:
    print("Religion = B")
elif Religion <= 69:
    print("Religion = A-")
elif Religion <= 79:
    print("Religion = A")
elif Religion <= 100:
    print("Religion = A+")


#social_science_11
if social_science <= 32: 
    print("Social_Science = F")
elif social_science <=39:
    print("Social_Science = D")
elif social_science <= 49:
    print("Social_Science = C")
elif social_science <= 59:
    print("Social_Science = B")
elif social_science <= 69:
    print("Social_Science = A-")
elif social_science <= 79:
    print("Social_Science = A")
elif social_science <= 100:
    print("Social_Science = A+")

#total_Point
total_Point = (bangla_1stPaper+bangla_2ndPaper+english_1stPaper+english_2ndPaper+mathematice+higher_math_total+biology_total+Physics_total+chemistry_total+Religion+social_science)/11

print("Total_grade : ", total_Point)

#Total_grade
if (bangla_1stPaper<=32 or bangla_2ndPaper <= 32 or english_1stPaper <=32 or english_2ndPaper <=32 or mathematice<=32 or higher_math_P <P or higher_math_T < T or biology_T<T or biology_P<P or Physics_T<T or Physics_P <P or chemistry_P <P or chemistry_T<T or Religion<=32 or social_science <=32):
    print("total_grade = F")
else :   
    if total_Point <= 32: 
        print("total_grade = F")
    elif total_Point <=39:
        print("total_grade = D")
    elif total_Point <= 49:
        print("total_grade = C")
    elif total_Point <= 59:
        print("total_grade = B")
    elif total_Point <= 69:
        print("total_grade = A-")
    elif total_Point <= 79:
        print("total_grade = A")
    elif total_Point <= 100:
        print("total_grade = A+")

