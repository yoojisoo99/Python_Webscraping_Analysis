import json

data = {
    "이름": "김철수",
    "나이": 25,
    "직업": "개발자",
    "취미": ["독서", "영화감상", "코딩"],
    "주소": "서울시 강남구"
}

file_path = 'data.json'
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"데이터가 {file_path}에 저장되었습니다.\n")

with open(file_path, 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)

print("JSON에서 읽어온 데이터:")
print(f"이름: {loaded_data['이름']}")
print(f"나이: {loaded_data['나이']}")
print(f"직업: {loaded_data['직업']}")
print(f"취미: {loaded_data['취미']}")
print(f"주소: {loaded_data['주소']}")