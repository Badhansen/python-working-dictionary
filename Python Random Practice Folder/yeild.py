l = []

for i in range(50):
    l.append(i%18)

#print(l)
print("\n")

def f():
    for i in l:
        yield print(i)

f()