num = [2, 4, 6, 8, 10]
num2 = [1, 3, 5, 7, 12]

is_all_even = all(n % 2 == 0 for n in num)
has_big_number = any(n > 10 for n in num)

is_all_even2 = all(n % 2 == 0 for n in num2)
has_big_number2 = any(n > 10 for n in num2)

print(f"숫자 리스트:{num}")
print(f"모든 수가 짝수인가? {is_all_even}")
print(f"하나라도 10보다 큰 수가 있는가? {has_big_number}")

print(f"숫자 리스트2:{num2}")
print(f"모든 수가 짝수인가? {is_all_even2}")
print(f"하나라도 10보다 큰 수가 있는가? {has_big_number2}")