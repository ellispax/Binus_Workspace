# roman to arabic and vice versa

def romanArabic(arg):
    if type(arg) == int:
        conv = [[10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']] # different arragement
        result = ""
        i = 0
        while arg > 0:
            while conv[i][0] > arg: i+=1
            result += conv[i][1]
            arg -= conv[i][0]
        print(result)
    elif type(arg) == str:
        arg = arg.upper()
        conv = [[9, 'IX'], [4, 'IV'], [10, 'X'], [5, 'V'], [1, 'I']] # different arragement
        result = 0
        i = 0
        while arg != "":
            if conv[i][1] in arg:
                result += conv[i][0]
                arg = arg.replace(conv[i][1], "", 1)
            else:
                i += 1
        print(result)
    else:
        print("Type not supported")

romanArabic(str(input("Enter the Roman number you want to convert to latin >> ")))
romanArabic(int(input("Enter the Latin number you want to convert to Roman>> ")))