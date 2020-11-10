factors = [1, 2, 5, 10, 20, 50, 100, 200]
combos = []
current = ""
for i in range(200):
  current += " 1"
base = current
combos.append(current)
for i in range(100):
  current = current.replace(" 1", " 2", 1)
  current = current.replace(" 1", " ", 1)
  combos.append(current)
current = base
for i in range(40):
  current = current.replace(" 1", " 5", 1)
  current = current.replace(" 1", "", 4)
  combos.append(current)
for i in range(20):
  current = current.replace(" 5", " 10", 1)
  current = current.replace(" 5", "", 1)
  combos.append(current)
base = current
for i in range(10):
  current = current.replace(" 10", " 20", 1)
  current = current.replace(" 10", "", 1)
  combos.append(current)
current = base
for i in range(4):
  current = current.replace(" 10", " 50", 1)
  current = current.replace(" 10", "", 4)
  combos.append(current)
for i in range(2):
  current = current.replace(" 50", " 100", 1)
  current = current.replace(" 50", "", 1)
  combos.append(current)
for i in range(1):
  current = current.replace(" 100", " 200", 1)
  current = current.replace(" 100", "", 1)
  combos.append(current)
print(combos)
print(len(combos))
