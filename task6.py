number = int(input("Введите целое число: "))

number = [value for value in range(1,number + 1)] #генератор списка

factorial = 1

for i in number:
    factorial*=i

print(factorial)