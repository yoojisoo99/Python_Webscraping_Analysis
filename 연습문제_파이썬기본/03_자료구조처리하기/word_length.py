words = ['cat', 'elephant', 'dog', 'butterfly', 'ant']
max_val = max(words, key=len)
min_val = min(words, key=len)
print(f"단어 목록: {words}")
print(f"가장 긴 단어: {max_val}")
print(f"가장 짧은 단어: {min_val}")