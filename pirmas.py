# 1.1

for sk in range(1, 101):
    print(sk, end=" | ")
print("")

# 1.2

for sk in range(1, 101):
    print(sk, end=" | ")
    if sk == 20:
        break
print("")

# 1.3

for sk in range(1, 101):
    if sk in range(1, 11):
        continue
    print(sk, end=" | ")
print("")

# 1.4

for sk in range(1, 101):
    if sk == 20:
        break
    if sk % 2 == 0:
        continue
    print(sk, end=" | ")
print("")

# Arba.

for sk in range(1, 101):
    if sk % 2 == 0:
        continue
    print(sk, end=" | ")
    if sk == 19:
        break
print("")

# Praleidžiame lyginius skaičius (iki vartotojo pasirinkimo), kurie dalinasi iš 9. Nebus 18 ir 36 it t.t.

sustoti = int(input("Įveskite skaičių, ties kuriuo nustoti tyrinėti seką: "))
for sk in range(1, 101):
    if sk % 2 == 0 and sk % 9 == 0:
        continue
    print(sk, end=" | ")
    if sk == sustoti:
        break
print("")

# Praleidžiame visus skaičius (iki vartotojo pasirinkimo) išskyrus tuos, kurie dalinasi iš 2 ir 9. Bus 18 ir 36 it t.t.

sustoti = int(input("Įveskite skaičių, ties kuriuo nustoti tyrinėti seką: "))
for sk in range(1, 101):
    if sk == sustoti:
        break
    if not (sk % 2 == 0 and sk % 9 == 0):
        continue
    print(sk, end=" | ")
print("")

