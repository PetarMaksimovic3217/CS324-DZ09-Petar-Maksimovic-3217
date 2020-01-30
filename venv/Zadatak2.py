symbols = ".,:!"
text = ("Commander, your base is under attack! ")
for ch in symbols:
    text = text.replace(ch, '')
resenje = text.split()
print(resenje)