def szyfr(move,text):
    text2 = ''
    move2 = (move%26)
    for litera in text:
        text2 = text2 + chr(ord(litera) + move2)
        
    return text2
print(szyfr(27,"za"))