letter=''' Dear <|name|>
           you are selected
           Dear <|date|>'''
print(letter.replace("<|name|>","Akash").replace("<|date|>","20th August"))