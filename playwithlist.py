L = [5, 3, 1, 7, 9, 8, 2, 4, 6, 10]
print("Orignal list is", L)

count = 0

for i in L:
    count += i

avg = count/len(L)

print("Sum =", count)
print("Average = ", avg)

L.sort()
print("Smallest element is", L[0])
print("The largest element is", L[-1])