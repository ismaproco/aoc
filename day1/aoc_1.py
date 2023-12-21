file1 = open("input.txt", "r")
lines = file1.readlines()
file1.close()

total = 0
for line in lines:   
    pivot1 = "0"
    pivot2 = "0"
    for char in line:
        if char.isnumeric():
            if pivot1 == "0":
                pivot1 = char
            else:
                pivot2 = char
    if pivot2 == "0":
        total += int(pivot1+pivot1)
    else:
        total += int(pivot1+pivot2)
print(total)
