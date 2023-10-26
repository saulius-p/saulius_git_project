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