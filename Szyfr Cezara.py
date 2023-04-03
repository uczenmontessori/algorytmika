def szyfr(move,text):
    text2 = ''
    move2 = (move%26)
    for litera in text:
        if move2 + ord(litera) > 122:
            text2 = text2 + chr(ord(litera) + move2 - 26)
        # bład jest w linijce:
        else:
            text2 = text2 + chr(ord(litera) + move2)
        
    return text2
print(szyfr(1,"abcxyz"))
