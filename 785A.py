t = int(input())
count = 0
for i in range(t):
    n = input()
    if n == "Tetrahedron":
       count += 4
    if n == "Cube":
        count+=6
    if n == "Octahedron":
        count+=8
    if n == "Dodecahedron":
        count+=12
    if n == "Icosahedron":
        count+=20
print(count)

