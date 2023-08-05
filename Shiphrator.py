def encrypt(text):
    i = 0
    str = ''
    if len(text) % 2 == 0:
        while i < len(text):
            if i == 0 or i % 2 == 0:
                result1 = text[i + 1]
                str = str + result1
            elif i != 0 or i % 2 != 0:
                result2 = text[i - 1]
                str = str + result2
            i = i + 1
        return str
    elif (len(text) - 1) % 2 == 0:
        while i < len(text) - 1:
            if i == 0 or i % 2 == 0:
                result1 = text[i + 1]
                str = str + result1
            elif i != 0 or i % 2 != 0:
                result2 = text[i - 1]
                str = str + result2
            i = i + 1
        return str + text[len(text) - 1]
print(encrypt('attack!')) #taatkc!