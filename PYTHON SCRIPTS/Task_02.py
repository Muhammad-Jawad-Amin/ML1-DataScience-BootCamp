stringlist = ["Saeed", "MOM", "owl", "SaS", "Fahad"]

for i in range(len(stringlist)):
    if stringlist[i].lower() == stringlist[i][::-1].lower():
        stringlist[i] = True
    else:
        stringlist[i] = False

print(stringlist)
