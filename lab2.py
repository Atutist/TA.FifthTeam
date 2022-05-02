import math
a = int(input("Input number: "))

l = []

def recconvert(b):
    if (b == 0):
        return 0
    dig = b % 2
    print(b)
    l.append(dig)
    recconvert(b // 2)
recconvert(a)
l.reverse()
print("Binary form by recursion:")
print(l)



r = []
def iterconvert(d):
    if d == 0:
        return 0
    while(d != 0):
        div = d % 2
        r.append(div)
        d = d // 2
    r.reverse()
    return r
print("Binary form by iteration:")
print(iterconvert(a))


def recurs(counter, a, b):
    if (counter == 0):
        return 0
    return math.sqrt(a + b * recurs(counter - 1, a + 1, b + 1))
b = int(input("Input recursion depth: "))
print("Result of recursion: ", recurs(b, 6, 2))