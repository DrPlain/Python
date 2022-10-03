def roman_to_num_converter(roman=""):
    all_roman_set = ['I', 'V','X','L','C','D','M']
    all_roman_dict = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    
    if not isinstance(roman, str):
        return "Invalid input"
    if roman == "":
        return "Empty string"
    roman = roman.strip().upper()
    if set(roman).issubset(set(all_roman_set)) == False:
        return "Invalid input"
    
    if len(set(roman)) == 1:
        for key in all_roman_dict:
            if list(set(roman))[0] == key:
                '''cases where input is key roman numeral or invalid input
                where a key numeral is repeated more than 3 times'''
                if len(roman) > 3:
                     return "Invalid input"
                elif len(roman) == 1:
                    return all_roman_dict[key]
                elif len(roman) == 2:
                    return all_roman_dict[key] * 2
                elif len(roman) == 3:
                    return all_roman_dict[key] * 3
    else:
        total = 0
        for key in all_roman_dict:
            for i, char in enumerate(roman):
                if char == key:
                        total += all_roman_dict[key]

                
        return total

test_dict = {
    0:'Invalid input',
    "":'Empty string',
    'ABC':'Invalid input',
    'IIII':'Invalid input',
    'i':1,
    'I':1,
    'V':5,
    'IX':9,
    'X':10,
    'xxx':30,
    'XL':40,
    'L':50,
    'XC':90,
    'C':100,
    'cL':150,
    'CDLVII':457,
    'DCCC':800,
    'CM':900,
    'LM':950,
    'MCDXCIV':1494,
    'MMMCDLVII':3457
}
def test(test_dict):
    passed = 0
    for key in test_dict:
        output = roman_to_num_converter(key)
        if output == test_dict[key]:
            print("Roman numeral: {}\nYour output: {}\nExpected output: {}\nRemark: PASSED".format(key, output, test_dict[key]))
            print()
            passed += 1
        else:
            print("Roman numeral: {}\nYour output: {}\nExpected output: {}\nRemark: FAILED".format(key, output, test_dict[key]))
            print()
        
    print("Overall summary: {} out of {} tests passed".format(passed, len(test_dict)))

test(test_dict)
