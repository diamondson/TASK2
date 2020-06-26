names = ["Manas", "Almaz", "Meerim", "Aibek"]
names2 = ["Mirbek", "Meerim", "Almaz"]

names3 = []

for name in names:
    if name not in names2:
        names3.append(name)

for names in names3:
    print(names)