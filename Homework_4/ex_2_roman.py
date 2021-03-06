def roman_to_int(roman):
    roman_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000, IV=4, IX=9, XL=40, XC=90, CD=400, CM=900)
    i = 0
    num = 0
    while i < len(roman):
        if i + 1 < len(roman) and roman[i:i + 2] in roman_dict:
            num += roman_dict[roman[i:i + 2]]
            i += 2
        else:
            num += roman_dict[roman[i]]
            i += 1
    return num


print(roman_to_int(input("Input a roman num :")))

