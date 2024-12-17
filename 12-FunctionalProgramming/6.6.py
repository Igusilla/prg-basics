
names = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
        ("Jackson","Peter"),("Johnson","Rick"),
        ("Lewis","Terry"),("Clarke","Robin")]
capital = list(map(lambda x: x[0].upper(), names))
imiona = list(map(lambda x: x[1], names)) 
for i in range(len(names)):
    print(f'{capital[i]}, {imiona[i]}')