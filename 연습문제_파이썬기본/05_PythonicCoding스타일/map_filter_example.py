numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
big_numbers = list(filter(lambda x: x > 5, numbers))
squared = list(map(lambda x: x**2, numbers))
squared_big_numbers = list(map(lambda x: x**2, big_numbers))
print(f"원본 숫자: {numbers}")
print(f"모든 수의 제곱: {squared}")
print(f"5보다 큰 수들: {big_numbers}")
print(f"5보다 큰 수들의 제곱: {squared_big_numbers}")