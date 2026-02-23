numbers = [15, 3, 27, 8, 19, 12, 31]
max_val = max(numbers)
min_val = min(numbers)
second_max = max([n for n in numbers if n != max_val])
print(f"숫자 목록: {numbers}")
print(f"최댓값: {max_val}")
print(f"최솟값: {min_val}")
print(f"두 번째로 큰 값: {second_max}")