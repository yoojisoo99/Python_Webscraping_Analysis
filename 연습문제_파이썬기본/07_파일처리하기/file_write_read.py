lines = [
    "안녕하세요\n",
    "파이썬 파일 처리를 연습하고 있습니다\n",
    "오늘은 좋은 날씨입니다\n"
]

file_path = "practice.txt"
with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("파일에 저장할 내용:")
for line in lines:
    print(line.strip())

print("파일에서 읽어온 내용:")
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)