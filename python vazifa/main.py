# x= [1,33,43,12,55]
# katta = x[0]
# i = 0
# while i < len(x):
#    if katta < x[i]:
#        katta = x[i]
#    i+=1
# print(katta)
# print ("")
#
# son = int(input("sonni kiriting"))
# son1 = int(input("sonni kiriting"))
# n = 0
# while n < son:
#     print(son1)
#     n+=1
# print(son1)
# natija = []
# son = int(input('3-xonali sonni kiriting'))
# while son <= 999:
#      bir = son // 100
#      ikki = (son // 10) % 10
#      uch = son % 10
#      result = bir + ikki + uch
#      if son > 8 and son > 5:
#          natija.append(son)
#      son+=1
# print(natija)

# a = int(input("sonni kiritng"))
# b = int(input("sonni kiriting"))
# c = 2
# while c
# x = [1,21,22,34,332,23,4322]
# katta = x[0]
# i = 0
# index = 0
# while i < len(x):
#       if katta < x[i]:
#          katta = x[i]
#       print(x[i])
#       index = i
#       i+=1
# print(katta)
# print(index
parking_zone = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
while True:
    row = int(input("row:"))
    col = int(input("col:"))
    carname = input("enter carname:")
    if parking_zone[row][col] == 0:
       parking_zone[row][col] = carname
       print(f"{carname} bu joyga {row+1} {col+1} parkovka qilindi")
       for i in parking_zone:
           for j in i:
                   print(j, end=" ")
           print()
    else:
        print(f"bu {row+1}:{col+1} joyga {carname} joylashtirildi.")
        print("Boshqa joyga joylashting")
        continue
    cars = input("yana mashina joylashtirasizma ha/yuq").lower
    if cars != "yuq":
    #     row = int(input("row:"))
    #     col = int(input("col:"))
    #     carname = input("enter carname:")
    #     if parking_zone[row][col] != 0:
    #         print(f"bu joy band chunki bu yerda {carname} bor")
    #     else:
    #         if parking_zone[row][col] == 0:
    #            parking_zone[row][col] = carname
    #         print(f"buy joyga {carname} joylashtirildi.")
    # else:
    #     if cars == "yuq":
           print("jarayon yakunlandi")
           break