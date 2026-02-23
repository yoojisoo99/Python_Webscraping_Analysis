origin_text = "Python is awesome programming language"
split_list = origin_text.split()
hyphen_list = "-".join(split_list)
upper_list = " ".join([word.upper() for word in split_list])
print(f"원본 문자열: {origin_text}")
print(f"분리된 단어들: {split_list}")
print(f"하이픈으로 연결: {hyphen_list}")
print(f"대문자로 변환 후 공백으로 연결: {upper_list}")
