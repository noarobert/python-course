numbers = [8, 7, 11, 7, 2, 10, 5, 8]
result=[]

for number in numbers:
    if numbers not in result:
        result.append(number)

print(result)

#result = [8, 7, 11, 2, 10, 5]
