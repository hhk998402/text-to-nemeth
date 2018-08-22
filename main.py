import english as eng
import brl2unicode
import nemethSystem as nm

brl=[]
index = 0

checkStr = input()
numericIndicator = False

while(index<len(checkStr)):

    # Checking if the character is a digit
    if(checkStr[index].isdigit()):
        if(not numericIndicator):
            brl.append(nm.numericIndicator)
        numericIndicator = True
        brl.append(nm.digits[checkStr[index]])
        index += 1
        continue

    #Checking if the character is a mathematical symbol
    if(checkStr[index] in nm.mathsym.keys()):
        data = nm.mathsym[checkStr[index]]
        print(len(data),checkStr[index])
        if(len(data)>6):
            data = map(''.join, zip(*[iter(data)] * 6))
            brl += list(data)
        else:
            brl.append(data)
        print(brl)
        index += 1
        continue

    #Checking if the character is an alphabet
    if(checkStr[index].isalpha()):
        if(checkStr[index].isupper()):
            brl.append(eng.specialCharacters['%capital'])
        brl.append(eng.alphabet[checkStr[index].lower()])
        numericIndicator = False        #Setting numericIndicator to False allows for the numeric indicator to be added later on
        index += 1
        continue


# for i in 'hemant':
#     brl.append(alphabets[i])
print(brl2unicode.toUnicodeSymbols([brl], flatten=True))
