n = [ 3, 1, 5, 19 , 45, 24, 34]
# n.sort()
# print(n)
# n.sort(reverse=True)
# print(n)

print("Ascending :" ,sorted(n))
print("Descending : " , sorted(n, reverse=True))


numbers = []
for i in range(10):
    value = int(input(f"Enter numbers {i + 1}: " ))
    numbers.append(value)


ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)
print("original list: ", numbers )
print("Ascending order : ", ascending )
print("Descending Order : ", descending)
print("Largest number : ", ascending[-1])
print("smallest number : " , ascending[0])
print("Total sum : ", sum(numbers))
