text = input("Введите текст на английском: ")
m = n = 0

# for i in text:
#     if "a" <= i <= "z":   # коды символов chr() и ord()
#         m += 1
#     elif "A" <= i <= "Z":
#         n += 1

for i in text: 
    if i.islower():
        m+=1 
    elif i.isupper():
        n+=1

print("Прописные буквы: % "+ str(n*100/len(text)))
print("Строчные буквы: % " + str(m*100/len(text)))



    