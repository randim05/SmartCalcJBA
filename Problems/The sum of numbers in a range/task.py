def range_sum(numbers, start, end):
    start = int(start)
    end = int(end)
    numbers = [int(i) for i in numbers]
    sum = 0
    if len(numbers) == 0:
        return 0
    for i in numbers:
        if start <= i <= end:
            sum += i
    return sum


input_numbers = input().split(" ")
a, b = input().split(" ")
print(range_sum(input_numbers, a, b))
