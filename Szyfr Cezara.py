#nadal nie wiem o co chodzi
#...
def szyfr(move,text):
    text2 = ''
    move2 = (move%26)
    for litera in text:
        # bład jest w linijce:
        text2 = text2 + chr(ord(litera) + move2)
        
    return text2
print(szyfr(27,"za"))
