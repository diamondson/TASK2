time1 = input("Введите цифровое время-1 через двоеточие: ")
time2 = input("Введите цифровое время-2 через двоеточие: ")

time1 = time1.split(":")
time2 = time2.split(":")

time1 = list(map(int, time1))
time2 = list(map(int, time2))

x = time1[0]*3600 + time1[1]*60 + time1[2]
y = time2[0]*3600 + time2[1]*60 + time2[2]

#x = int(time1[0])*3600 + int(time1[1])*60 + int(time1[2])
#y = int(time2[0])*3600 + int(time2[1])*60 + int(time2[2])

print(y - x)