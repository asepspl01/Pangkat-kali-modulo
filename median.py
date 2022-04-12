print()
print("=========== MEDIAN ===========")
print()

#n = int(input("Banyak data : "))
data = []

for i in range(6):
    a = int(input("Data ke-%d : " % (i+1)))
    data.append(a)
    data.sort()
    b = len(data)
    x1 = data[b//2]
    x2 = data[(b//2)-1]

    median = (x1+x2)/2

print("Median : %0.2f " % median)
