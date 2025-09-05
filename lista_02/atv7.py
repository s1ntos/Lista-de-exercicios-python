list1 = []
list2 = []
listaT = []

for i in range(5):
    listA = int(input(f"Digite o numero {i+1}: "))
    listaT.append(listA)

print("")

for i in range(5):
    listB = int(input(f"Digite o numero {i+6}: "))
    listaT.append(listB)

print(listaT)