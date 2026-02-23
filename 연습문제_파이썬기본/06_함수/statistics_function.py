import math

def print_stats(numbers):
    n = len(numbers)
    avg_val = sum(numbers) / n
    max_val = max(numbers)
    min_val = min(numbers)
  
    variance = sum((x - avg_val) ** 2 for x in numbers) / (n - 1)
    std_dev = math.sqrt(variance)

   
    print(f"숫자들: {numbers}")
    print(f"평균: {avg_val:.1f}")
    print(f"최댓값: {max_val}")
    print(f"최솟값: {min_val}")
    print(f"표준편차: {std_dev:.2f}")

numbers = [10, 20, 30, 40, 50]
print_stats(numbers)