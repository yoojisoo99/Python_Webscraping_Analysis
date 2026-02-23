squares = {x: x**2 for x in range(1, 6)}
even_squares = {x: x**2 for x in range(1, 11) if x%2==0 }
print(f"1부터 5까지의 제곱 딕셔너리: {squares}")
print(f"짝수만의 제곱 딕셔너리: {even_squares}")