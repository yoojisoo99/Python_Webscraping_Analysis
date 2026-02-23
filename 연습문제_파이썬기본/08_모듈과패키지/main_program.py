import math_operations

def main():
    circle_res = math_operations.get_circle_area(5)
    print(f"원의 넓이: {circle_res}")

    rect_res = math_operations.get_rectangle_area(5, 10)
    print(f"직사각형 넓이: {rect_res}")

    fact_res = math_operations.get_factorial(5)
    print(f"팩토리얼 5! = {fact_res}")

    gcd_res = math_operations.get_gcd(48, 18)
    print(f"최대공약수(48, 18) = {gcd_res}")

if __name__ == "__main__":
    main()