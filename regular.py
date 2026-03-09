import re

patter = r'[A-z]yclone'
text = 'Dyclone cyclone'

matches = re.finditer(patter, text)

for i in matches:
    print(i.span())
    print(text[i.span()[0]:i.span()[1]])