result = 0
list_number = []
for num in range(1,1000):
    if num % 3 == 0 or num % 5 ==0:
        result +=num
        list_number.append(num)

print("Sum of numbers divisible by 3 or 5 below 1000 without exceeding 1000:", result)
print("List of numbers:", list_number)


# advance code

list_number = [num for num in range(1, 1000) if num % 3 == 0 or num % 5 == 0]
result = sum(list_number)

print("Sum of numbers divisible by 3 or 5 below 1000:", result)
print("List of numbers:", list_number)


