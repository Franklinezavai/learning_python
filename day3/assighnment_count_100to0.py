for number in range(100, 0, -1):
    if number > 0:
        print(f'{number} is positive')
        if number % 2 == 0:
            print(f"{number} is an even number")
        else:
            print(f"{number} is an odd number")