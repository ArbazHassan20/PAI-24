def avg(lst):
    total = count = 0
    for i in lst:
        total += i
        count += 1
    return total / count

def sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp

def delete(lst, day):
    lst.pop(day)

# New temperature data
temperatures = [25, 27, 26, 24, 23, 22, 25, 26, 27, 28, 29, 30,
                28, 27, 26, 25, 24, 23, 25, 26, 27, 28, 29, 30,
                28, 27, 26, 25, 24, 23, 22, 23, 24, 25, 26, 27,
                28, 29, 30, 31, 32, 31, 30, 29, 28, 27, 26, 25]

sort(temperatures)
print("Sorted list:", temperatures)
print("Lowest temperature:", temperatures[0])
print("Highest temperature:", temperatures[-1])
print("Average temperature:", avg(temperatures))
print("Removing temperature for day 1...")
delete(temperatures, 0)
print("Updated temperatures:", temperatures)
