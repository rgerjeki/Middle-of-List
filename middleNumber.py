numbers = [1, 5, 7, 8, 10, 3, 5, 4, 10, 4, 7, 28, 54, 97, 28]

if len(numbers) % 2: 
    middle_list = int(len(numbers) // 2)
    print(numbers[middle_list])
        
else:
    middle_list = int(len(numbers) // 2) - 1
    middle_list_two = int(len(numbers) // 2) 
    print(numbers[middle_list])
    print(numbers[middle_list_two])

