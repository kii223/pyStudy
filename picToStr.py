from PIL import Image

ascii_char = list('$@B%8&WM#*oahkbdpqwmZ0OQLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. ')

def getChar(r, g, b, alpha=256.0):
    if alpha == 0:
        return ' '
    else:
        lengthC = len(ascii_char)
        grey = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        unit = (256.0 + 1)
        return ascii_char[int((grey/unit) * lengthC)]


im = Image.open('biki.jpg')
pix = im.load()
x, y = im.size
print(x, y)

listAll = []
textOut = ''
for i in range(0, y):
    for j in range(0, x):
        r, g, b = pix[j, i]
        strW = getChar(r, g, b)
        textOut += strW
    textOut += '\n'

with open('str3.txt', 'w') as f:
   f.write(textOut)

print(textOut)


