cart = {
    "사과": [2, 1000],
    "바나나": [3, 800],
    "오렌지": [1, 1500]
}
total_price = 0
print(f"쇼핑카트: ")
for item, info in cart.items():
    count = info[0]  
    price = info[1]  
    subtotal = count * price  
    total_price += subtotal
    print(f"{item}: {count}개 (개당 {price}원) = {subtotal}원")
print(f"총 가격: {total_price}원")