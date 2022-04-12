# Metode Pangkat-Kali (SM)

import timeit
print("Pangkat Modulo x^b mod n")
x = int(input("Nilai x : "))
b = int(input("Nilai b : "))
n = int(input("Nilai n : "))
start = timeit.default_timer()
a = bin(b)
c = [1]
for i in range(2, len(a)):
    c[0] = (pow(c[0], 2)) % n
    if (a[i] == '1'):
        c[0] = (c[0]*x) % n

stop = timeit.default_timer()
print("x^b mod n = ", c[0])

print('Time: ', stop - start)
